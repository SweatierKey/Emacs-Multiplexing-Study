# multi-vterm

Categoria: **gestore**. [Sorgente upstream](https://github.com/suonlight/multi-vterm). Revisione: `36746d85870dac5aaee6b9af4aa1c3c0ef21a905`.

## Funzionamento

Lista di vterm, cycling, terminale dedicato e helper per progetti.

## Utilizzo umano e limiti

M-x multi-vterm due volte, M-x multi-vterm-prev. Non occorre inventare un binding globale per dimostrarlo.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/multi-vterm.md).
- [Log del caricamento](../../results/load/multi-vterm.log).

### Scenario multi-vterm: passed

[Esito e snapshot](../../results/multi-vterm.json) · [Traccia dei tasti](../../results/multi-vterm-keys.json) · [Registrazione asciinema](../../recordings/multi-vterm.cast) · [Player](../../index.html#multi-vterm)

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
| 2.62 | `multi-vterm` |
| 3.12 | `RET` |
| 4.42 | `lab-ssh lab-web` |
| 4.62 | `RET` |
| 5.62 | `cat status.txt; tail -n 3 service.log` |
| 5.82 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.02 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `multi-vterm` |
| 8.62 | `RET` |
| 9.93 | `lab-ssh lab-db` |
| 10.13 | `RET` |
| 11.13 | `cat status.txt; tail -n 3 service.log` |
| 11.33 | `RET` |
| 12.33 | `M-x` |
| 12.63 | `multi-vterm-prev` |
| 13.13 | `RET` |
| 13.95 | `printenv STUDY_KEEP` |
| 14.15 | `RET` |
| 14.86 | `less service.log` |
| 15.06 | `RET` |
| 15.76 | `q: leave less` |
| 16.26 | `printf 'PAGER_%s\n' RETURNED` |
| 16.46 | `RET` |
