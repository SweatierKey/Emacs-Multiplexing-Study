# terminal

Categoria: **emulatore-storico**. [Sorgente upstream](https://git.savannah.gnu.org/cgit/emacs). Revisione: `30.1`.

## Funzionamento

terminal.el di GNU Emacs, codice storico dal 1986, marcato obsoleto da Emacs 24.4; parser, filtro di processo e schermo in Lisp, distinto dal successivo term.el.

## Utilizzo umano e limiti

M-x terminal-emulator; prefisso C-^ per i comandi dell'emulatore, C-^ b per cambiare buffer. Tentativo registrato, con esito nella scheda; il supporto remoto dipende anche dalle sue capability terminali generate a runtime.

## Evidenza

- Acquisizione: `builtin`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/terminal.md).
- [Log del caricamento](../../results/load/terminal.log).

### Scenario terminal: passed

[Esito e snapshot](../../results/terminal.json) · [Traccia dei tasti](../../results/terminal-keys.json) · [Registrazione asciinema](../../recordings/terminal.cast) · [Player](../../index.html#terminal)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `terminal-emulator` |
| 3.11 | `RET` |
| 3.91 | `b''` |
| 4.11 | `RET` |
| 5.42 | `lab-ssh lab-web` |
| 5.62 | `RET` |
| 6.62 | `cat status.txt; tail -n 3 service.log` |
| 6.82 | `RET` |
| 7.84 | `export STUDY_KEEP=web-session-alive` |
| 8.04 | `RET` |
| 8.85 | `C-^ b: leave historical emulator` |
| 9.25 | `*scratch*` |
| 9.45 | `RET` |
| 10.26 | `M-x` |
| 10.56 | `terminal-emulator` |
| 11.06 | `RET` |
| 11.86 | `b''` |
| 12.06 | `RET` |
| 13.37 | `lab-ssh lab-db` |
| 13.57 | `RET` |
| 14.57 | `cat status.txt; tail -n 3 service.log` |
| 14.77 | `RET` |
| 15.79 | `C-^ b: leave historical emulator` |
| 16.20 | `*scratch*` |
| 16.40 | `RET` |
| 17.20 | `C-x b: switch-to-buffer` |
| 17.60 | `*terminal*` |
| 18.00 | `RET` |
| 18.41 | `printenv STUDY_KEEP` |
| 18.61 | `RET` |
