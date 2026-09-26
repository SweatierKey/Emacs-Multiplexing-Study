# vterms

Categoria: **gestore**. [Sorgente upstream](https://github.com/t0yv0/vterms.el). Revisione: `e823b788ebc787374950a0e10bf606019b8443f4`.

## Funzionamento

Wrapper di vterm orientato al progetto e alla creazione ripetuta.

## Utilizzo umano e limiti

M-x vterms-project-vterm; C-u per un altro buffer. Ritorno con C-x b nel test.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/vterms.md).
- [Log del caricamento](../../results/load/vterms.log).

### Scenario vterms: passed

[Esito e snapshot](../../results/vterms.json) · [Traccia dei tasti](../../results/vterms-keys.json) · [Registrazione asciinema](../../recordings/vterms.cast) · [Player](../../index.html#vterms)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.32 | `M-x` |
| 2.62 | `vterms-project-vterm` |
| 3.12 | `RET` |
| 4.42 | `lab-ssh lab-web` |
| 4.62 | `RET` |
| 5.62 | `cat status.txt; tail -n 3 service.log` |
| 5.82 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.02 | `RET` |
| 7.82 | `C-u` |
| 8.23 | `M-x` |
| 8.53 | `vterms-project-vterm` |
| 9.03 | `RET` |
| 10.33 | `lab-ssh lab-db` |
| 10.53 | `RET` |
| 11.53 | `cat status.txt; tail -n 3 service.log` |
| 11.73 | `RET` |
| 12.73 | `C-x b: switch-to-buffer` |
| 13.13 | `*Emacs-Multiplexing-Study-vterm*` |
| 13.53 | `RET` |
| 13.94 | `printenv STUDY_KEEP` |
| 14.14 | `RET` |
| 14.84 | `less service.log` |
| 15.04 | `RET` |
| 15.74 | `q: leave less` |
| 16.24 | `printf 'PAGER_%s\n' RETURNED` |
| 16.44 | `RET` |
