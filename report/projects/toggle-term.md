# toggle-term

Categoria: **popup**. [Sorgente upstream](https://github.com/justinlime/toggle-term.el). Revisione: `ebfce6283e53fda7f69ccda73109a02b646623af`.

## Funzionamento

Terminali nominati e scelta del backend/posizione attraverso completing-read e annotazioni.

## Utilizzo umano e limiti

M-x toggle-term-find, nome web/db, posizione bottom, tipo shell. Nel test il completamento usa Vertico/Marginalia.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/toggle-term.md).
- [Log del caricamento](../../results/load/toggle-term.log).

### Scenario toggle-term: passed

[Esito e snapshot](../../results/toggle-term.json) · [Traccia dei tasti](../../results/toggle-term-keys.json) · [Registrazione asciinema](../../recordings/toggle-term.cast) · [Player](../../index.html#toggle-term)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `toggle-term-find` |
| 3.11 | `RET` |
| 3.91 | `web` |
| 4.11 | `RET` |
| 4.91 | `bottom` |
| 5.11 | `RET` |
| 5.91 | `shell` |
| 6.11 | `RET` |
| 7.41 | `lab-ssh lab-web` |
| 7.61 | `RET` |
| 8.61 | `cat status.txt; tail -n 3 service.log` |
| 8.81 | `RET` |
| 9.82 | `export STUDY_KEEP=web-session-alive` |
| 10.02 | `RET` |
| 10.82 | `M-x` |
| 11.12 | `toggle-term-find` |
| 11.62 | `RET` |
| 12.42 | `db` |
| 12.62 | `RET` |
| 13.42 | `bottom` |
| 13.62 | `RET` |
| 14.42 | `shell` |
| 14.62 | `RET` |
| 15.92 | `lab-ssh lab-db` |
| 16.12 | `RET` |
| 17.12 | `cat status.txt; tail -n 3 service.log` |
| 17.32 | `RET` |
| 18.33 | `C-x b: switch-to-buffer` |
| 18.73 | ` *web*` |
| 19.13 | `RET` |
| 19.53 | `printenv STUDY_KEEP` |
| 19.73 | `RET` |
