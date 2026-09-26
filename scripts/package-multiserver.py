#!/usr/bin/env python3
"""Create a standalone, explicitly scoped multi-server study archive.

Run only after the report and recordings are final.  Refuses to replace an
existing archive.  Excludes runtime state, credentials, VCS metadata and caches.
"""
import argparse
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tarfile


ROOT = Path(__file__).resolve().parents[1]
STEM = 'Emacs-Multiserver-Followup-2026-09-26'
SOURCE_NAMES = ('compat', 'vertico', 'marginalia', 'term-sessions', 'multi-run',
                'window-layout', 'dash', 'f', 's', 'term', 'eterm-256color',
                'clustershell', 'cssh', 'telecommand', 'emacs-ssh-machines',
                'dotfairy-ssh-manager', 'nssh')
SKIP_PARTS = {'.git', '.hg', '.svn', '.runtime', '__pycache__', '.pytest_cache',
              '.mypy_cache', '.zig-cache', 'node_modules', 'target'}
SKIP_SUFFIXES = {'.pyc', '.pyo', '.elc', '.eln'}
ZMX = 'native/zmx-0.8.1-linux-x86_64.tar.gz'
ZMX_SHA256 = 'dfd75720b942466f28870731cc86dbc07afa72fb8f3bd5eeb4ff707e4eecebe8'


def eligible(path):
    return not (SKIP_PARTS.intersection(path.parts) or path.suffix in SKIP_SUFFIXES)


def collect(root):
    files = {}

    def add(path):
        rel = path.relative_to(root)
        if not eligible(rel):
            return
        if path.is_symlink():
            raise RuntimeError('Review source symlink before bundling: ' + str(rel))
        if path.is_file():
            files[str(rel)] = path
        elif path.is_dir():
            for item in sorted(path.rglob('*')):
                if eligible(item.relative_to(root)) and item.is_file():
                    add(item)

    mandatory = ['config/init.el', 'lab/bash', 'lab/remote-shell.sh',
                 'scripts/record.py', 'scripts/lab.py', 'scripts/prepare-multiserver.py',
                 'scripts/package-multiserver.py', 'report/MULTISERVER.md',
                 'report/MULTISERVER.html', 'report/style.css', ZMX, ZMX + '.sha256']
    for name in mandatory:
        path = root / name
        if not path.is_file():
            raise RuntimeError('Required bundle input is missing: ' + name)
        add(path)
    for name in SOURCE_NAMES:
        path = root / 'sources' / name
        if not path.is_dir():
            raise RuntimeError('Missing pinned source: ' + str(path))
        add(path)
    for pattern in ['lab/multiserver/**', 'lab/fixtures/**', 'player/*',
                    'scripts/test-multiserver*.py', 'scripts/build-multiserver.py',
                    'results/multiserver*.json', 'recordings/multiserver*.cast',
                    'research/multiserver*.json', 'wheels/markdown*.whl']:
        for path in sorted(root.glob(pattern)):
            add(path)
    for name in ['clush', 'multi-run', 'term-sessions']:
        for pattern in [f'scripts/test-multiserver-{name}.py',
                        f'results/multiserver-{name}.json',
                        f'recordings/multiserver-{name}.cast']:
            if pattern not in files:
                raise RuntimeError('Required scenario artifact missing: ' + pattern)
    if hashlib.sha256((root / ZMX).read_bytes()).hexdigest() != ZMX_SHA256:
        raise RuntimeError('zmx release archive does not match the pinned SHA256')
    return files


def provenance(root, files):
    lock = root / 'research/source-lock.json'
    previous = root / 'research/multiserver-bundle-sources.json'
    rows = {x['id']: x for x in json.loads(lock.read_text())} if lock.is_file() else {}
    if previous.is_file():
        rows.update({x['id']: x for x in json.loads(previous.read_text()).get('sources', [])})
    new = root / 'research/multiserver-candidates.json'
    if new.is_file():
        rows.update({x['id']: x for x in json.loads(new.read_text())['candidates']})
    sources = []
    for name in SOURCE_NAMES:
        row = rows.get(name, {})
        result = {'id': name, 'path': 'sources/' + name,
                  'repository': row.get('repository', row.get('url')),
                  'commit': row.get('commit', row.get('sha')),
                  'commit_date': row.get('commit_date'), 'version': row.get('version')}
        if (root / 'sources' / name / '.git').is_dir():
            result['commit'] = subprocess.check_output(['git', '-C', str(root / 'sources' / name),
                                                       'rev-parse', 'HEAD'], text=True).strip()
            result['commit_date'] = subprocess.check_output(['git', '-C', str(root / 'sources' / name),
                                                            'show', '-s', '--format=%cI', 'HEAD'], text=True).strip()
            result['repository'] = subprocess.check_output(['git', '-C', str(root / 'sources' / name),
                                                           'remote', 'get-url', 'origin'], text=True).strip()
        if not result['repository']:
            raise RuntimeError('No source provenance for ' + name)
        result['files_sha256'] = {rel: hashlib.sha256(path.read_bytes()).hexdigest()
                                 for rel, path in files.items() if rel.startswith('sources/' + name + '/')}
        sources.append(result)
    return {'date': '2026-09-26', 'scope': 'Standalone multi-server follow-up, not the whole terminal census',
            'sources': sources,
            'native': [{'path': ZMX, 'version': '0.8.1', 'platform': 'Linux x86_64',
                        'sha256': ZMX_SHA256,
                        'url': 'https://github.com/neurosnap/zmx/releases/download/v0.8.1/' + Path(ZMX).name,
                        'source_release_url': 'https://github.com/neurosnap/zmx/tree/v0.8.1',
                        'license': 'MIT; native/ZMX-LICENSE',
                        'origin': 'Unmodified upstream release executable, not rebuilt from a different master snapshot'}]}


README = '''# Emacs: lavoro su più server — follow-up riproducibile

Leggere `report/MULTISERVER.html` per il confronto, i risultati e i video.
Questo archivio autonomo contiene gli scenari mirati; non richiede il precedente
archivio del censimento. Le prove usano due endpoint SSH reali su loopback che
condividono il medesimo kernel, non due macchine indipendenti.

## Prerequisiti

Riferimento: Debian 13, Linux x86_64, Emacs 30.1, Python 3.13. Vertico e
Marginalia sono inclusi, installati dai sorgenti fissati e sempre abilitati.
Serve almeno Emacs 29.1. Il binario zmx incluso è la release upstream 0.8.1
per Linux x86_64; non serve Rust/Zig o il download di pacchetti Emacs.

```sh
sudo apt-get update
sudo apt-get install emacs-nox openssh-client openssh-server ncurses-bin python3 bash
sudo install -d -m 755 /run/sshd
```

Eseguire i test con il proprio utente, da una directory con un percorso corto
(per esempio `/tmp/emacs-multiserver`), senza spazi. Le porte loopback 22461 e
22462 devono essere libere. Emacs usa PTY e socket locali; ambienti sandbox che
li vietano richiedono l'esecuzione fuori da tali restrizioni.

## Verifica e riproduzione

Nella radice estratta:

```sh
sha256sum -c SHA256SUMS
python3 scripts/prepare-multiserver.py
python3 scripts/lab.py start
python3 scripts/test-multiserver-term-sessions.py
python3 scripts/test-multiserver-multi-run.py
python3 scripts/test-multiserver-clush.py
python3 scripts/lab.py stop
```

Eseguire `python3 scripts/lab.py stop` anche dopo un errore. `prepare` verifica
i prerequisiti senza aprire connessioni, estrae zmx, compila Compat e terminfo,
e controlla il caricamento delle dipendenze. La configurazione personale Emacs
e `~/.ssh` non vengono usate né modificate. Chiavi temporanee e stato rimangono
in `.runtime/`, che è esclusa da questo archivio. Le registrazioni si generano
con sequenze di tasti inviate a Emacs reale; emacsclient legge le asserzioni.
Ripetere uno scenario archivia i risultati precedenti sotto `results/attempts/`.

## Riproduzione dei video e aggiornamento del report

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Aprire `http://127.0.0.1:8000/report/MULTISERVER.html`. Player JavaScript e CSS
sono locali. In alternativa: `asciinema play recordings/multiserver-clush.cast`
(asciinema è facoltativo). Il report esistente descrive la prova originale;
`python3 scripts/build-multiserver.py`, se presente, ricompila l'HTML dal Markdown
con la wheel inclusa. Nuovi risultati richiedono una revisione esplicita del
testo del report. Non serve il catalogo generale.

## Provenienza e licenze

`research/multiserver-bundle-sources.json` fissa revisioni, URL e hash dei sorgenti.
`SHA256SUMS` verifica ogni file distribuito, escluso il manifest stesso.
I progetti terzi conservano copyright e licenze nei rispettivi `sources/<nome>/`:
Emacs, Compat, Vertico, Marginalia, term-sessions, multi-run, window-layout e
gli altri pacchetti Emacs mantengono le proprie licenze; ClusterShell include
`COPYING.LGPLv2.1`, il player `player/LICENSE`, zmx `native/ZMX-LICENSE`.
La wheel Markdown conserva la licenza interna. L'archivio non attribuisce una
nuova licenza unica ai componenti terzi. I quattro nuovi candidati cssh,
telecommand, emacs-ssh-machines e dotfairy-ssh-manager sono inclusi per verifica
del codice; non sono presentati come scenari SSH eseguiti.

Il pacchetto può essere ricreato con:

```sh
python3 scripts/package-multiserver.py --output /tmp/nuovo-followup.tar.gz
```

Il comando rifiuta la sovrascrittura.
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path, default=Path('/home/admin') / (STEM + '.tar.gz'))
    args = parser.parse_args()
    root, output = args.root.resolve(), args.output.resolve()
    if output.exists():
        raise SystemExit('Refusing to overwrite existing archive: ' + str(output))
    files = collect(root)
    metadata = provenance(root, files)
    source_manifest = root / 'research/multiserver-bundle-sources.json'
    source_manifest.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
    files[str(source_manifest.relative_to(root))] = source_manifest
    generated = {'README-MULTISERVER.md': README.encode(),
                 'native/ZMX-LICENSE': (root / 'sources/zmx-runtime/LICENSE').read_bytes()
                 if (root / 'sources/zmx-runtime/LICENSE').is_file()
                 else (root / 'native/ZMX-LICENSE').read_bytes()}
    payloads = {rel: (path.read_bytes(), 0o755 if path.stat().st_mode & 0o111 else 0o644)
                for rel, path in files.items()}
    payloads.update({name: (data, 0o644) for name, data in generated.items()})
    sums = ''.join(hashlib.sha256(data).hexdigest() + '  ' + name + '\n'
                   for name, (data, mode) in sorted(payloads.items()))
    payloads['SHA256SUMS'] = (sums.encode(), 0o644)
    output.parent.mkdir(parents=True, exist_ok=True)
    # x mode guarantees that concurrent packaging cannot replace an archive.
    with output.open('xb') as raw:
        with gzip.GzipFile(fileobj=raw, mode='wb', filename='', mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode='w', format=tarfile.PAX_FORMAT) as tf:
                for name, (data, mode) in sorted(payloads.items()):
                    info = tarfile.TarInfo(STEM + '/' + name)
                    info.size, info.mode, info.mtime = len(data), mode, 0
                    info.uid = info.gid = 0
                    info.uname = info.gname = ''
                    tf.addfile(info, io.BytesIO(data))
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_name(output.name + '.sha256').write_text(digest + '  ' + output.name + '\n')
    print(json.dumps({'archive': str(output), 'bytes': output.stat().st_size,
                      'files': len(payloads), 'sha256': digest}, indent=2))


if __name__ == '__main__':
    main()
