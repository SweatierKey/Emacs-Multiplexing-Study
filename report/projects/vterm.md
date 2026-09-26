# vterm

Categoria: **emulatore**. [Sorgente upstream](https://github.com/akermu/emacs-libvterm). Revisione: `6d715a93fa0e5182bc137d4db09f376e06938aa5`.

## Funzionamento

Modulo C interfaccia libvterm; il filtro di processo alimenta parser e aggiornamenti del buffer.

## Utilizzo umano e limiti

M-x vterm e C-u M-x vterm; C-x b per tornare. La libreria nativa deve corrispondere all'ABI di Emacs. Nel test compilata localmente.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/vterm.md).
- [Log del caricamento](../../results/load/vterm.log).

### Scenario vterm: passed

[Esito e snapshot](../../results/vterm.json) · [Traccia dei tasti](../../results/vterm-keys.json) · [Registrazione asciinema](../../recordings/vterm.cast) · [Player](../../index.html#vterm)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `vterm` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.02 | `RET` |
| 7.82 | `C-u` |
| 8.22 | `M-x` |
| 8.52 | `vterm` |
| 9.02 | `RET` |
| 10.32 | `lab-ssh lab-db` |
| 10.52 | `RET` |
| 11.52 | `cat status.txt; tail -n 3 service.log` |
| 11.72 | `RET` |
| 12.72 | `C-x b: switch-to-buffer` |
| 13.12 | `*vterm*` |
| 13.53 | `RET` |
| 13.93 | `printenv STUDY_KEEP` |
| 14.13 | `RET` |
| 14.83 | `less service.log` |
| 15.03 | `RET` |
| 15.73 | `q: leave less` |
| 16.23 | `printf 'PAGER_%s\n' RETURNED` |
| 16.43 | `RET` |

### Scenario tmux-nested: passed

[Esito e snapshot](../../results/tmux-nested.json) · [Traccia dei tasti](../../results/tmux-nested-keys.json) · [Registrazione asciinema](../../recordings/tmux-nested.cast) · [Player](../../index.html#vterm)

- `ssh_web`: `True`
- `ssh_db`: `True`
- `return_preserves_shell`: `True`
- `survives_emacs_exit`: `True`
- `restart_reconnect`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.32 | `M-x` |
| 2.62 | `vterm` |
| 3.12 | `RET` |
| 3.92 | `tmux -L ems-tmux-nested -f /dev/null new-session -s ops` |
| 4.12 | `RET` |
| 5.12 | `lab-ssh lab-web` |
| 5.32 | `RET` |
| 6.32 | `cat status.txt; tail -n 3 service.log` |
| 6.52 | `RET` |
| 7.53 | `export STUDY_KEEP=web-session-alive` |
| 7.73 | `RET` |
| 8.53 | `C-b c: tmux new-window` |
| 9.53 | `lab-ssh lab-db` |
| 9.73 | `RET` |
| 10.73 | `cat status.txt; tail -n 3 service.log` |
| 10.93 | `RET` |
| 11.93 | `C-b p: tmux previous-window` |
| 12.93 | `printenv STUDY_KEEP` |
| 13.13 | `RET` |

[Registrazione della riconnessione](../../recordings/tmux-nested-resume.cast).
