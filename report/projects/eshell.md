# eshell

Categoria: **baseline**. [Sorgente upstream](https://git.savannah.gnu.org/cgit/emacs). Revisione: `30.1`.

## Funzionamento

Shell implementata in Emacs Lisp; alcuni programmi visuali vengono delegati a terminali esterni al suo interprete.

## Utilizzo umano e limiti

M-x eshell e C-u M-x eshell. Due SSH verificano l'uso pratico, non trasformano il motore Eshell in un parser VT.

## Evidenza

- Acquisizione: `builtin`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eshell.md).
- [Log del caricamento](../../results/load/eshell.log).

### Scenario eshell: passed

[Esito e snapshot](../../results/eshell.json) · [Traccia dei tasti](../../results/eshell-keys.json) · [Registrazione asciinema](../../recordings/eshell.cast) · [Player](../../index.html#eshell)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `eshell` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-u` |
| 8.22 | `M-x` |
| 8.52 | `eshell` |
| 9.02 | `RET` |
| 10.33 | `lab-ssh lab-db` |
| 10.53 | `RET` |
| 11.53 | `cat status.txt; tail -n 3 service.log` |
| 11.73 | `RET` |
| 12.74 | `C-x b: switch-to-buffer` |
| 13.14 | `*eshell*` |
| 13.54 | `RET` |
| 13.94 | `printenv STUDY_KEEP` |
| 14.14 | `RET` |
