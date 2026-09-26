# aweshell

Categoria: **gestore**. [Sorgente upstream](https://github.com/manateelazycat/aweshell). Revisione: `db495f29eef9013cf6b3796c3797e0ec76352e3f`.

## Funzionamento

Estende Eshell con più buffer e helper di interazione.

## Utilizzo umano e limiti

M-x aweshell-new e aweshell-prev. Scenario lineare verificato; dipendenze caricate dal bundle.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/aweshell.md).
- [Log del caricamento](../../results/load/aweshell.log).

### Scenario aweshell: passed

[Esito e snapshot](../../results/aweshell.json) · [Traccia dei tasti](../../results/aweshell-keys.json) · [Registrazione asciinema](../../recordings/aweshell.cast) · [Player](../../index.html#aweshell)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `aweshell-new` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `M-x` |
| 8.42 | `aweshell-new` |
| 8.92 | `RET` |
| 10.22 | `lab-ssh lab-db` |
| 10.42 | `RET` |
| 11.42 | `cat status.txt; tail -n 3 service.log` |
| 11.62 | `RET` |
| 12.63 | `M-x` |
| 12.93 | `aweshell-prev` |
| 13.43 | `RET` |
| 14.23 | `printenv STUDY_KEEP` |
| 14.43 | `RET` |
