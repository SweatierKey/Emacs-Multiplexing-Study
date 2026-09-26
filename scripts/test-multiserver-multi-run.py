#!/usr/bin/env python3
"""Record multi-run's documented Eshell UI against two real loopback SSH roles.

Requires scripts/lab.py start.  No package code or keys are changed.  The only
SSH adjustment is a private PATH wrapper selecting the laboratory ssh_config.
An observed overlap is a successful verification of the *limitation*: a delay
between launches does not provide execution in series across hosts.
"""
from record import Session, ROOT
import json
import os
import pathlib
import re
import shlex
import sys
import time
import traceback

NAME = 'multiserver-multi-run'


def capture(s, name):
    form = ('(with-current-buffer ' + json.dumps(name) +
            ' (json-encode `((name . ,(buffer-name))'
            ' (mode . ,(symbol-name major-mode))'
            ' (text . ,(buffer-substring-no-properties (point-min) (point-max))))))')
    return json.loads(json.loads(s.eval(form)))


def visit(s, name):
    s.key(b'\x18b', 'C-x b: switch-to-buffer')
    s.command(name)


def run():
    result = {
        'id': NAME,
        'status': 'running',
        'started': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'source_revision': '13d4d923535b5e8482b13ff76185203075fb26a3',
        'scenario': 'Documented master Eshell UI; two live SSH roles; delay versus strict series',
        'lab': 'Two loopback SSH endpoints on the same kernel; their clock is shared.',
        'configuration': {
            'completion': ['vertico', 'marginalia'],
            'package_changes': [],
            'keymap_changes': [],
            'ssh': 'Private PATH wrapper: /usr/bin/ssh -F .runtime/ssh_config',
        },
        'checks': {},
        'snapshots': [],
        'timings': {},
    }
    bindir = ROOT / '.runtime' / (NAME + '-bin')
    bindir.mkdir(parents=True, exist_ok=True)
    wrapper = bindir / 'ssh'
    wrapper.write_text('#!/bin/sh\nexec /usr/bin/ssh -F ' +
                       shlex.quote(str(ROOT / '.runtime/ssh_config')) + ' "$@"\n')
    wrapper.chmod(0o755)
    s = None
    try:
        s = Session(NAME, "(require 'multi-run)\n", width=132, height=42,
                    env_override={'PATH': str(bindir) + ':' + os.environ['PATH']})
        result['checks']['completion_enabled'] = s.eval('(and vertico-mode marginalia-mode)') == 't'
        assert result['checks']['completion_enabled'], 'Vertico and Marginalia must both be enabled'
        s.mx('eshell')
        master = s.snapshot()['name']
        assert s.snapshot()['mode'] == 'eshell-mode'
        s.command('(setq multi-run-hostnames-list (list "lab-web" "lab-db"))')
        s.command('multi-run-configure-terminals 2', 1)
        assert s.snapshot()['name'] == master, 'Package did not return to master Eshell'
        s.command('multi-run-ssh', 2)
        s.command('multi-run "cat status.txt"', 1)
        for number, role in [(1, 'web'), (2, 'db')]:
            snap = capture(s, f'eshell<{number}>')
            result['snapshots'].append(snap)
            result['checks']['ssh_' + role] = bool(re.search(r'^role=' + role + r'\s*$', snap['text'], re.M))
            assert result['checks']['ssh_' + role], 'No actual remote output for ' + role

        for tag, delay in [('PARALLEL', 0), ('DELAY', 0.2)]:
            command = ("printf 'MS_" + tag + "_BEGIN_%s %s\\n' \"$STUDY_ROLE\" \"$(date +%s.%N)\"; "
                       "sleep 2; printf 'MS_" + tag + "_END_%s %s\\n' \"$STUDY_ROLE\" \"$(date +%s.%N)\"")
            if delay == 0:
                expression = '(multi-run ' + json.dumps(command) + ')'
            else:
                expression = '(multi-run-with-delay 0.2 ' + json.dumps(command) + ')'
            s.command(expression, 3.2)
            intervals = {}
            for number, role in [(1, 'web'), (2, 'db')]:
                snap = capture(s, f'eshell<{number}>')
                result['snapshots'].append(snap)
                row = {}
                for edge in ['BEGIN', 'END']:
                    match = re.search(r'^MS_' + tag + '_' + edge + '_' + role + r' (\d+\.\d+)\s*$',
                                      snap['text'], re.M)
                    assert match, f'Missing actual {tag} {edge} output for {role}'
                    row[edge.lower()] = float(match.group(1))
                assert row['end'] - row['begin'] >= 1.9, 'Remote workload did not run for two seconds'
                intervals[role] = row
            overlap = min(x['end'] for x in intervals.values()) - max(x['begin'] for x in intervals.values())
            result['timings'][tag.lower()] = {
                'configured_launch_delay_seconds': delay,
                'intervals': intervals,
                'observed_overlap_seconds': overlap,
                'host_start_gap_seconds': intervals['db']['begin'] - intervals['web']['begin'],
                'strict_series_observed': intervals['db']['begin'] >= intervals['web']['end'],
            }
            result['checks'][tag.lower() + '_overlaps'] = overlap > 0.5
            assert result['checks'][tag.lower() + '_overlaps'], 'Expected observable overlap missing'

        # These are ordinary default Emacs keys, displaying the actual buffers
        # that own the output.  Assertions above did not synthesize this output.
        for name in ['eshell<1>', 'eshell<2>', master]:
            visit(s, name)
            s.pump(1)
        result['checks']['separate_output_buffers'] = True
        result['status'] = 'passed'
        result['finding'] = ('Both broadcast and fixed-delay launches overlap. '
                             'multi-run-with-delay does not wait for host A to finish before starting host B.')
        result['capabilities_observed'] = {
            'host_list': True,
            'parallel': True,
            'separate_output_buffers': True,
            'strict_series_via_delay': False,
            'combined_output_buffer': 'No built-in collector found in source; not synthesized by this test.',
        }
    except Exception as exc:
        result['status'] = 'failed'
        result['error'] = str(exc)
        result['traceback'] = traceback.format_exc()
        if s:
            try:
                result['snapshots'].append(s.snapshot())
                result['messages'] = s.eval('(with-current-buffer "*Messages*" (buffer-string))')
            except Exception:
                pass
    finally:
        if s:
            s.close()
    target = ROOT / 'results' / (NAME + '.json')
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(NAME, result['status'], result.get('error', result.get('finding', '')), flush=True)
    if result['timings']:
        print(json.dumps(result['timings'], indent=2), flush=True)
    return result['status'] == 'passed'


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
