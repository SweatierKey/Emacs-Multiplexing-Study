# term

Categoria: **emulatore**. [Sorgente upstream](https://git.savannah.gnu.org/cgit/emacs). Revisione: `30.1`.

## Funzionamento

Parser e schermo in Lisp, processo PTY gestito da term.el. ansi-term è un secondo comando dello stesso motore, non un altro progetto.

## Utilizzo umano e limiti

M-x ansi-term, accettare la shell; C-c C-j passa alla modifica Emacs e C-c C-k ritorna al processo. C-x b sceglie un'altra sessione. I processi appartengono a Emacs.

## Evidenza

- Acquisizione: `builtin`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term.md).
- [Log del caricamento](../../results/load/term.log).

### Scenario term: passed

[Esito e snapshot](../../results/term.json) · [Traccia dei tasti](../../results/term-keys.json) · [Registrazione asciinema](../../recordings/term.cast) · [Player](../../index.html#term)

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
| 2.61 | `term` |
| 3.11 | `RET` |
| 3.91 | `b''` |
| 4.11 | `RET` |
| 5.41 | `lab-ssh lab-web` |
| 5.61 | `RET` |
| 6.61 | `cat status.txt; tail -n 3 service.log` |
| 6.81 | `RET` |
| 7.81 | `export STUDY_KEEP=web-session-alive` |
| 8.01 | `RET` |
| 8.82 | `C-c C-j: term line mode` |
| 9.22 | `M-x` |
| 9.52 | `ansi-term` |
| 10.02 | `RET` |
| 10.82 | `b''` |
| 11.02 | `RET` |
| 12.32 | `lab-ssh lab-db` |
| 12.52 | `RET` |
| 13.52 | `cat status.txt; tail -n 3 service.log` |
| 13.72 | `RET` |
| 14.72 | `C-c C-j: term line mode` |
| 15.12 | `C-x b: switch-to-buffer` |
| 15.53 | `*terminal*` |
| 15.93 | `RET` |
| 16.33 | `C-c C-k: term char mode` |
| 16.73 | `printenv STUDY_KEEP` |
| 16.93 | `RET` |
| 17.63 | `less service.log` |
| 17.83 | `RET` |
| 18.53 | `q: leave less` |
| 19.03 | `printf 'PAGER_%s\n' RETURNED` |
| 19.23 | `RET` |

### Scenario ansi-term: passed

[Esito e snapshot](../../results/ansi-term.json) · [Traccia dei tasti](../../results/ansi-term-keys.json) · [Registrazione asciinema](../../recordings/ansi-term.cast) · [Player](../../index.html#term)

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
| 2.61 | `ansi-term` |
| 3.11 | `RET` |
| 3.91 | `b''` |
| 4.11 | `RET` |
| 5.41 | `lab-ssh lab-web` |
| 5.61 | `RET` |
| 6.61 | `cat status.txt; tail -n 3 service.log` |
| 6.81 | `RET` |
| 7.81 | `export STUDY_KEEP=web-session-alive` |
| 8.02 | `RET` |
| 8.82 | `C-c C-j: term line mode` |
| 9.22 | `M-x` |
| 9.52 | `ansi-term` |
| 10.02 | `RET` |
| 10.82 | `b''` |
| 11.02 | `RET` |
| 12.32 | `lab-ssh lab-db` |
| 12.52 | `RET` |
| 13.52 | `cat status.txt; tail -n 3 service.log` |
| 13.72 | `RET` |
| 14.72 | `C-c C-j: term line mode` |
| 15.12 | `C-x b: switch-to-buffer` |
| 15.52 | `*ansi-term*` |
| 15.92 | `RET` |
| 16.33 | `C-c C-k: term char mode` |
| 16.73 | `printenv STUDY_KEEP` |
| 16.93 | `RET` |
| 17.63 | `less service.log` |
| 17.83 | `RET` |
| 18.53 | `q: leave less` |
| 19.03 | `printf 'PAGER_%s\n' RETURNED` |
| 19.23 | `RET` |
