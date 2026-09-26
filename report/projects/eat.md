# eat

Categoria: **emulatore**. [Sorgente upstream](https://codeberg.org/akib/emacs-eat). Revisione: `c8d54d649872bfe7b2b9f49ae5c2addbf12d3b99`.

## Funzionamento

Macchina terminale in Lisp, renderer nel buffer, modalità semi-char/char/emacs; integrazione Eshell.

## Utilizzo umano e limiti

M-x eat; C-u M-x eat crea un'altra istanza. Nel test due SSH e less. Per il remoto occorre installare la sua terminfo; il laboratorio lo fa esplicitamente.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eat.md).
- [Log del caricamento](../../results/load/eat.log).

### Scenario eat: passed

[Esito e snapshot](../../results/eat.json) · [Traccia dei tasti](../../results/eat-keys.json) · [Registrazione asciinema](../../recordings/eat.cast) · [Player](../../index.html#eat)

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
| 2.91 | `eat` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.11 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `C-u` |
| 8.52 | `M-x` |
| 8.82 | `eat` |
| 9.32 | `RET` |
| 10.62 | `lab-ssh lab-db` |
| 10.82 | `RET` |
| 11.82 | `cat status.txt; tail -n 3 service.log` |
| 12.02 | `RET` |
| 13.02 | `C-x b: switch-to-buffer` |
| 13.42 | `*eat*` |
| 13.82 | `RET` |
| 14.23 | `printenv STUDY_KEEP` |
| 14.43 | `RET` |
| 15.13 | `less service.log` |
| 15.33 | `RET` |
| 16.03 | `q: leave less` |
| 16.53 | `printf 'PAGER_%s\n' RETURNED` |
| 16.73 | `RET` |

### Scenario eat-eshell: passed

[Esito e snapshot](../../results/eat-eshell.json) · [Traccia dei tasti](../../results/eat-eshell-keys.json) · [Registrazione asciinema](../../recordings/eat-eshell.cast) · [Player](../../index.html#eat)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `eshell` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `C-u` |
| 8.52 | `M-x` |
| 8.82 | `eshell` |
| 9.32 | `RET` |
| 10.62 | `lab-ssh lab-db` |
| 10.82 | `RET` |
| 11.82 | `cat status.txt; tail -n 3 service.log` |
| 12.02 | `RET` |
| 13.04 | `C-x b: switch-to-buffer` |
| 13.44 | `*eshell*` |
| 13.84 | `RET` |
| 14.24 | `printenv STUDY_KEEP` |
| 14.45 | `RET` |
