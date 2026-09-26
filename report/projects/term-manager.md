# term-manager

Categoria: **gestore**. [Sorgente upstream](https://github.com/colonelpanic8/term-manager). Revisione: `1581a90ff9b359449e056da55259b9f42e749f0c`.

## Funzionamento

Gestione indicizzata dei terminali con backend e frontend per directory, project.el e Projectile.

## Utilizzo umano e limiti

M-x term-project-default-directory-create-new e term-project-default-directory-backward. Snapshot mostra il backend effettivo.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term-manager.md).
- [Log del caricamento](../../results/load/term-manager.log).

### Scenario term-manager: passed

[Esito e snapshot](../../results/term-manager.json) · [Traccia dei tasti](../../results/term-manager-keys.json) · [Registrazione asciinema](../../recordings/term-manager.cast) · [Player](../../index.html#term-manager)

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
| 2.61 | `term-project-default-directory-create-new` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-c C-j: term line mode` |
| 8.23 | `M-x` |
| 8.53 | `term-project-default-directory-create-new` |
| 9.03 | `RET` |
| 10.33 | `lab-ssh lab-db` |
| 10.53 | `RET` |
| 11.54 | `cat status.txt; tail -n 3 service.log` |
| 11.73 | `RET` |
| 12.74 | `C-c C-j: term line mode` |
| 13.14 | `M-x` |
| 13.44 | `term-project-default-directory-backward` |
| 13.94 | `RET` |
| 14.74 | `C-c C-k: term char mode` |
| 15.14 | `printenv STUDY_KEEP` |
| 15.34 | `RET` |
| 16.05 | `less service.log` |
| 16.25 | `RET` |
| 16.95 | `q: leave less` |
| 17.45 | `printf 'PAGER_%s\n' RETURNED` |
| 17.65 | `RET` |
