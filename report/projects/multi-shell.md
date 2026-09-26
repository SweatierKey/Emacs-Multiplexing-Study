# multi-shell

Categoria: **gestore**. [Sorgente upstream](https://github.com/emacsmirror/multi-shell). Revisione: `57490c1be4a42b3d0e062a3ea5ebfe53ab21c74d`.

## Funzionamento

Gestisce molte shell comint e il loro passaggio.

## Utilizzo umano e limiti

M-x multi-shell-new; secondo buffer e ritorno con C-x b. Scenario lineare, non full-screen.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/multi-shell.md).
- [Log del caricamento](../../results/load/multi-shell.log).

### Scenario multi-shell: passed

[Esito e snapshot](../../results/multi-shell.json) · [Traccia dei tasti](../../results/multi-shell-keys.json) · [Registrazione asciinema](../../recordings/multi-shell.cast) · [Player](../../index.html#multi-shell)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `multi-shell-new` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `multi-shell-new` |
| 8.62 | `RET` |
| 9.92 | `lab-ssh lab-db` |
| 10.12 | `RET` |
| 11.12 | `cat status.txt; tail -n 3 service.log` |
| 11.32 | `RET` |
| 12.32 | `C-x b: switch-to-buffer` |
| 12.72 | `*multi-shell<1>*` |
| 13.12 | `RET` |
| 13.53 | `printenv STUDY_KEEP` |
| 13.73 | `RET` |
