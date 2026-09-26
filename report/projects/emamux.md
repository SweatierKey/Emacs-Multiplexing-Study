# emamux

Categoria: **controller**. [Sorgente upstream](https://github.com/emacsorphanage/emamux). Revisione: `93bb7e8b8cfb0ced5b9b38044a031d40342201a1`.

## Funzionamento

Invia testo/comandi a tmux con process-file, selezione pane e runner.

## Utilizzo umano e limiti

Nel test M-x emamux:send-command seleziona la finestra web/db di un tmux isolato e invia la richiesta di stato; vterm mostra poi l’output reale. Il controller da solo non rende lo schermo nel buffer.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/emamux.md).
- [Log del caricamento](../../results/load/emamux.log).

### Scenario emamux: passed

[Esito e snapshot](../../results/emamux.json) · [Traccia dei tasti](../../results/emamux-keys.json) · [Registrazione asciinema](../../recordings/emamux.cast) · [Player](../../index.html#emamux)

- `completion_enabled`: `True`
- `remote_web_command_executed`: `True`
- `remote_db_command_executed`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 3.15 | `M-x` |
| 3.45 | `emamux:send-command` |
| 3.95 | `RET` |
| 4.75 | `0: web` |
| 4.96 | `RET` |
| 5.75 | `C-a C-k: clear previous command` |
| 6.16 | `cat status.txt; tail -n 3 service.log` |
| 6.36 | `RET` |
| 7.36 | `M-x` |
| 7.66 | `vterm` |
| 8.16 | `RET` |
| 8.96 | `tmux attach -t ops:0` |
| 9.16 | `RET` |
| 10.16 | `C-b d: detach tmux to return to controller` |
| 10.96 | `C-u` |
| 11.37 | `M-x` |
| 11.66 | `emamux:send-command` |
| 12.16 | `RET` |
| 12.96 | `1: db` |
| 13.17 | `RET` |
| 13.97 | `C-a C-k: clear previous command` |
| 14.37 | `cat status.txt; tail -n 3 service.log` |
| 14.57 | `RET` |
| 15.57 | `C-u` |
| 15.97 | `M-x` |
| 16.27 | `vterm` |
| 16.77 | `RET` |
| 17.57 | `tmux attach -t ops:1` |
| 17.77 | `RET` |
| 18.77 | `C-b d: detach tmux to return to controller` |
