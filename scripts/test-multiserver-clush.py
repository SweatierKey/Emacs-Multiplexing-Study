#!/usr/bin/env python3
"""Test unmodified clush against loopback SSH; record its actual Emacs shell UI.

The launcher only isolates source/config paths. Scheduling, SSH, collection and
per-host files are all supplied by ClusterShell. No custom Emacs collector.
Requires scripts/lab.py start and the pinned ClusterShell source in sources/.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time

from record import ROOT, Session

REVISION = 'f3f5b1594be3350b0c29bcc6786cff86abba19d7'
NAME = 'multiserver-clush'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-ui', action='store_true')
    args = parser.parse_args()
    runtime = ROOT / '.runtime' / NAME
    runtime.mkdir(exist_ok=True)
    config = runtime / 'clush.conf'
    config.write_text('[Main]\nfanout: 64\nconnect_timeout: 5\ncommand_timeout: 12\n'
                      'maxrc: yes\nssh_options: -F ' + str(ROOT / '.runtime/ssh_config') + '\n')
    (runtime / 'groups.conf').write_text('[Main]\n')
    launch = runtime / 'clush'
    launch.write_text('#!/bin/sh\nexport PYTHONPATH=' + shlex.quote(str(ROOT / 'sources/clustershell/lib')) +
                      '\nexec python3 -m ClusterShell.CLI.Clush --worker ssh --conf ' +
                      shlex.quote(str(config)) + ' "$@"\n')
    launch.chmod(0o755)
    env = dict(os.environ, CLUSTERSHELL_CFGDIR=str(runtime))
    result = {'id': NAME, 'status': 'running', 'source_revision': REVISION,
              'topology': 'two real loopback SSH endpoints on the same kernel; flat SSH worker',
              'checks': {}, 'runs': []}

    def run(label, options, command, stdin=None):
        argv = [str(launch), *options, command]
        if stdin is None:
            argv.insert(1, '-n')
        start = time.monotonic()
        p = subprocess.run(argv, cwd=ROOT, env=env, input=stdin or '', text=True,
                           capture_output=True, timeout=25)
        row = {'name': label, 'argv': argv, 'stdin': stdin, 'exit': p.returncode,
               'elapsed': time.monotonic() - start, 'stdout': p.stdout, 'stderr': p.stderr}
        result['runs'].append(row)
        return row

    def times(row):
        found = re.findall(r'^lab-(web|db): (START|END) (\d+)\s*$', row['stdout'], re.M)
        out = {}
        for role, phase, stamp in found:
            out.setdefault(role, {})[phase] = int(stamp)
        assert set(out) == {'web', 'db'} and all(set(v) == {'START', 'END'} for v in out.values()), out
        return out

    s = None
    try:
        assert (ROOT / '.runtime/lab-state.json').exists(), 'Start scripts/lab.py first'
        source = ROOT / 'sources/clustershell'
        # Archive installations have no .git: provenance is checked by the bundle manifest.
        if (source / '.git').exists():
            rev = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
            assert rev == REVISION, rev
        hosts = ['--hostfile', 'lab/multiserver/hosts.txt']
        timing = 'printf "START %s\\n" "$(date +%s%N)"; sleep 2; printf "END %s\\n" "$(date +%s%N)"'
        single = run('single-host', ['-w', 'lab-web'], 'cat status.txt')
        result['checks']['single_host'] = single['exit'] == 0 and 'role=web' in single['stdout'] and 'role=db' not in single['stdout']
        parallel = run('parallel', [*hosts, '-f', '2'], timing)
        pt = times(parallel)
        result['parallel_intervals_ns'] = pt
        result['checks']['parallel_overlap'] = parallel['exit'] == 0 and max(t['START'] for t in pt.values()) < min(t['END'] for t in pt.values())
        serial = run('serial', [*hosts, '-f', '1'], timing)
        st = times(serial)
        result['serial_intervals_ns'] = st
        ordered = sorted(st, key=lambda host: st[host]['START'])
        result['observed_serial_order'] = ordered
        result['checks']['serial_no_overlap'] = serial['exit'] == 0 and st[ordered[1]]['START'] >= st[ordered[0]]['END']
        result['inventory_order_preserved'] = ordered == ['web', 'db']
        script = (ROOT / 'lab/multiserver/check.sh').read_text()
        checks = run('script-stdin', [*hosts, '-b'], 'sh -s', script)
        result['checks']['script_on_both'] = checks['exit'] == 0 and all('CHECK role=' + role in checks['stdout'] for role in ('web', 'db'))
        # The fixture banner differs by role: -b therefore creates two labelled
        # groups in one output stream. Deduplication is not asserted here.
        gathered = run('gathered-labelled-output', [*hosts, '-b'], 'printf "HEALTH_OK\\n"')
        result['checks']['combined_labelled_output'] = gathered['exit'] == 0 and all('lab-' + role in gathered['stdout'] for role in ('web', 'db')) and gathered['stdout'].count('HEALTH_OK') == 2
        outdir, errdir = runtime / 'stdout', runtime / 'stderr'
        separate = run('per-host-files', [*hosts, '--outdir', str(outdir), '--errdir', str(errdir)],
                       'printf "STDOUT_%s\\n" "$STUDY_ROLE"; printf "STDERR_%s\\n" "$STUDY_ROLE" >&2')
        result['per_host_files'] = {f'{stream}/{host}': (directory / host).read_text()
            for stream, directory in [('stdout', outdir), ('stderr', errdir)] for host in ['lab-web', 'lab-db']}
        result['checks']['separate_stdout_stderr_files'] = separate['exit'] == 0 and all(
            f'STDOUT_{role}' in result['per_host_files']['stdout/lab-' + role] and
            f'STDERR_{role}' in result['per_host_files']['stderr/lab-' + role] for role in ('web', 'db'))
        failed = run('remote-exit-status', [*hosts, '-S'], 'if [ "$STUDY_ROLE" = db ]; then echo CHECK_FAILED >&2; exit 7; fi; echo CHECK_OK')
        result['checks']['failure_status_reported'] = failed['exit'] == 7 and 'CHECK_OK' in failed['stdout'] and 'CHECK_FAILED' in failed['stderr']
        timeout = run('command-timeout', ['-w', 'lab-web', '-S', '-u', '1'], 'sleep 3; echo TOO_LATE')
        result['checks']['command_timeout'] = timeout['exit'] == 255 and 'TOO_LATE' not in timeout['stdout']
        if not args.no_ui:
            s = Session(NAME, "(require 'shell)", width=120, height=35,
                        env_override={'PATH': str(runtime) + ':' + os.environ['PATH'], 'CLUSTERSHELL_CFGDIR': str(runtime)})
            s.mx('shell')
            s.command('clush -n -w lab-web cat status.txt', 1.5)
            s.command('clush -n --hostfile lab/multiserver/hosts.txt -f 2 ' + shlex.quote(timing), 3.5)
            s.command('clush -n --hostfile lab/multiserver/hosts.txt -f 1 ' + shlex.quote(timing), 5.5)
            s.command('clush --hostfile lab/multiserver/hosts.txt -b sh -s < lab/multiserver/check.sh', 1.5)
            aggregate = s.snapshot()
            result['ui_aggregate'] = aggregate
            result['checks']['emacs_aggregate_buffer'] = aggregate['mode'] == 'shell-mode' and all('CHECK role=' + role in aggregate['text'] for role in ('web', 'db'))
            s.command('clush -n --hostfile lab/multiserver/hosts.txt --outdir .runtime/multiserver-clush/ui-output cat status.txt', 1.5)
            snapshots = []
            for role in ['web', 'db']:
                s.key(b'\x18\x06', 'C-x C-f')
                s.key(str(runtime / 'ui-output' / ('lab-' + role)), 'open clush output file: ' + role)
                s.key(b'\r', 'RET', 1)
                snapshots.append(s.snapshot())
            result['ui_file_buffers'] = snapshots
            result['checks']['separate_file_buffers_manually_opened'] = snapshots[0]['name'] != snapshots[1]['name'] and all('role=' + role in snap['text'] for role, snap in zip(['web', 'db'], snapshots))
            result['checks']['vertico_and_marginalia'] = all(x['vertico'] and x['marginalia'] for x in [aggregate, *snapshots])
            s.key(b'\x18b', 'C-x b'); s.key('*shell*', 'select aggregate shell'); s.key(b'\r', 'RET', 1)
        result['status'] = 'passed' if all(result['checks'].values()) else 'failed'
    except Exception as exc:
        result.update(status='failed', error=repr(exc))
        raise
    finally:
        if s:
            s.close()
        (ROOT / 'results' / (NAME + '.json')).write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps({'status': result['status'], 'checks': result['checks'], 'observed_serial_order': result.get('observed_serial_order')}, indent=2))
    if result['status'] != 'passed':
        sys.exit(1)


if __name__ == '__main__':
    main()
