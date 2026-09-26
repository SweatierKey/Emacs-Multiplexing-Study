# ghostel

Categoria: **emulatore**. [Sorgente upstream](https://github.com/dakra/ghostel). Revisione: `c2c411f2b0051465a5f5e7826ebab4ed216d4c0e`.

## Funzionamento

Modulo Zig basato su libghostty-vt, con parsing nativo e resa nel buffer Emacs; modalità di input separate.

## Utilizzo umano e limiti

M-x ghostel, C-u M-x ghostel; C-x b. Snapshot e modulo v0.56.0. La selezione buffer conserva SSH, non dimostra persistenza dopo kill-emacs.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/ghostel.md).
- [Log del caricamento](../../results/load/ghostel.log).

### Scenario ghostel: passed

[Esito e snapshot](../../results/ghostel.json) · [Traccia dei tasti](../../results/ghostel-keys.json) · [Registrazione asciinema](../../recordings/ghostel.cast) · [Player](../../index.html#ghostel)

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
| 2.92 | `ghostel` |
| 3.42 | `RET` |
| 4.73 | `lab-ssh lab-web` |
| 4.93 | `RET` |
| 5.93 | `cat status.txt; tail -n 3 service.log` |
| 6.13 | `RET` |
| 7.13 | `export STUDY_KEEP=web-session-alive` |
| 7.33 | `RET` |
| 8.13 | `C-u` |
| 8.53 | `M-x` |
| 8.83 | `ghostel` |
| 9.33 | `RET` |
| 10.63 | `lab-ssh lab-db` |
| 10.84 | `RET` |
| 11.84 | `cat status.txt; tail -n 3 service.log` |
| 12.04 | `RET` |
| 13.04 | `C-x b: switch-to-buffer` |
| 13.44 | `*ghostel*` |
| 13.84 | `RET` |
| 14.24 | `printenv STUDY_KEEP` |
| 14.44 | `RET` |
| 15.14 | `less service.log` |
| 15.34 | `RET` |
| 16.05 | `q: leave less` |
| 16.55 | `printf 'PAGER_%s\n' RETURNED` |
| 16.75 | `RET` |
