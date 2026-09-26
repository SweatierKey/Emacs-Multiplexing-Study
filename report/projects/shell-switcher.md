# shell-switcher

Categoria: **gestore**. [Sorgente upstream](https://github.com/DamienCassou/shell-switcher). Revisione: `4c96dc27afb519bdbf7bbe42d49a51497f078192`.

## Funzionamento

Registro di shell e costruttori configurabili; selezione e cycling.

## Utilizzo umano e limiti

M-x shell-switcher-new-shell; M-x shell-switcher-switch-buffer per tornare. Default comint nel test.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/shell-switcher.md).
- [Log del caricamento](../../results/load/shell-switcher.log).

### Scenario shell-switcher: passed

[Esito e snapshot](../../results/shell-switcher.json) · [Traccia dei tasti](../../results/shell-switcher-keys.json) · [Registrazione asciinema](../../recordings/shell-switcher.cast) · [Player](../../index.html#shell-switcher)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `shell-switcher-new-shell` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `shell-switcher-new-shell` |
| 8.62 | `RET` |
| 9.92 | `lab-ssh lab-db` |
| 10.12 | `RET` |
| 11.12 | `cat status.txt; tail -n 3 service.log` |
| 11.32 | `RET` |
| 12.34 | `M-x` |
| 12.64 | `shell-switcher-switch-buffer` |
| 13.14 | `RET` |
| 13.94 | `printenv STUDY_KEEP` |
| 14.14 | `RET` |
