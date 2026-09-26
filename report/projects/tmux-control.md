# tmux-control

Categoria: **persistenza**. [Sorgente upstream](https://github.com/csheaff/tmux-control). Revisione: `ebe07f4caff0c1be21e1c92323de6d00744c2891`.

## Funzionamento

csheaff: protocollo tmux control-mode, processo a pipe ed emulazione delle pane con Eat.

## Utilizzo umano e limiti

M-x tmux-control-connect, host vuoto per locale, socket dedicato e sessione ops; tmux-control-new-window e C-c C-p. Verificata riconnessione dopo kill-emacs.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/tmux-control.md).
- [Log del caricamento](../../results/load/tmux-control.log).

### Scenario tmux-control: passed

[Esito e snapshot](../../results/tmux-control.json) · [Traccia dei tasti](../../results/tmux-control-keys.json) · [Registrazione asciinema](../../recordings/tmux-control.cast) · [Player](../../index.html#tmux-control)

- `ssh_web`: `True`
- `ssh_db`: `True`
- `return_preserves_shell`: `True`
- `survives_emacs_exit`: `True`
- `restart_reconnect`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `tmux-control-connect` |
| 3.41 | `RET` |
| 4.21 | `b''` |
| 4.41 | `RET` |
| 5.21 | `ems-tmux-control` |
| 5.41 | `RET` |
| 6.21 | `ops` |
| 6.41 | `RET` |
| 7.91 | `lab-ssh lab-web` |
| 8.11 | `RET` |
| 9.11 | `cat status.txt; tail -n 3 service.log` |
| 9.31 | `RET` |
| 10.32 | `export STUDY_KEEP=web-session-alive` |
| 10.52 | `RET` |
| 11.32 | `M-x` |
| 11.62 | `tmux-control-new-window` |
| 12.12 | `RET` |
| 12.92 | `db` |
| 13.12 | `RET` |
| 14.12 | `lab-ssh lab-db` |
| 14.32 | `RET` |
| 15.32 | `cat status.txt; tail -n 3 service.log` |
| 15.52 | `RET` |
| 16.52 | `C-c C-p: previous-window` |
| 17.52 | `printenv STUDY_KEEP` |
| 17.72 | `RET` |

[Registrazione della riconnessione](../../recordings/tmux-control-resume.cast).
