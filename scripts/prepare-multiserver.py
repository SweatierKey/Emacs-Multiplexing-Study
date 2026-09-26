#!/usr/bin/env python3
"""Prepare the standalone multi-server study offline; do not start SSH servers.

The bundled zmx executable is the upstream Linux x86_64 release.  All generated
state stays in .runtime except Emacs bytecode compiled beside the compat source.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tarfile


ROOT = Path(__file__).resolve().parents[1]
ZMX_ARCHIVE = 'native/zmx-0.8.1-linux-x86_64.tar.gz'
ZMX_SHA256 = 'dfd75720b942466f28870731cc86dbc07afa72fb8f3bd5eeb4ff707e4eecebe8'


def prepare(root, emacs):
    runtime = root / '.runtime'
    for name in ['bin', 'terminfo', 'emacs', 'sockets', 'smoke-home', 'smoke-xdg']:
        (runtime / name).mkdir(parents=True, exist_ok=True)
    for name in ['results', 'recordings']:
        (root / name).mkdir(exist_ok=True)
    for name in ['sockets', 'smoke-xdg']:
        (runtime / name).chmod(0o700)
    required = [emacs, 'emacsclient', 'ssh', 'ssh-keygen', 'tic', 'bash']
    missing = [name for name in required if not shutil.which(name)]
    if not Path('/usr/sbin/sshd').is_file():
        missing.append('/usr/sbin/sshd')
    if missing:
        raise RuntimeError('Missing prerequisites: ' + ', '.join(missing) +
                           '. See README-MULTISERVER.md for Debian packages.')
    if platform.system() != 'Linux' or platform.machine() not in ('x86_64', 'amd64'):
        raise RuntimeError('The bundled zmx binary needs Linux x86_64. '
                           'Install the matching upstream zmx 0.8.1 build for another platform.')
    archive = root / ZMX_ARCHIVE
    actual = hashlib.sha256(archive.read_bytes()).hexdigest()
    if actual != ZMX_SHA256:
        raise RuntimeError('Unexpected zmx archive SHA256: ' + actual)
    with tarfile.open(archive, 'r:gz') as tf:
        entries = [m for m in tf.getmembers() if m.isfile() and Path(m.name).name == 'zmx']
        if len(entries) != 1:
            raise RuntimeError('Expected one ordinary zmx executable in the release archive')
        with tf.extractfile(entries[0]) as source:
            (runtime / 'bin/zmx').write_bytes(source.read())
    (runtime / 'bin/zmx').chmod(0o755)

    env = dict(os.environ, HOME=str(runtime / 'smoke-home'),
               XDG_RUNTIME_DIR=str(runtime / 'smoke-xdg'), LC_ALL='C.UTF-8')
    env.pop('STUDY_SPEC', None)
    env.pop('STUDY_SERVER', None)
    steps = []

    def run(label, argv, timeout=90, extra_env=None):
        proc = subprocess.run(argv, cwd=root, env=extra_env or env, text=True,
                              capture_output=True, timeout=timeout)
        steps.append({'step': label, 'argv': argv, 'returncode': proc.returncode,
                      'stdout': proc.stdout, 'stderr': proc.stderr})
        if proc.returncode:
            raise RuntimeError(label + ' failed: ' + (proc.stderr or proc.stdout))
        return proc.stdout

    try:
        version = run('Emacs version', [emacs, '-Q', '--batch', '--eval',
                      '(progn (when (version< emacs-version "29.1") '
                      '(error "Emacs 29.1 or newer required")) (princ emacs-version))'])
        # Compat installs some definitions while byte compiling.  Rebuild on the
        # actual Emacs version rather than distributing machine-specific .elc.
        compat = root / 'sources/compat'
        files = sorted(str(p) for p in compat.glob('compat*.el') if p.name != 'compat-tests.el')
        if not files:
            raise RuntimeError('Missing sources/compat source snapshot')
        run('Compile Compat', [emacs, '-Q', '--batch', '-L', str(compat),
                              '-f', 'batch-byte-compile', *files])
        terminfo = root / 'sources/term/eterm-color.ti'
        if not terminfo.is_file():
            located = run('Locate system terminfo source', [emacs, '-Q', '--batch', '--eval',
                          '(princ (expand-file-name "e/eterm-color.ti" data-directory))']).strip()
            terminfo = Path(located)
        if not terminfo.is_file():
            raise RuntimeError('Missing eterm-color.ti source (snapshot or Emacs data-directory)')
        run('Compile Eterm terminfo', ['tic', '-x', '-o', str(runtime / 'terminfo'), str(terminfo)])
        extra_ti = root / 'sources/eterm-256color/eterm-256color.ti'
        if extra_ti.is_file():
            ti_env = dict(env, TERMINFO_DIRS=str(runtime / 'terminfo') + ':/usr/share/terminfo:/lib/terminfo')
            run('Compile Eterm 256-color terminfo', ['tic', '-x', '-o', str(runtime / 'terminfo'), str(extra_ti)], extra_env=ti_env)
        smoke = """(progn
          (dolist (feature '(term-sessions multi-run cssh telecommand init-ssh ssh-manager))
            (require feature))
          (unless (and vertico-mode marginalia-mode) (error "Completion modes inactive"))
          (unless (fboundp 'set-local) (error "Compat definitions not installed"))
          (princ (json-encode `((emacs . ,emacs-version)
            (vertico . ,vertico-mode) (marginalia . ,marginalia-mode)
            (term_sessions . ,(featurep 'term-sessions))
            (multi_run . ,(featurep 'multi-run))))))"""
        run('Offline Emacs source-load smoke', [emacs, '-Q', '--batch', '-l',
                                             str(root / 'config/init.el'), '--eval', smoke])
        csenv = dict(env, PYTHONPATH=str(root / 'sources/clustershell/lib'))
        run('Offline ClusterShell import smoke', [sys.executable, '-c',
            'from ClusterShell.CLI import Clush; from ClusterShell.NodeSet import NodeSet; '
            'assert len(NodeSet("node[1-2]")) == 2; print("ClusterShell import and NodeSet OK")'],
            extra_env=csenv)
        result = {'status': 'passed', 'emacs_version': version, 'zmx_archive_sha256': actual,
                  'network_used': False, 'ssh_servers_started': False, 'steps': steps}
    except Exception as exc:
        result = {'status': 'failed', 'error': str(exc), 'steps': steps}
        (runtime / 'prepare-multiserver.json').write_text(json.dumps(result, indent=2) + '\n')
        raise
    (runtime / 'prepare-multiserver.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT,
                        help='Study root; useful for checking a freshly extracted bundle')
    parser.add_argument('--emacs', default='emacs')
    args = parser.parse_args()
    result = prepare(args.root.resolve(), args.emacs)
    print(json.dumps({k: v for k, v in result.items() if k != 'steps'}, indent=2))


if __name__ == '__main__':
    main()
