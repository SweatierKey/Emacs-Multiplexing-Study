# friendly-shell

Categoria: **gestore**. [Sorgente upstream](https://github.com/p3r7/friendly-shell). Revisione: `5cafa3f6313ce04a47c8996ea1ac6b617d155d46`.

## Funzionamento

Shell comint con nomi e ambiente coerenti, supporto a directory TRAMP.

## Utilizzo umano e limiti

M-x friendly-shell ripetuto; test tramite SSH esplicito. Il percorso TRAMP è analizzato, non testato qui.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/friendly-shell.md).
- [Log del caricamento](../../results/load/friendly-shell.log).

### Scenario friendly-shell: passed

[Esito e snapshot](../../results/friendly-shell.json) · [Traccia dei tasti](../../results/friendly-shell-keys.json) · [Registrazione asciinema](../../recordings/friendly-shell.cast) · [Player](../../index.html#friendly-shell)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `friendly-shell` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `friendly-shell` |
| 8.62 | `RET` |
| 9.92 | `lab-ssh lab-db` |
| 10.12 | `RET` |
| 11.12 | `cat status.txt; tail -n 3 service.log` |
| 11.32 | `RET` |
| 12.32 | `C-x b: switch-to-buffer` |
| 12.72 | `*bash*` |
| 13.12 | `RET` |
| 13.53 | `printenv STUDY_KEEP` |
| 13.73 | `RET` |
