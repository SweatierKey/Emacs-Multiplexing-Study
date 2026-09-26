# sticky-shell

Categoria: **estensione**. [Sorgente upstream](https://github.com/andrewdea/sticky-shell). Revisione: `2aec19f60539faf21f567e89701a8e28492eccd1`.

## Funzionamento

Minor mode per shell persistente nell'interfaccia Emacs, sopra comint.

## Utilizzo umano e limiti

Hook shell-mode-hook; due shell create con M-x shell e C-u. Persistenza del buffer non significa sopravvivenza a kill-emacs.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/sticky-shell.md).
- [Log del caricamento](../../results/load/sticky-shell.log).

### Scenario sticky-shell: passed

[Esito e snapshot](../../results/sticky-shell.json) · [Traccia dei tasti](../../results/sticky-shell-keys.json) · [Registrazione asciinema](../../recordings/sticky-shell.cast) · [Player](../../index.html#sticky-shell)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

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
| 8.22 | `M-x` |
| 8.52 | `shell` |
| 9.02 | `RET` |
| 9.82 | `C-a C-k` |
| 10.22 | `*shell-db*` |
| 10.42 | `RET` |
| 11.72 | `lab-ssh lab-db` |
| 11.92 | `RET` |
| 12.93 | `cat status.txt; tail -n 3 service.log` |
| 13.12 | `RET` |
| 14.13 | `C-x b: switch-to-buffer` |
| 14.53 | `*shell*` |
| 14.93 | `RET` |
| 15.33 | `printenv STUDY_KEEP` |
| 15.53 | `RET` |
