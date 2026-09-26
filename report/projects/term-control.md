# term-control

Categoria: **gestore**. [Sorgente upstream](https://github.com/Pablololo12/term-control.el). Revisione: `d5c0bf282e0e292881b24c4816de5fde0897034c`.

## Funzionamento

Terminali vterm nominati, associazione allo stato delle tab e completamento dei nomi.

## Utilizzo umano e limiti

M-x term-control-switch-to-term e nomi web/db. Vertico e Marginalia operano sul minibuffer reale.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term-control.md).
- [Log del caricamento](../../results/load/term-control.log).

### Scenario term-control: passed

[Esito e snapshot](../../results/term-control.json) · [Traccia dei tasti](../../results/term-control-keys.json) · [Registrazione asciinema](../../recordings/term-control.cast) · [Player](../../index.html#term-control)

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
| 2.91 | `term-control-switch-to-term` |
| 3.41 | `RET` |
| 4.21 | `web` |
| 4.41 | `RET` |
| 5.71 | `lab-ssh lab-web` |
| 5.92 | `RET` |
| 6.92 | `cat status.txt; tail -n 3 service.log` |
| 7.12 | `RET` |
| 8.12 | `export STUDY_KEEP=web-session-alive` |
| 8.32 | `RET` |
| 9.12 | `M-x` |
| 9.42 | `term-control-switch-to-term` |
| 9.92 | `RET` |
| 10.72 | `db` |
| 10.92 | `RET` |
| 12.23 | `lab-ssh lab-db` |
| 12.43 | `RET` |
| 13.43 | `cat status.txt; tail -n 3 service.log` |
| 13.63 | `RET` |
| 14.64 | `C-x b: switch-to-buffer` |
| 15.04 | `web` |
| 15.44 | `RET` |
| 15.84 | `printenv STUDY_KEEP` |
| 16.04 | `RET` |
| 16.74 | `less service.log` |
| 16.94 | `RET` |
| 17.66 | `q: leave less` |
| 18.16 | `printf 'PAGER_%s\n' RETURNED` |
| 18.36 | `RET` |
