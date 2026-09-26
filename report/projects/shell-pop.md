# shell-pop

Categoria: **popup**. [Sorgente upstream](https://github.com/kyagi/shell-pop-el). Revisione: `446b1691454e65be648dcb7e316639aa7dd73be2`.

## Funzionamento

Mostra/nasconde una shell e memorizza finestre/buffer; backend configurabili.

## Utilizzo umano e limiti

M-x shell-pop; C-u per un'altra istanza. Profilo predefinito shell verificato.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/shell-pop.md).
- [Log del caricamento](../../results/load/shell-pop.log).

### Scenario shell-pop: passed

[Esito e snapshot](../../results/shell-pop.json) · [Traccia dei tasti](../../results/shell-pop-keys.json) · [Registrazione asciinema](../../recordings/shell-pop.cast) · [Player](../../index.html#shell-pop)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.62 | `shell-pop` |
| 3.12 | `RET` |
| 4.42 | `lab-ssh lab-web` |
| 4.62 | `RET` |
| 5.62 | `cat status.txt; tail -n 3 service.log` |
| 5.82 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.02 | `RET` |
| 7.82 | `C-u` |
| 8.22 | `M-x` |
| 8.53 | `shell-pop` |
| 9.03 | `RET` |
| 10.33 | `lab-ssh lab-db` |
| 10.53 | `RET` |
| 11.53 | `cat status.txt; tail -n 3 service.log` |
| 11.73 | `RET` |
| 12.73 | `C-x b: switch-to-buffer` |
| 13.13 | `*shell-1*` |
| 13.53 | `RET` |
| 13.94 | `printenv STUDY_KEEP` |
| 14.13 | `RET` |
