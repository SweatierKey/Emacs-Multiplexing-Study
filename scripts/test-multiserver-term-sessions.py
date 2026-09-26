#!/usr/bin/env python3
"""Exercise term-sessions' native marked-list actions through real Emacs keys.

Topology: two LOCAL, isolated zmx sessions, each containing a real SSH client
connected to one loopback fixture endpoint. This is not a remote-zmx/TRAMP test.
Emacsclient only observes state; no test helper implements sending or grouping.
Start the existing lab with scripts/lab.py before running this script.
"""
from record import Session, ROOT
import json
import re
import subprocess
import sys
import time
import traceback

NAME = 'multiserver-term-sessions'
TARGETS = ('fleet-web', 'fleet-db')


def observe(session, form):
    return json.loads(json.loads(session.eval('(json-encode ' + form + ')')))


def selected(session, form):
    return '(with-current-buffer (window-buffer (selected-window)) ' + form + ')'


def line_mode(session):
    if session.eval(selected(session, "(and (derived-mode-p 'term-mode) (term-in-char-mode))")) == 't':
        session.key(b'\x03\x0a', 'C-c C-j: term line mode')


def terminal_snapshot(session, buffer_name):
    return observe(session, '(with-current-buffer ' + json.dumps(buffer_name) +
                   ' `((name . ,(buffer-name)) (text . ,(buffer-string))'
                   ' (visible . ,(if (get-buffer-window (current-buffer) t) t :json-false))))')


def marked_names(session):
    return observe(session, selected(session,
        '(vconcat (mapcar (lambda (entry) (plist-get entry :name)) term-sessions-list--marked-entries))'))


def main():
    session = None
    result = {
        'id': NAME, 'status': 'failed', 'checks': {}, 'snapshots': [],
        'topology': 'Two local zmx sessions; each runs SSH to one loopback fixture. '
                    'Both SSH endpoints share one kernel. Remote zmx/TRAMP is not tested.',
        'scope': 'Native list marking, command dispatch to hidden terminals, real overlapping execution, separate output buffers.',
        'source_commit': '29084b6a8a73b612f60a73ef798303384bd44215',
        'limitations': ['No native host-inventory import is exercised.',
                        'No serial execution barrier or aggregated output is provided by this scenario.',
                        'Parallelism is observed shell execution after independent input delivery; no job tracking is asserted.'],
    }
    try:
        assert (ROOT / '.runtime/lab-state.json').exists(), 'Start scripts/lab.py first'
        setup = "(require 'term-sessions)\n(setq term-sessions-default-command (expand-file-name \"lab/bash\" study-root))\n"
        session = Session(NAME, setup, width=130, height=34)
        result['checks']['vertico_marginalia_enabled'] = session.eval('(and vertico-mode marginalia-mode)') == 't'
        assert result['checks']['vertico_marginalia_enabled']
        terminals = {}
        for role, target in zip(('web', 'db'), TARGETS):
            line_mode(session)
            session.mx('term-sessions-open')
            session.command(target, 1.2)
            session.command('lab-ssh lab-' + role, 1)
            session.command('cat status.txt', .6)
            snapshot = session.snapshot()
            assert re.search(r'^role=' + role + r'\s*$', snapshot['text'], re.M), snapshot
            terminals[role] = snapshot['name']
            result['snapshots'].append(snapshot)
        assert len(set(terminals.values())) == 2
        result['buffers'] = terminals
        result['checks']['two_real_ssh_connections_in_distinct_buffers'] = True

        line_mode(session)
        session.mx('term-sessions-list')
        session.key(b'\x18\x31', 'C-x 1: show only the session list')
        session.key(b'\x1b<', 'M-<: first session row')
        session.key('m', 'm: mark one session')
        one = marked_names(session)
        assert len(one) == 1 and one[0] in TARGETS, one
        result['single_selection'] = one
        session.key('s', 's: native send-command to marked session')
        session.command("printf 'SELECTED_ONLY role=%s\\n' \"$STUDY_ROLE\"", .8)
        single_output = {role: terminal_snapshot(session, name) for role, name in terminals.items()}
        recipient_roles = [role for role, snap in single_output.items()
                           if re.search(r'^SELECTED_ONLY role=' + role + r'\s*$', snap['text'], re.M)]
        assert recipient_roles == [one[0].removeprefix('fleet-')], recipient_roles
        result['checks']['m_s_targets_only_marked_session'] = True
        result['single_output'] = single_output

        session.key('U', 'U: unmark all')
        session.key('T', 'T: mark all listed sessions')
        assert set(marked_names(session)) == set(TARGETS)
        result['snapshots'].append(session.snapshot())
        before = {role: terminal_snapshot(session, name) for role, name in terminals.items()}
        assert all(not snap['visible'] for snap in before.values()), before
        result['checks']['both_terminal_buffers_hidden_before_dispatch'] = True
        command = ("printf 'BATCH_BEGIN role=%s ns=%s\\n' \"$STUDY_ROLE\" \"$(date +%s%N)\"; "
                   "sleep 2; printf 'BATCH_END role=%s ns=%s\\n' \"$STUDY_ROLE\" \"$(date +%s%N)\"")
        result['command'] = command
        session.key('s', 's: native send-command to both marked sessions')
        session.command(command, .15)
        session.pump(3)
        after = {role: terminal_snapshot(session, name) for role, name in terminals.items()}
        intervals = {}
        for role, snap in after.items():
            assert not snap['visible'], 'Dispatch unexpectedly displayed terminal'
            start = re.findall(r'^BATCH_BEGIN role=' + role + r' ns=(\d+)\s*$', snap['text'], re.M)
            end = re.findall(r'^BATCH_END role=' + role + r' ns=(\d+)\s*$', snap['text'], re.M)
            assert len(start) == len(end) == 1, snap['text']
            intervals[role] = {'start_ns': int(start[0]), 'end_ns': int(end[0])}
            assert intervals[role]['end_ns'] - intervals[role]['start_ns'] >= 1_900_000_000
        overlap = min(v['end_ns'] for v in intervals.values()) - max(v['start_ns'] for v in intervals.values())
        assert overlap > 0, intervals
        result['intervals'] = intervals
        result['overlap_seconds'] = overlap / 1e9
        result['hidden_output'] = after
        result['checks']['T_s_reaches_both_hidden_terminals'] = True
        result['checks']['remote_command_intervals_overlap'] = True
        result['checks']['outputs_remain_separate'] = True

        # Show the actual outputs in the video using ordinary buffer selection.
        for role, buffer_name in terminals.items():
            line_mode(session)
            session.key(b'\x18b', 'C-x b: inspect ' + role + ' output')
            session.command(buffer_name, 1.5)
            snapshot = session.snapshot()
            assert snapshot['name'] == buffer_name
            result['snapshots'].append(snapshot)
        line_mode(session)
        session.mx('term-sessions-list')
        session.pump(1)
        result['status'] = 'passed'
    except Exception as exc:
        result['error'] = str(exc)
        result['traceback'] = traceback.format_exc()
        if session:
            try:
                result['snapshots'].append(session.snapshot())
                result['messages'] = session.eval('(with-current-buffer "*Messages*" (buffer-string))')
            except Exception:
                pass
    finally:
        if session:
            session.close()
            cleanup = []
            for target in TARGETS:
                proc = subprocess.run([str(ROOT / '.runtime/bin/zmx'), 'kill', target],
                                      env=session.env, capture_output=True, text=True, timeout=10)
                cleanup.append({'target': target, 'returncode': proc.returncode,
                                'stdout': proc.stdout, 'stderr': proc.stderr})
            remaining = subprocess.run([str(ROOT / '.runtime/bin/zmx'), 'list'],
                                       env=session.env, capture_output=True, text=True, timeout=10)
            result['cleanup'] = {'kill': cleanup, 'remaining_stdout': remaining.stdout,
                                 'remaining_stderr': remaining.stderr, 'returncode': remaining.returncode}
            result['checks']['isolated_zmx_sessions_removed'] = not any(t in remaining.stdout for t in TARGETS)
            if not result['checks']['isolated_zmx_sessions_removed']:
                result['status'] = 'failed'
        (ROOT / 'results' / (NAME + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'checks': result['checks'],
                      'overlap_seconds': result.get('overlap_seconds'), 'error': result.get('error')}, indent=2))
    return result['status'] != 'passed'


if __name__ == '__main__':
    sys.exit(main())
