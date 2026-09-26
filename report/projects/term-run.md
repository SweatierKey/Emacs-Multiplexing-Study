# term-run

Categoria: **launcher-interno**. [Sorgente upstream](https://github.com/10sr/term-run-el). Revisione: `0fd135d55fcf864598b1fb8dd880833a1a322910`.

## Funzionamento

Avvia un comando arbitrario in term e ne visualizza il buffer con display-buffer.

## Utilizzo umano e limiti

M-x term-run-shell-command; C-x o seleziona la finestra mostrata. C-u crea un altro buffer; senza prefisso può sostituire il processo previo consenso.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term-run.md).
- [Log del caricamento](../../results/load/term-run.log).

### Scenario term-run: passed

[Esito e snapshot](../../results/term-run.json) · [Traccia dei tasti](../../results/term-run-keys.json) · [Registrazione asciinema](../../recordings/term-run.cast) · [Player](../../index.html#term-run)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.32 | `M-x` |
| 2.62 | `term-run-shell-command` |
| 3.12 | `RET` |
| 3.92 | `/bin/bash --noprofile --norc` |
| 4.12 | `RET` |
| 5.42 | `C-x o: select displayed terminal` |
| 5.83 | `lab-ssh lab-web` |
| 6.03 | `RET` |
| 7.03 | `cat status.txt; tail -n 3 service.log` |
| 7.23 | `RET` |
| 8.23 | `export STUDY_KEEP=web-session-alive` |
| 8.43 | `RET` |
| 9.23 | `C-c C-j: term line mode` |
| 9.63 | `C-u` |
| 10.03 | `M-x` |
| 10.33 | `term-run-shell-command` |
| 10.83 | `RET` |
| 11.63 | `/bin/bash --noprofile --norc` |
| 11.83 | `RET` |
| 13.13 | `C-x o: select displayed terminal` |
| 13.54 | `lab-ssh lab-db` |
| 13.73 | `RET` |
| 14.74 | `cat status.txt; tail -n 3 service.log` |
| 14.94 | `RET` |
| 15.94 | `C-c C-j: term line mode` |
| 16.34 | `C-x b: switch-to-buffer` |
| 16.74 | `*Term-Run Shell Command*` |
| 17.14 | `RET` |
| 17.55 | `C-c C-k: term char mode` |
| 17.95 | `printenv STUDY_KEEP` |
| 18.15 | `RET` |
| 18.86 | `less service.log` |
| 19.05 | `RET` |
| 19.76 | `q: leave less` |
| 20.26 | `printf 'PAGER_%s\n' RETURNED` |
| 20.46 | `RET` |
