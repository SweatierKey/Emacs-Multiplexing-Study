# Emacs: lavoro su più server — follow-up riproducibile

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
