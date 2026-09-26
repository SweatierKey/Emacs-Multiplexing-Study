# shell

Categoria: **baseline**. [Sorgente upstream](https://git.savannah.gnu.org/cgit/emacs). Revisione: `30.1`.

## Funzionamento

comint con processo shell, editing delle righe e riconoscimento del prompt; non un emulatore VT completo.

## Utilizzo umano e limiti

M-x shell; C-u M-x shell e un nuovo nome per un'altra SSH. Il test non usa less per certificare shell come terminale completo.

## Evidenza

- Acquisizione: `builtin`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/shell.md).
- [Log del caricamento](../../results/load/shell.log).

### Scenario shell: passed

[Esito e snapshot](../../results/shell.json) · [Traccia dei tasti](../../results/shell-keys.json) · [Registrazione asciinema](../../recordings/shell.cast) · [Player](../../index.html#shell)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `shell` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-u` |
| 8.22 | `M-x` |
| 8.52 | `shell` |
| 9.02 | `RET` |
| 9.82 | `C-a C-k` |
| 10.22 | `*shell-db*` |
| 10.42 | `RET` |
| 11.72 | `lab-ssh lab-db` |
| 11.92 | `RET` |
| 12.92 | `cat status.txt; tail -n 3 service.log` |
| 13.12 | `RET` |
| 14.13 | `C-x b: switch-to-buffer` |
| 14.53 | `*shell*` |
| 14.93 | `RET` |
| 15.33 | `printenv STUDY_KEEP` |
| 15.53 | `RET` |
