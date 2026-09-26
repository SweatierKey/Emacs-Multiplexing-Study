# coterm

Categoria: **emulatore**. [Sorgente upstream](https://github.com/emacsmirror/coterm). Revisione: `ce3206fbd7156685e2d2f3fbc39b3eea3334754b`.

## Funzionamento

Aggiunge emulazione terminale a comint, con gestione automatica dell'input per applicazioni interattive.

## Utilizzo umano e limiti

Abilitare coterm-mode, poi M-x shell; C-u M-x shell per un nuovo nome. Il test esercita anche less, a differenza del baseline shell.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/coterm.md).
- [Log del caricamento](../../results/load/coterm.log).

### Scenario coterm: passed

[Esito e snapshot](../../results/coterm.json) · [Traccia dei tasti](../../results/coterm-keys.json) · [Registrazione asciinema](../../recordings/coterm.cast) · [Player](../../index.html#coterm)

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
| 2.61 | `shell` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-u` |
| 8.21 | `M-x` |
| 8.52 | `shell` |
| 9.02 | `RET` |
| 9.82 | `C-a C-k` |
| 10.22 | `*shell-db*` |
| 10.42 | `RET` |
| 11.72 | `lab-ssh lab-db` |
| 11.92 | `RET` |
| 12.92 | `cat status.txt; tail -n 3 service.log` |
| 13.12 | `RET` |
| 14.12 | `C-x b: switch-to-buffer` |
| 14.52 | `*shell*` |
| 14.92 | `RET` |
| 15.33 | `printenv STUDY_KEEP` |
| 15.53 | `RET` |
| 16.23 | `less service.log` |
| 16.43 | `RET` |
| 17.13 | `q: leave less` |
| 17.63 | `printf 'PAGER_%s\n' RETURNED` |
| 17.83 | `RET` |
