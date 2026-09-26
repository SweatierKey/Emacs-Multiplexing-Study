# term-toggle

Categoria: **popup**. [Sorgente upstream](https://github.com/amno1/emacs-term-toggle). Revisione: `8d3258bc8d03bbb4c735afc681a3c415bb0bbcc6`.

## Funzionamento

Console a comparsa per directory/progetto con molte shell supportate e animazione opzionale.

## Utilizzo umano e limiti

M-x term-toggle-ansi; secondo terminale standard e C-x b. Non confonderlo con terminal-toggle o toggle-term.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term-toggle.md).
- [Log del caricamento](../../results/load/term-toggle.log).

### Scenario term-toggle: passed

[Esito e snapshot](../../results/term-toggle.json) · [Traccia dei tasti](../../results/term-toggle-keys.json) · [Registrazione asciinema](../../recordings/term-toggle.cast) · [Player](../../index.html#term-toggle)

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
| 2.61 | `term-toggle-ansi` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-c C-j: term line mode` |
| 8.22 | `M-x` |
| 8.52 | `ansi-term` |
| 9.02 | `RET` |
| 9.82 | `b''` |
| 10.02 | `RET` |
| 11.33 | `lab-ssh lab-db` |
| 11.53 | `RET` |
| 12.53 | `cat status.txt; tail -n 3 service.log` |
| 12.73 | `RET` |
| 13.74 | `C-c C-j: term line mode` |
| 14.14 | `C-x b: switch-to-buffer` |
| 14.54 | `tt-*terminal*<Emacs-Multiplexing-Study>` |
| 14.94 | `RET` |
| 15.34 | `C-c C-k: term char mode` |
| 15.74 | `printenv STUDY_KEEP` |
| 15.94 | `RET` |
| 16.64 | `less service.log` |
| 16.84 | `RET` |
| 17.55 | `q: leave less` |
| 18.05 | `printf 'PAGER_%s\n' RETURNED` |
| 18.25 | `RET` |
