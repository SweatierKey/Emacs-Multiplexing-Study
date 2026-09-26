# navorski

Categoria: **gestore**. [Sorgente upstream](https://github.com/roman/navorski.el). Revisione: `698c1c62da70164aebe9a7a5d034778fbc30ea5b`.

## Funzionamento

Profili e macro per terminali locali/remoti; opzione GNU screen per sessioni persistenti.

## Utilizzo umano e limiti

M-x nav/term nel test locale con due SSH. La variante screen non è coperta da quella registrazione.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/navorski.md).
- [Log del caricamento](../../results/load/navorski.log).

### Scenario navorski: passed

[Esito e snapshot](../../results/navorski.json) · [Traccia dei tasti](../../results/navorski-keys.json) · [Registrazione asciinema](../../recordings/navorski.cast) · [Player](../../index.html#navorski)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `nav/term` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.92 | `cat status.txt; tail -n 3 service.log` |
| 6.12 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `C-c C-j: term line mode` |
| 8.52 | `M-x` |
| 8.82 | `nav/term` |
| 9.32 | `RET` |
| 10.64 | `lab-ssh lab-db` |
| 10.84 | `RET` |
| 11.84 | `cat status.txt; tail -n 3 service.log` |
| 12.04 | `RET` |
| 13.04 | `C-c C-j: term line mode` |
| 13.44 | `C-x b: switch-to-buffer` |
| 13.84 | `*terminal*` |
| 14.24 | `RET` |
| 14.64 | `printenv STUDY_KEEP` |
| 14.84 | `RET` |
| 15.55 | `less service.log` |
| 15.75 | `RET` |
| 16.45 | `q: leave less` |
| 16.95 | `printf 'PAGER_%s\n' RETURNED` |
| 17.15 | `RET` |
