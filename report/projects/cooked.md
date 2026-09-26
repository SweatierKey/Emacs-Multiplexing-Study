# cooked

Categoria: **emulatore**. [Sorgente upstream](https://github.com/vodik/cooked). Revisione: `dd8e9fcc3c09d85d9dd598682dbe6390bd138262`.

## Funzionamento

Core Rust con PTY e gestione dell'ownership dei tasti in base a stato del terminale e shell integration.

## Utilizzo umano e limiti

M-x cooked e C-u per nuova istanza. In input raw remoto M-x da solo viene inviato alla shell: usare il default C-c M-x. Il wrapper bash del laboratorio non abilita tutte le integrazioni di startup della shell.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/cooked.md).
- [Log del caricamento](../../results/load/cooked.log).

### Scenario cooked: passed

[Esito e snapshot](../../results/cooked.json) · [Traccia dei tasti](../../results/cooked-keys.json) · [Registrazione asciinema](../../recordings/cooked.cast) · [Player](../../index.html#cooked)

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
| 2.92 | `cooked` |
| 3.42 | `RET` |
| 4.72 | `lab-ssh lab-web` |
| 4.92 | `RET` |
| 5.92 | `cat status.txt; tail -n 3 service.log` |
| 6.12 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.33 | `RET` |
| 8.13 | `C-u` |
| 8.53 | `C-c M-x` |
| 8.83 | `cooked` |
| 9.33 | `RET` |
| 10.63 | `lab-ssh lab-db` |
| 10.83 | `RET` |
| 11.83 | `cat status.txt; tail -n 3 service.log` |
| 12.03 | `RET` |
| 13.04 | `C-x b: switch-to-buffer` |
| 13.44 | `*cooked: /home/admin/Emacs-Multiplexing-Study/*` |
| 13.84 | `RET` |
| 14.24 | `printenv STUDY_KEEP` |
| 14.44 | `RET` |
| 15.14 | `less service.log` |
| 15.34 | `RET` |
| 16.04 | `q: leave less` |
| 16.54 | `printf 'PAGER_%s\n' RETURNED` |
| 16.74 | `RET` |
