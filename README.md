# Emacs Multiplexing Study

Studio di terminali e multiplexer per Emacs, con sorgenti fissati, analisi del codice, workflow da amministratore di sistema e registrazioni reali. Vertico e Marginalia sono abilitati nei test; i comandi e i binding dei pacchetti sono documentati senza rimappature globali inventate.

- **[Report e video navigabili](https://sweatierkey.github.io/Emacs-Multiplexing-Study/)**
- **[Archivio completo tar.gz e SHA256](https://github.com/SweatierKey/Emacs-Multiplexing-Study/releases/tag/study-2026-09-26)**
- [Report in Markdown](report/REPORT.md) · [Catalogo](report/CATALOGUE.md)
- [Riproduzione](report/REPRODUCE.md) · [Ricerca e provenienza](report/SEARCH.md) · [Validazione](report/VALIDATION.md)

Snapshot del 26 settembre 2026: **145 voci nel catalogo**, incluse dipendenze applicative, fork, estensioni, progetti adiacenti e candidati irrisolti; **66 scenari, 59 riusciti e 7 non conclusi**. Sono disponibili 71 cast originali, oltre alle repliche nel contenitore e ai tentativi diagnostici. I conteggi strutturati sono in [summary.json](report/summary.json).

**Non è un censimento dimostrabilmente esaustivo di tutti i progetti mai esistiti. Non tutte le voci hanno una demo end-to-end.** Ogni scheda distingue codice analizzato, caricamento, prova effettiva e limiti. `passed` vale per il singolo scenario descritto, non per ogni funzionalità del progetto.

Il laboratorio usa due endpoint SSH reali su loopback, web e db, sullo stesso kernel. Verifica cambio sessione, stato della shell e, dove previsto, pager e riattacco dopo chiusura di Emacs. Non contatta server dell'utente.

## Avvio dal bundle completo

```sh
tar -xzf Emacs-Multiplexing-Study-2026-09-26.tar.gz
cd Emacs-Multiplexing-Study
python3 scripts/verify.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Aprire `http://127.0.0.1:8000/`. Per replicare i test in ambiente pulito:

```sh
podman build -t emacs-study:2026-09-26 .
podman run --rm emacs-study:2026-09-26
```

Il repository contiene report, codice del laboratorio, player, risultati e cast. La release aggiunge sorgenti, moduli nativi, wheel e pacchetti Debian; non occorre recuperare artifact Actions scaduti. Consultare [THIRD_PARTY.md](THIRD_PARTY.md) per provenienza e licenze.
