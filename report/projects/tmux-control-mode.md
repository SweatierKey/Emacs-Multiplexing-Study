# tmux-control-mode

Categoria: **persistenza**. [Sorgente upstream](https://github.com/stephenjayakar/emacs-tmux-control-mode). Revisione: `d2a93a336f7d6a4a770cb9e740d5e6cfb602843b`.

## Funzionamento

stephenjayakar: feature tmux-cc, manager di sessioni e renderer vterm per le pane, protocollo -CC.

## Utilizzo umano e limiti

Avvio e due SSH riusciti; selezione della finestra tmux non ha riportato il focus Emacs alla pane attesa nel copione. Scenario completo negativo; non attribuire persistenza verificata a questo risultato.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/tmux-control-mode.md).
- [Log del caricamento](../../results/load/tmux-control-mode.log).

### Scenario tmux-control-mode: failed

[Esito e snapshot](../../results/tmux-control-mode.json) · [Traccia dei tasti](../../results/tmux-control-mode-keys.json) · [Registrazione asciinema](../../recordings/tmux-control-mode.cast) · [Player](../../index.html#tmux-control-mode)

- `ssh_web`: `True`
- `ssh_db`: `True`

Errore finale: asserzione non soddisfatta; leggere traceback e snapshot

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.32 | `M-x` |
| 2.62 | `tmux-cc-start` |
| 3.12 | `RET` |
| 3.92 | `C-a C-k` |
| 4.32 | `tmux -L ems-tmux-control-mode -f /dev/null -CC new-session -A -s ops` |
| 4.52 | `RET` |
| 6.02 | `M-< C-s %0 RET RET: visit first pane` |
| 7.03 | `lab-ssh lab-web` |
| 7.23 | `RET` |
| 8.23 | `cat status.txt; tail -n 3 service.log` |
| 8.43 | `RET` |
| 9.43 | `export STUDY_KEEP=web-session-alive` |
| 9.63 | `RET` |
| 10.43 | `C-t c: tmux-cc new-window` |
| 11.43 | `db` |
| 11.63 | `RET` |
| 12.63 | `lab-ssh lab-db` |
| 12.83 | `RET` |
| 13.83 | `cat status.txt; tail -n 3 service.log` |
| 14.03 | `RET` |
| 15.05 | `M-x` |
| 15.35 | `tmux-cc-switch-window` |
| 15.85 | `RET` |
| 16.65 | `ops:ssh` |
| 16.85 | `RET` |
| 17.85 | `C-x b: select rendered pane` |
| 18.25 | `tmux-pane %0` |
| 18.45 | `RET` |
| 19.45 | `printenv STUDY_KEEP` |
| 19.65 | `RET` |
