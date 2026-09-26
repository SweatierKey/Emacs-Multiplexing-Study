# shell-here

Categoria: **launcher-interno**. [Sorgente upstream](https://codeberg.org/emacs-weirdware/shell-here). Revisione: `eeb437ff26d62a5009046b1b3b4503b768e3131a`.

## Funzionamento

Apre shell nel contesto/directory corrente, incluse integrazioni con buffer e progetti.

## Utilizzo umano e limiti

M-x shell-here; C-u M-x shell per un'altra istanza. Non impone un nuovo modello di multiplexer.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/shell-here.md).
- [Log del caricamento](../../results/load/shell-here.log).

### Scenario shell-here: passed

[Esito e snapshot](../../results/shell-here.json) · [Traccia dei tasti](../../results/shell-here-keys.json) · [Registrazione asciinema](../../recordings/shell-here.cast) · [Player](../../index.html#shell-here)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `shell-here` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `C-u` |
| 8.52 | `M-x` |
| 8.82 | `shell` |
| 9.32 | `RET` |
| 10.12 | `C-a C-k` |
| 10.52 | `*shell-db*` |
| 10.72 | `RET` |
| 12.02 | `lab-ssh lab-db` |
| 12.22 | `RET` |
| 13.22 | `cat status.txt; tail -n 3 service.log` |
| 13.42 | `RET` |
| 14.43 | `C-x b: switch-to-buffer` |
| 14.83 | `*shell Emacs-Multiplexing-Study*` |
| 15.23 | `RET` |
| 15.63 | `printenv STUDY_KEEP` |
| 15.83 | `RET` |
