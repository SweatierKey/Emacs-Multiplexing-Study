# kuro

Categoria: **emulatore**. [Sorgente upstream](https://github.com/takeokunn/kuro). Revisione: `30a4ff96bdde62c789f42a443766632e8c379873`.

## Funzionamento

Core Rust, parser VTE e trasporto binario degli aggiornamenti verso Emacs Lisp.

## Utilizzo umano e limiti

M-x kuro-create chiede il programma; accettare la shell. Modulo e sorgente 1.2.0 nel test.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/kuro.md).
- [Log del caricamento](../../results/load/kuro.log).

### Scenario kuro: passed

[Esito e snapshot](../../results/kuro.json) · [Traccia dei tasti](../../results/kuro-keys.json) · [Registrazione asciinema](../../recordings/kuro.cast) · [Player](../../index.html#kuro)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 3.51 | `M-x` |
| 3.81 | `kuro-create` |
| 4.31 | `RET` |
| 5.11 | `b''` |
| 5.31 | `RET` |
| 6.62 | `lab-ssh lab-web` |
| 6.82 | `RET` |
| 7.82 | `cat status.txt; tail -n 3 service.log` |
| 8.02 | `RET` |
| 9.02 | `export STUDY_KEEP=web-session-alive` |
| 9.22 | `RET` |
| 10.02 | `M-x` |
| 10.32 | `kuro-create` |
| 10.82 | `RET` |
| 11.62 | `b''` |
| 11.82 | `RET` |
| 13.13 | `lab-ssh lab-db` |
| 13.33 | `RET` |
| 14.33 | `cat status.txt; tail -n 3 service.log` |
| 14.53 | `RET` |
| 15.55 | `C-x b: switch-to-buffer` |
| 15.95 | `*kuro*` |
| 16.35 | `RET` |
| 16.77 | `printenv STUDY_KEEP` |
| 16.97 | `RET` |
| 17.68 | `less service.log` |
| 17.88 | `RET` |
| 18.60 | `q: leave less` |
| 19.10 | `printf 'PAGER_%s\n' RETURNED` |
| 19.30 | `RET` |
