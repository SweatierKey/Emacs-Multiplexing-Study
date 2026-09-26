# emux

Categoria: **gestore**. [Sorgente upstream](https://github.com/re5et/emux). Revisione: `ab000ab78fb6a96b00ac8332575871a31f6f9548`.

## Funzionamento

Progetto re5et: sessioni, screen e configurazioni di finestre sopra multi-term; moduli emux-base/emux-screen/emux-session.

## Utilizzo umano e limiti

Caricare emux-term e usare M-x emux-term-create. Due SSH e pager verificati. Questo testa il gestore di terminali, non tutte le gerarchie di sessioni/screen.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/emux.md).
- [Log del caricamento](../../results/load/emux.log).

### Scenario emux: passed

[Esito e snapshot](../../results/emux.json) · [Traccia dei tasti](../../results/emux-keys.json) · [Registrazione asciinema](../../recordings/emux.cast) · [Player](../../index.html#emux)

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
| 2.61 | `emux-term-create` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-c C-j: term line mode` |
| 8.22 | `M-x` |
| 8.52 | `emux-term-create` |
| 9.02 | `RET` |
| 10.33 | `lab-ssh lab-db` |
| 10.53 | `RET` |
| 11.53 | `cat status.txt; tail -n 3 service.log` |
| 11.73 | `RET` |
| 12.73 | `C-c C-j: term line mode` |
| 13.13 | `C-x b: switch-to-buffer` |
| 13.54 | `terminal` |
| 13.94 | `RET` |
| 14.34 | `printenv STUDY_KEEP` |
| 14.54 | `RET` |
| 15.25 | `less service.log` |
| 15.45 | `RET` |
| 16.16 | `q: leave less` |
| 16.66 | `printf 'PAGER_%s\n' RETURNED` |
| 16.86 | `RET` |
