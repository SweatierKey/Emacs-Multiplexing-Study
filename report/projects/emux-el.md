# emux-el

Categoria: **gestore**. [Sorgente upstream](https://github.com/luozengbin/emux-el). Revisione: `acc8db2b25d394364165ddeee13019a28eff4fba`.

## Funzionamento

Implementazione luozengbin distinta: lista doppiamente collegata di terminali e interfaccia a tab, term-exec.

## Utilizzo umano e limiti

M-x emux:term-new due volte; C-x b per il ritorno. Scenario SSH/pager verificato.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/emux-el.md).
- [Log del caricamento](../../results/load/emux-el.log).

### Scenario emux-el: passed

[Esito e snapshot](../../results/emux-el.json) · [Traccia dei tasti](../../results/emux-el-keys.json) · [Registrazione asciinema](../../recordings/emux-el.cast) · [Player](../../index.html#emux-el)

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
| 2.61 | `emux:term-new` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-c C-j: term line mode` |
| 8.22 | `M-x` |
| 8.52 | `emux:term-new` |
| 9.02 | `RET` |
| 10.32 | `lab-ssh lab-db` |
| 10.52 | `RET` |
| 11.52 | `cat status.txt; tail -n 3 service.log` |
| 11.72 | `RET` |
| 12.72 | `C-c C-j: term line mode` |
| 13.12 | `C-x b: switch-to-buffer` |
| 13.53 | `emux` |
| 13.93 | `RET` |
| 14.33 | `C-c C-k: term char mode` |
| 14.73 | `printenv STUDY_KEEP` |
| 14.93 | `RET` |
| 15.63 | `less service.log` |
| 15.83 | `RET` |
| 16.53 | `q: leave less` |
| 17.03 | `printf 'PAGER_%s\n' RETURNED` |
| 17.23 | `RET` |
