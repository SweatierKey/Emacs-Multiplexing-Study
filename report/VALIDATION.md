# Verifica della consegna

## Prove originali

I risultati puntuali sono `results/<scenario>.json`, le registrazioni `recordings/<scenario>.cast` e i byte inviati `results/<scenario>-keys.json`. I conteggi sono calcolati da `scripts/build-report.py`, non mantenuti manualmente nelle schede. Gli esiti negativi precedenti sono in `results/attempts/`.

## Replica in ambiente pulito

È stato costruito ed eseguito un contenitore Debian dal digest fissato nel Dockerfile, installando i pacchetti archiviati e compilando vterm. I log delle build precedenti conservano le dipendenze mancanti individuate e corrette: ordine delle pre-dipendenze Debian, make e terminfo di base.

| Replica | Esito | Evidenza |
|---|---|---|
| Smoke pulito: ansi-term, Eat, vterm, multi-vterm, ghostel-mux, tmux annidato con riavvio | 6 scenari riusciti, processo suite exit 0 | `results/container-smoke-fixed.log`, `results/container-replay/smoke/` |
| Motori aggiuntivi: Alacritty, Kuro, Ebb, MisTTY, Coterm | 5 scenari riusciti | `results/container-native.log`, `results/container-replay/native/` |
| Cooked, primo tentativo nel contenitore | Due SSH riuscite; pager fermo per terminfo remota assente; suite exit 1 | `results/container-replay/native/cooked.json` |
| Cooked, terminfo preparata anche per SSH | Scenario completo riuscito, exit 0 | `results/container-cooked-fixed.log`, `results/container-replay/cooked-fixed/` |

Le immagini e i codici di uscita sono registrati in [manifest.json](../results/container-replay/manifest.json). Queste repliche **non vengono sommate** ai risultati originali per gonfiare il conteggio. Il primo smoke fallito sul riattacco usava una directory tmux diversa fra i due client; `env_override` mantiene ora il namespace del server.

La suite completa non è stata ripetuta interamente nel contenitore: sono stati verificati i percorsi principali e i moduli nativi sopra. La suite include deliberatamente test che falliscono sullo snapshot corrente. Il Dockerfile e gli script non ne trasformano gli errori in successi.

## Registrazioni e collegamenti

`scripts/verify.py` valida formato e ordine temporale degli asciicast, riproduce gli eventi tramite pyte, verifica che gli scenari riusciti abbiano registrazioni e modalità di completamento attive, controlla i collegamenti HTML locali e, quando presente, il manifesto SHA256 del bundle. Il risultato è in `results/verification.json`.

È stata ispezionata anche una ricostruzione dello schermo vterm dagli eventi del cast (`report/vterm-replayed.png`). Non è stato eseguito un test di compatibilità visuale del player su tutti i browser. Il player originale asciinema è incluso con licenza; l'HTML non necessita di servizi remoti per riprodurre i cast.

## Limiti della riproducibilità

I tempi degli eventi, PID, directory assolute, identificatori dei buffer e dettagli della redisplay possono differire fra repliche. I dati attesi sono fixture deterministiche e stato della shell, non un confronto pixel per pixel. I moduli precompilati sono Linux x86_64; le build complete di tutti i backend Rust/Zig non sono ripetute nel contenitore. La provenienza dei binari e i sorgenti sono separatamente conservati.
