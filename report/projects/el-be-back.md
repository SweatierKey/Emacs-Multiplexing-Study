# el-be-back

Categoria: **emulatore**. [Sorgente upstream](https://github.com/ArthurHeymans/el-be-back). Revisione: `e7a4b2d3b340aa98fd99d593054cca834601f4d6`.

## Funzionamento

Ebb: Lisp, separazione dello stato dello schermo dal rendering del buffer, discendenza architetturale da Eat.

## Utilizzo umano e limiti

M-x ebb e C-u M-x ebb. Due SSH e pager verificati. Nessun confronto prestazionale deducibile da questo scenario.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/el-be-back.md).
- [Log del caricamento](../../results/load/el-be-back.log).

### Scenario el-be-back: passed

[Esito e snapshot](../../results/el-be-back.json) · [Traccia dei tasti](../../results/el-be-back-keys.json) · [Registrazione asciinema](../../recordings/el-be-back.cast) · [Player](../../index.html#el-be-back)

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
| 2.92 | `ebb` |
| 3.42 | `RET` |
| 4.74 | `lab-ssh lab-web` |
| 4.93 | `RET` |
| 5.93 | `cat status.txt; tail -n 3 service.log` |
| 6.13 | `RET` |
| 7.14 | `export STUDY_KEEP=web-session-alive` |
| 7.34 | `RET` |
| 8.14 | `C-u` |
| 8.54 | `M-x` |
| 8.84 | `ebb` |
| 9.34 | `RET` |
| 10.64 | `lab-ssh lab-db` |
| 10.84 | `RET` |
| 11.84 | `cat status.txt; tail -n 3 service.log` |
| 12.04 | `RET` |
| 13.05 | `C-x b: switch-to-buffer` |
| 13.45 | `*ebb: /home/admin/Emacs-Multiplexing-Study*` |
| 13.85 | `RET` |
| 14.25 | `printenv STUDY_KEEP` |
| 14.45 | `RET` |
| 15.15 | `less service.log` |
| 15.35 | `RET` |
| 16.05 | `q: leave less` |
| 16.55 | `printf 'PAGER_%s\n' RETURNED` |
| 16.75 | `RET` |
