# multi-term

Categoria: **gestore**. [Sorgente upstream](https://github.com/manateelazycat/multi-term). Revisione: `017c77c550115936860e2ea71b88e585371475d5`.

## Funzionamento

Lista di buffer term, creazione e cycling, mappe per passare tasti al processo.

## Utilizzo umano e limiti

M-x multi-term, ripetere per nuovo terminale, M-x multi-term-prev. M-n/M-p non vanno confusi con switching: possono agire sulla cronologia shell.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/multi-term.md).
- [Log del caricamento](../../results/load/multi-term.log).

### Scenario multi-term: passed

[Esito e snapshot](../../results/multi-term.json) · [Traccia dei tasti](../../results/multi-term-keys.json) · [Registrazione asciinema](../../recordings/multi-term.cast) · [Player](../../index.html#multi-term)

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
| 2.62 | `multi-term` |
| 3.12 | `RET` |
| 4.42 | `lab-ssh lab-web` |
| 4.62 | `RET` |
| 5.62 | `cat status.txt; tail -n 3 service.log` |
| 5.82 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.02 | `RET` |
| 7.83 | `C-c C-j: term line mode` |
| 8.23 | `M-x` |
| 8.53 | `multi-term` |
| 9.03 | `RET` |
| 10.33 | `lab-ssh lab-db` |
| 10.53 | `RET` |
| 11.53 | `cat status.txt; tail -n 3 service.log` |
| 11.73 | `RET` |
| 12.73 | `C-c C-j: term line mode` |
| 13.13 | `M-x` |
| 13.43 | `multi-term-prev` |
| 13.93 | `RET` |
| 14.74 | `printenv STUDY_KEEP` |
| 14.94 | `RET` |
| 15.64 | `less service.log` |
| 15.84 | `RET` |
| 16.55 | `q: leave less` |
| 17.05 | `printf 'PAGER_%s\n' RETURNED` |
| 17.25 | `RET` |
