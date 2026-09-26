# lterm

Categoria: **terminale-lineare**. [Sorgente upstream](https://github.com/TaylanUB/lterm). Revisione: `734cb5bd91fff337cefd266c4e43a9ae306e4c51`.

## Funzionamento

Usa lui di Circe e xterm-color per output orientato alle righe; il codice dichiara esplicitamente i limiti rispetto a un vero emulatore completo.

## Utilizzo umano e limiti

M-x lterm; due SSH lineari verificati. Nessuna rivendicazione di compatibilità ncurses o schermo alternativo.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/lterm.md).
- [Log del caricamento](../../results/load/lterm.log).

### Scenario lterm: passed

[Esito e snapshot](../../results/lterm.json) · [Traccia dei tasti](../../results/lterm-keys.json) · [Registrazione asciinema](../../recordings/lterm.cast) · [Player](../../index.html#lterm)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `lterm` |
| 3.41 | `RET` |
| 4.21 | `b''` |
| 4.41 | `RET` |
| 5.71 | `lab-ssh lab-web` |
| 5.91 | `RET` |
| 6.91 | `cat status.txt; tail -n 3 service.log` |
| 7.11 | `RET` |
| 8.12 | `export STUDY_KEEP=web-session-alive` |
| 8.32 | `RET` |
| 9.12 | `M-x` |
| 9.42 | `lterm` |
| 9.92 | `RET` |
| 10.72 | `b''` |
| 10.92 | `RET` |
| 12.22 | `lab-ssh lab-db` |
| 12.42 | `RET` |
| 13.42 | `cat status.txt; tail -n 3 service.log` |
| 13.62 | `RET` |
| 14.63 | `C-x b: switch-to-buffer` |
| 15.03 | `*lterm*` |
| 15.43 | `RET` |
| 15.83 | `printenv STUDY_KEEP` |
| 16.03 | `RET` |
