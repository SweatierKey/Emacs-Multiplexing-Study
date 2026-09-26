# mistty

Categoria: **emulatore**. [Sorgente upstream](https://github.com/szermatt/mistty). Revisione: `baba2dcd18cac75fc9953da20e8c0a9886441319`.

## Funzionamento

Buffer di lavoro modificabile sincronizzato con un terminale sottostante; le modifiche vengono tradotte in input e riconciliate con l'output.

## Utilizzo umano e limiti

M-x mistty, C-u M-x mistty. Il test usa il backend predefinito dello snapshot; non certifica il backend Alacritty opzionale.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/mistty.md).
- [Log del caricamento](../../results/load/mistty.log).

### Scenario mistty: passed

[Esito e snapshot](../../results/mistty.json) · [Traccia dei tasti](../../results/mistty-keys.json) · [Registrazione asciinema](../../recordings/mistty.cast) · [Player](../../index.html#mistty)

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
| 2.91 | `mistty` |
| 3.41 | `RET` |
| 4.72 | `lab-ssh lab-web` |
| 4.92 | `RET` |
| 5.92 | `cat status.txt; tail -n 3 service.log` |
| 6.12 | `RET` |
| 7.13 | `export STUDY_KEEP=web-session-alive` |
| 7.33 | `RET` |
| 8.13 | `C-u` |
| 8.53 | `M-x` |
| 8.83 | `mistty` |
| 9.33 | `RET` |
| 10.63 | `lab-ssh lab-db` |
| 10.83 | `RET` |
| 11.83 | `cat status.txt; tail -n 3 service.log` |
| 12.03 | `RET` |
| 13.04 | `C-x b: switch-to-buffer` |
| 13.44 | `*mistty*` |
| 13.84 | `RET` |
| 14.24 | `printenv STUDY_KEEP` |
| 14.44 | `RET` |
| 15.14 | `less service.log` |
| 15.34 | `RET` |
| 16.06 | `q: leave less` |
| 16.56 | `printf 'PAGER_%s\n' RETURNED` |
| 16.76 | `RET` |
