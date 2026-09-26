# Lavorare su più server da Emacs

Approfondimento del 26 settembre 2026. Obiettivo: eseguire comandi, check, script e programmi su uno o più host, scelti da una lista, in parallelo oppure in serie, con output separati o riuniti. Sono preferite funzioni previste dal progetto, accessibili senza costruire un orchestratore in Lisp.

## Scelta consigliata

**Nessuno dei progetti Emacs verificati soddisfa tutti questi requisiti nativamente.** Il risultato cambia a seconda del lavoro prevalente:

- **Check e script su gruppi di server: ClusterShell / `clush`, eseguito in `M-x shell`.** È il candidato provato che unisce inventario, parallelismo limitabile, esecuzione seriale con attesa, raccolta output, timeout ed esiti. Il limite è concreto: l'output per host viene scritto in file; aprirli con `C-x C-f` crea buffer separati, ma non terminali remoti interattivi né una UI Emacs che li gestisce automaticamente.
- **Sessioni interattive persistenti e buffer separati: `term-sessions`.** La sua lista permette di marcare sessioni e inviare un comando anche a terminali nascosti. È il flusso Emacs più convincente fra quelli provati per questo lavoro. Mancano però l'importazione di un inventario host, una campagna seriale con attesa e l'output aggregato.
- **Un solo pacchetto Emacs, tutti i requisiti obbligatori: nessun vincitore verificato.** Accoppiare i due strumenti copre attività complementari, ma resta una scelta di due strumenti. Non viene presentata come soluzione già integrata.

`clush` è un'applicazione esterna con interfaccia a riga di comando: usare Emacs come terminale non la trasforma in un pacchetto Emacs. Viceversa, una shell che replica l'input non diventa automaticamente un gestore di job distribuiti.

## Criteri che hanno cambiato la selezione

1. **Serie** significa che il comando su B inizia dopo la conclusione su A. Un ritardo fisso fra invii non basta.
2. **Output aggregato** contiene i risultati degli host, identificabili. Il buffer che riceve il comando da distribuire non conta se non riceve anche i risultati.
3. **Lista host** è distinta dalla lista di sessioni già aperte. Importare un inventario e creare le connessioni è lavoro aggiuntivo se il progetto non lo prevede.
4. **Buffer separati vivi** è distinto da file di log separati o pannelli interni a una TUI. Sono utili, ma hanno comportamenti diversi.
5. **Semplicità** viene valutata attraverso il flusso documentato e i tasti reali, senza punteggi arbitrari. I test non aggiungono al prodotto selezione host, sincronizzazione o collector mancanti.

## Confronto delle capacità native

“No” significa nessun flusso corrispondente trovato nello snapshot analizzato; non è una dimostrazione su tutte le versioni o possibili estensioni.

| Progetto | Da una lista | Parallelo | Serie con attesa fra host | Output separati / unico | Costo umano e limite |
|---|---|---|---|---|---|
| **clush** | File host, espressioni, gruppi | Sì, limite `-f N` | **Sì, `-f 1` in modalità flat** | File per host / unico etichettato o raccolto | Comandi CLI brevi; nessun gestore nativo di buffer Emacs per host |
| **term-sessions** | Sessioni già create, marcatura | Sì, invio alla selezione | No nel flusso della lista | Terminali e history separate / no | `M-x term-sessions-list`, `m` o `T`, `s`; richiede zmx |
| **multi-run** | Lista Lisp di host, subset per indici | Sì | **No, ritardi fissi** | Eshell separati / no | Configurazione e comandi nel master Eshell; molte funzioni non sono comandi `M-x` |
| **cssh** | File DSH, gruppi, regexp, IBuffer | Sì | No | Terminali separati / no | Molto pertinente all'inventario; controller di input senza raccolta esiti |
| **dotfairy-ssh-manager** | Gruppo di terminali aperti | Sì, riga/regione/buffer | No | Terminali separati / no | Invio di script comodo, gruppo costruito aggiungendo le sessioni |
| **Ghostel Mux** | Pannelli della finestra attiva | Sì, pannelli vivi e visibili | No | Terminali separati / no | SYNC immediato; i terminali nascosti non ricevono input |
| **tmux-control** (csheaff) | Connessioni/sessioni tmux | Nessun batch Emacs trovato | No | Buffer di terminale / no | Buono per sessioni persistenti, non per orchestrare una lista di host |
| **nssh** | Un hostname DNS risolto in più IP | Sì | No | Shell separate / no | Cluster DNS, non inventario arbitrario; controller senza output remoto |
| **telecommand** | Comandi nominati per host | Una riga per invocazione | Nessun orchestratore host | Riusa un buffer / nessun collector multihost | Menu semplice; colonna “Marked” senza esecuzione collettiva implementata |
| **emacs-ssh-machines** | Inventario e import/export | Connessioni individuali | No | Terminali separati / no | Semplifica raggiungere una macchina; non coordina i comandi |

`project-shells`, `eev/eepitch` ed `emamux` rimangono utili per raggiungere shell, eseguire runbook e controllare tmux. Nei sorgenti analizzati non offrono la combinazione inventario + scheduler + collector richiesta. Il precedente studio documenta separatamente le loro prove.

Un'ulteriore alternativa esterna è [bssh](https://github.com/lablup/bssh): lista host, parallelismo, output in streaming, file per host e una TUI di consultazione. È stato esaminato nella documentazione, **non eseguito in questa prova**. Le sue viste rimangono dentro un buffer terminale Emacs; non risolvono il requisito dei buffer Emacs distinti. Non lo classifico sopra un candidato testato sulla sola base del README.

## Uso concreto: check e script con clush

Con ClusterShell installato e accesso SSH già configurato, il file `hosts.txt` contiene un host o alias SSH per riga. Non serve scrivere un programma di coordinamento. In Emacs: `M-x shell`, quindi, per esempio:

```sh
# Un solo host
clush -n -S -w web01 'uptime'

# Stesso check sull'inventario, al massimo 8 host contemporaneamente
clush -n -S --worker ssh --hostfile hosts.txt -f 8 'systemctl is-active nginx'

# Uno per volta, aspettando il termine di ciascun comando
clush -n -S --worker ssh --hostfile hosts.txt -f 1 'hostname; uptime'

# Invia il contenuto dello script a tutti gli host; raccoglie gli output
clush -S --worker ssh --hostfile hosts.txt -b sh -s < check.sh

# Salva anche stdout e stderr separati per host
clush -n -S --worker ssh --hostfile hosts.txt \
  --outdir results/stdout --errdir results/stderr 'uptime'
```

La scelta `--worker ssh` mantiene esplicita l'esecuzione diretta, flat. `-S` fa propagare il massimo codice d'uscita dei comandi: per default clush può terminare con successo anche quando un comando remoto fallisce. `-n` disabilita l'inoltro di stdin; va omesso quando si invia uno script tramite stdin. Un output comune si consulta nel buffer `*shell*`; un file per host si apre con `C-x C-f`, poi si cambia buffer con `C-x b`.

Limiti da considerare nella scelta:

- `-f 1` garantisce al massimo un comando attivo nel worker diretto; **non promette l'ordine letterale delle righe del file**. Il parser costruisce un NodeSet e l'engine mantiene i client in un set. L'ordine osservato in una prova non è un contratto.
- La serializzazione non implica fermarsi automaticamente al primo errore né rollback. Queste politiche non sono state attribuite al comando.
- Ogni esecuzione apre un comando SSH: lo stato di una shell precedente non viene mantenuto come in un terminale persistente. Programmi interattivi che richiedono un terminale completo richiedono un altro flusso.
- I file per host si aprono manualmente. Il test non implementa aggiornamento live, creazione automatica dei buffer o un selettore Emacs di risultati.

Funzioni e opzioni sono descritte nel [manuale clush](https://github.com/clustershell/clustershell/blob/f3f5b1594be3350b0c29bcc6786cff86abba19d7/doc/txt/clush.txt). Codice verificato: [parsing hostfile](https://github.com/clustershell/clustershell/blob/f3f5b1594be3350b0c29bcc6786cff86abba19d7/lib/ClusterShell/CLI/Clush.py#L924), [file per host](https://github.com/clustershell/clustershell/blob/f3f5b1594be3350b0c29bcc6786cff86abba19d7/lib/ClusterShell/CLI/Clush.py#L177), [limite di concorrenza](https://github.com/clustershell/clustershell/blob/f3f5b1594be3350b0c29bcc6786cff86abba19d7/lib/ClusterShell/Engine/Engine.py#L439), [exit status](https://github.com/clustershell/clustershell/blob/f3f5b1594be3350b0c29bcc6786cff86abba19d7/lib/ClusterShell/CLI/Clush.py#L1197).

## Uso concreto: terminali con term-sessions

Nel test ciascuna sessione zmx locale contiene una connessione SSH. Si apre con `M-x term-sessions-open`, si assegna un nome e si esegue `ssh HOST`. La topologia è semplice da usare senza installare zmx sui server. Il diverso backend TRAMP remoto esiste, ma richiede zmx anche dove gira quel backend e non è stato verificato da questa prova.

Con il frontend predefinito `term`, `C-c C-j` torna alla modalità in cui usare i comandi Emacs. Il flusso operativo è:

1. `M-x term-sessions-list` mostra le sessioni.
2. `m` marca una riga; `T` marca tutte; `U` rimuove tutte le marcature. È disponibile anche `%` per regexp.
3. `s`, comando, `RET` invia il comando alle sessioni selezionate.
4. `RET` apre una sessione; `C-x b` passa tra i buffer. `h` apre history separate, senza aggregarle.

La prova nasconde entrambi i terminali prima dell'invio: non occorre tenerli tutti a schermo. Non si deve però scambiare il ritorno dell'operazione di invio per la conclusione del comando remoto. Le API `run` e `wait` del backend operano su una sessione; la lista non le trasforma in un batch seriale con esiti per host.

Codice verificato: [keymap della lista](https://github.com/ArthurHeymans/emacs-term-sessions/blob/29084b6a8a73b612f60a73ef798303384bd44215/term-sessions-list.el#L72), [dispatch alla selezione](https://github.com/ArthurHeymans/emacs-term-sessions/blob/29084b6a8a73b612f60a73ef798303384bd44215/term-sessions-list.el#L825), [send/run/wait](https://github.com/ArthurHeymans/emacs-term-sessions/blob/29084b6a8a73b612f60a73ef798303384bd44215/term-sessions-zmx.el#L428).

## Perché multi-run non vince

È nato proprio per lavorare su nodi remoti e merita attenzione. Il suo flusso documentato parte da `M-x eshell`:

```elisp
(setq multi-run-hostnames-list '("web01" "db01"))
```

Poi nel master Eshell:

```text
multi-run-configure-terminals 2
multi-run-ssh
multi-run "uptime"
```

La lista è reale e ciascun host conserva il proprio output. Però `multi-run-with-delay` usa timer; non aspetta l'exit status. Con ritardo 0,2 secondi e comandi di 2 secondi abbiamo misurato **1,802 secondi di sovrapposizione**. Quindi non è esecuzione seriale. Non abbiamo trovato un comando nativo che riunisca i risultati in un buffer.

Il [codice dei timer](https://github.com/sagarjha/multi-run/blob/13d4d923535b5e8482b13ff76185203075fb26a3/multi-run.el#L49) e la [documentazione dell'autore](https://sagarjha.github.io/multi-run/#loops) spiegano il limite. La vecchia documentazione include backend assenti dallo snapshot master analizzato: la prova corrente usa Eshell, come previsto da quel codice.

## Prove eseguite e video

Le registrazioni catturano una vera PTY di Emacs; i comandi sono digitati con i binding normali. Emacsclient legge gli snapshot e verifica le condizioni, senza produrre risultati simulati. **Vertico e Marginalia erano attivi in tutte e tre le prove.**

| Prova | Evidenza osservata | Cosa non dimostra |
|---|---|---|
| clush | Un host; lista di due host; intervalli sovrapposti con `-f 2`; nessuna sovrapposizione con `-f 1`; script via stdin; output unico; file stdout/stderr per host; errore 7 propagato; timeout; uso dentro Emacs | Buffer interattivi per host, ordine dell'inventario, programmi TUI, persistenza |
| term-sessions | `m` + `s` raggiunge solo la sessione marcata; `T` + `s` raggiunge entrambi i terminali nascosti; sovrapposizione 1,990 s; due buffer distinti | Inventario host, serializzazione, raccolta output, backend remoto TRAMP |
| multi-run | Lista host; due SSH; broadcast e ritardo misurati; output separati; ritardo 0,2 s produce sovrapposizione 1,802 s | Nessuna prova positiva di serializzazione o aggregazione |

I due server sono endpoint SSH reali su loopback, ruoli `web` e `db`, **sullo stesso kernel e con lo stesso orologio**. Questo rende confrontabili i timestamp; non misura latenza WAN, scalabilità o differenze tra sistemi remoti. Il banner della fixture cambia per host: la prova clush di `-b` verifica due gruppi etichettati nello stesso output, non la deduplicazione di output identici.

`passed` significa che le asserzioni dello scenario sono riuscite. Per multi-run comprende la conferma di una limitazione, non il superamento di tutti i requisiti.

<!-- MULTISERVER_VIDEOS -->

- **Clush**: [video asciinema](../recordings/multiserver-clush.cast), [risultati](../results/multiserver-clush.json), [tasti](../results/multiserver-clush-keys.json), [script](../scripts/test-multiserver-clush.py).
- **Term-sessions**: [video asciinema](../recordings/multiserver-term-sessions.cast), [risultati](../results/multiserver-term-sessions.json), [tasti](../results/multiserver-term-sessions-keys.json), [script](../scripts/test-multiserver-term-sessions.py).
- **Multi-run**: [video asciinema](../recordings/multiserver-multi-run.cast), [risultati](../results/multiserver-multi-run.json), [tasti](../results/multiserver-multi-run-keys.json), [script](../scripts/test-multiserver-multi-run.py).

## Riproduzione e provenienza

È disponibile un [bundle autonomo di questo approfondimento](https://github.com/SweatierKey/Emacs-Multiplexing-Study/releases/tag/multiserver-2026-09-26), con sorgenti, dipendenze selezionate, zmx, configurazione, player e risultati. Non modifica l'archivio dello studio precedente. Il README incluso elenca i prerequisiti e la verifica SHA256.

Nel bundle, dopo i prerequisiti:

```sh
python3 scripts/prepare-multiserver.py
python3 scripts/lab.py start
python3 scripts/test-multiserver-clush.py
python3 scripts/test-multiserver-term-sessions.py
python3 scripts/test-multiserver-multi-run.py
python3 scripts/lab.py stop
python3 -m http.server 8000 --bind 127.0.0.1
```

Aprire `/report/MULTISERVER.html`. Le chiavi SSH generate sono in `.runtime`, escluse dall'archivio e dal repository. Le prove usano solo i due endpoint locali, senza cambiare `~/.ssh/config`.

Snapshot principali: clush `f3f5b1594be3350b0c29bcc6786cff86abba19d7` (versione dichiarata 1.10.1); term-sessions `29084b6a8a73b612f60a73ef798303384bd44215`; multi-run `13d4d923535b5e8482b13ff76185203075fb26a3`; zmx 0.8.1. Gli snapshot dei nuovi candidati e i riferimenti di codice sono in [multiserver-candidates.json](../research/multiserver-candidates.json); quelli inclusi nel bundle sono in [multiserver-bundle-sources.json](../research/multiserver-bundle-sources.json).

Le quattro aggiunte native sono state esaminate nel sorgente, **senza prova SSH runtime**: [cssh](https://github.com/dimitri/cssh/blob/2fe2754235225a59b63f08b130cfd4352e2e1c3f/cssh.el), [telecommand](https://github.com/abrochard/telecommand/blob/fe6620e70a7da2a5cc502eabb3eab9ae046a39cc/telecommand.el), [emacs-ssh-machines](https://github.com/charmitro/emacs-ssh-machines), [dotfairy-ssh-manager](https://github.com/b40yd/dotfairy-ssh-manager). La ricerca aggiuntiva ha cercato progetti orientati all'esecuzione remota, oltre ai multiplexer del catalogo originale; non pretende di escludere ogni progetto mai pubblicato.
