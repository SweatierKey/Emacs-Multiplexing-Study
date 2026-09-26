# project-terminal

Categoria: **gestore**. [Sorgente upstream](https://github.com/cowboyd/project-terminal.el). Revisione: `79a4cb4fe4bd30c4088f634a108ef24b54769943`.

## Funzionamento

Terminali per progetto, side window e tab-line; default Eshell.

## Utilizzo umano e limiti

M-x project-terminal-add; non viene presentato come un nuovo motore VT. Test lineare su due SSH.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/project-terminal.md).
- [Log del caricamento](../../results/load/project-terminal.log).

### Scenario project-terminal: passed

[Esito e snapshot](../../results/project-terminal.json) · [Traccia dei tasti](../../results/project-terminal-keys.json) · [Registrazione asciinema](../../recordings/project-terminal.cast) · [Player](../../index.html#project-terminal)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `project-terminal-add` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `project-terminal-add` |
| 8.62 | `RET` |
| 9.92 | `lab-ssh lab-db` |
| 10.12 | `RET` |
| 11.12 | `cat status.txt; tail -n 3 service.log` |
| 11.32 | `RET` |
| 12.32 | `C-x b: switch-to-buffer` |
| 12.72 | `*project-terminal: /home/admin/Emacs-Multiplexing-Study/*` |
| 13.12 | `RET` |
| 13.53 | `printenv STUDY_KEEP` |
| 13.73 | `RET` |
