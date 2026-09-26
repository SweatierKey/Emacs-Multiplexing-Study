# Riprodurre lo studio

## Materiale

Scaricare `Emacs-Multiplexing-Study-2026-09-26.tar.gz` e il relativo SHA256 dalla [release](https://github.com/SweatierKey/Emacs-Multiplexing-Study/releases/tag/study-2026-09-26). Il repository Git contiene report, strumenti, risultati, player e registrazioni; il bundle della release aggiunge i sorgenti acquisiti, moduli nativi, wheel e pacchetti Debian. Non richiede che gli artifact temporanei di GitHub Actions restino disponibili.

```sh
sha256sum -c Emacs-Multiplexing-Study-2026-09-26.tar.gz.sha256
tar -xzf Emacs-Multiplexing-Study-2026-09-26.tar.gz
cd Emacs-Multiplexing-Study
python3 scripts/verify.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Aprire `http://127.0.0.1:8000/`. Il player è locale; i `.cast` non richiedono account o upload su asciinema.org. Per rivedere da terminale: `asciinema play recordings/vterm.cast`. Il server HTTP serve solo i file del bundle; non avvia le SSH del test.

## Ambiente fissato

Laboratorio originale: Debian GNU/Linux 13, x86_64, Emacs 30.1, Bash, OpenSSH, tmux, libvterm. Versioni effettive: `results/environment-current.json`. Le revisioni di Vertico e Marginalia sono fissate come gli altri sorgenti in `research/source-lock.json`; non vengono installate da un archivio mobile durante le prove.

Il Dockerfile usa il digest Debian registrato in `research/debian-image-digest.json` e i `.deb` archiviati in `vendor/lab-debs.tar.gz` e `vendor/extra-debs/`. Il primo pull della base richiede rete; installazione dei pacchetti e preparazione dei test usano il bundle. I passaggi dpkg ripetuti risolvono pre-dipendenze ordinate nello stesso insieme locale; l'ultimo errore resta bloccante. I tentativi di build e la verifica del contenitore, quando eseguiti, sono in `results/container-*.log`.

```sh
podman build -t emacs-study:2026-09-26 .
podman run --rm emacs-study:2026-09-26
```

Il comando predefinito esegue uno smoke test. Per la suite completa:

```sh
podman run --name emacs-study-run emacs-study:2026-09-26 \
  python3 scripts/run-suite.py
podman cp emacs-study-run:/study/results ./results-replayed
podman cp emacs-study-run:/study/recordings ./recordings-replayed
podman rm emacs-study-run
```

Non sono necessarie porte pubblicate né accesso a server esterni: le due SSH stanno nello stesso contenitore. La suite completa comprende scenari negativi documentati e può terminare con codice non zero. Questo è un esito visibile, non un errore ignorato per rendere verde il report.

## Esecuzione su Debian senza container

Occorrono `emacs`/`emacsclient` con moduli dinamici, Python 3, OpenSSH client/server, `tic`, CMake, GCC, make, libvterm-dev, tmux e less. Non installare indiscriminatamente l'intero archivio Debian su una distribuzione diversa: usare il contenitore per mantenere la base fissata.

```sh
python3 scripts/prepare.py
python3 scripts/run-suite.py --smoke
# oppure tutta la suite dichiarata in config/suite.json
python3 scripts/run-suite.py
```

Per un progetto singolo:

```sh
python3 scripts/lab.py start
python3 scripts/test-scenarios.py ghostel
python3 scripts/lab.py stop
```

I controller hanno `test-controllers.py emamux tmux-view`; eev ha `test-eev.py` con F8 su `lab/eev-demo.e`. I copioni speciali sono `test-special.py tmux-nested tmux-control tab-bar elscreen eyebrowse` e `test-zmx.py`. `tmux-control-mode` ha un copione separato ma un risultato negativo nello snapshot consegnato. Usare un percorso di estrazione corto e senza spazi per restare entro i limiti dei socket Unix e dei file di configurazione SSH.

## Profilo Emacs e differenze dichiarate

`config/init.el` avvia un ambiente `-Q`, crea la directory privata `.runtime`, prepara il load-path e abilita `(vertico-mode 1)` e `(marginalia-mode 1)`. Non legge l'init dell'utente. Le variabili di shell puntano a `lab/bash`, che disabilita file di startup personali. Le opzioni specifiche, i `require` aggiuntivi e gli hook sono in `scripts/scenarios.py`. Il profilo popterm usa finestre invece di posframe perché la prova è TTY.

La preparazione compila compat e il modulo vterm e installa le terminfo dentro `.runtime/terminfo`. Ghostel, Kuro, Cooked e Alacritty usano moduli nativi inclusi per Linux x86_64, con provenienza e hash in `research/native-manifest.json`. Non sono binari universali per ogni ABI/piattaforma. Le build originali di Cooked/Alacritty sono documentate nei workflow e nei log; le altre release native sono identificate nei JSON di acquisizione. Una replica di esecuzione con binari fissati non è una promessa di build bit-identica di tutto Rust/Zig.

## Come sono registrati e verificati i tasti

`scripts/record.py` crea una PTY 110×32, esegue Emacs reale e registra gli eventi asciicast v2. Input e output vengono salvati con timestamp; `emacsclient` legge stato/snapshot e termina Emacs, ma non genera comandi shell né testo dimostrativo. I file `*-keys.json` contengono etichetta e byte esadecimali di ogni input.

Le asserzioni controllano output effettivo con righe ancorate (`role=web`, `role=db`, log WARN e variabile conservata), non la sola presenza del comando digitato. I profili standard richiedono due buffer distinti. Le prove di persistenza richiedono una nuova istanza Emacs e recupero dello stato. Alcuni profili shell non eseguono il pager: la scheda non lo rivendica.

Le registrazioni contengono tempi d'attesa reali; il player limita le pause di inattività per facilitarne la visione. Restano catture del terminale, non MP4 sintetici. Il motore del player è incluso localmente.

## Aggiornare e ricostruire il dossier

```sh
python3 scripts/index-sources.py
python3 scripts/probe.py
python3 scripts/build-report.py
python3 scripts/verify.py
python3 scripts/package.py
```

`probe.py` avvia un Emacs batch distinto per voce e distingue `loaded`, `error`, `wrong-library` e timeout. Non sostituisce la demo. `source-lock.json` fissa le revisioni; gli script di acquisizione iniziali che seguono HEAD sono strumenti di scoperta, non il percorso consigliato per replicare questo snapshot.

`.runtime` contiene chiavi effimere, socket, cache e processi del laboratorio; è esclusa da Git e dal pacchetto distribuito. Lo script di arresto termina solo i PID memorizzati per le due SSH del laboratorio. Usare un contenitore o una copia separata per più suite simultanee: le porte sono fisse e i nomi delle sessioni non sono pensati per due esecuzioni concorrenti dello stesso scenario.
