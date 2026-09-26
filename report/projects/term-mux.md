# term-mux

Categoria: **gestore**. [Sorgente upstream](https://github.com/merrickluo/term-mux.el). Revisione: `0b1770318c892de0d9dce5a5eb6cde38b9c03d78`.

## Funzionamento

Registro di sessioni e slot di buffer con backend selezionabile fra terminali disponibili.

## Utilizzo umano e limiti

M-x term-mux-create, term-mux-prev. Il backend effettivo è visibile nelle snapshot del test.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term-mux.md).
- [Log del caricamento](../../results/load/term-mux.log).

### Scenario term-mux: passed

[Esito e snapshot](../../results/term-mux.json) · [Traccia dei tasti](../../results/term-mux-keys.json) · [Registrazione asciinema](../../recordings/term-mux.cast) · [Player](../../index.html#term-mux)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.62 | `M-x` |
| 2.92 | `term-mux-create` |
| 3.42 | `RET` |
| 4.72 | `lab-ssh lab-web` |
| 4.92 | `RET` |
| 5.93 | `cat status.txt; tail -n 3 service.log` |
| 6.13 | `RET` |
| 7.13 | `export STUDY_KEEP=web-session-alive` |
| 7.33 | `RET` |
| 8.13 | `M-x` |
| 8.43 | `term-mux-create` |
| 8.93 | `RET` |
| 10.23 | `lab-ssh lab-db` |
| 10.44 | `RET` |
| 11.44 | `cat status.txt; tail -n 3 service.log` |
| 11.63 | `RET` |
| 12.64 | `M-x` |
| 12.94 | `term-mux-prev` |
| 13.44 | `RET` |
| 14.24 | `printenv STUDY_KEEP` |
| 14.44 | `RET` |
| 15.14 | `less service.log` |
| 15.34 | `RET` |
| 16.05 | `q: leave less` |
| 16.55 | `printf 'PAGER_%s\n' RETURNED` |
| 16.75 | `RET` |
