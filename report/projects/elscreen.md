# elscreen

Categoria: **workspace**. [Sorgente upstream](https://github.com/knu/elscreen). Revisione: `cc58337faf5ba1eae7e87f75f6ff3758675688f2`.

## Funzionamento

Configurazioni di finestre dette screen, con prefisso C-z e lista di schermi.

## Utilizzo umano e limiti

elscreen-start; C-z c crea e C-z p torna. Per term passare prima alla modalità Emacs. Scenario verificato.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/elscreen.md).
- [Log del caricamento](../../results/load/elscreen.log).

### Scenario elscreen: passed

[Esito e snapshot](../../results/elscreen.json) · [Traccia dei tasti](../../results/elscreen-keys.json) · [Registrazione asciinema](../../recordings/elscreen.cast) · [Player](../../index.html#elscreen)

- `ssh_web`: `True`
- `ssh_db`: `True`
- `layout_restores_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.91 | `M-x` |
| 3.21 | `ansi-term` |
| 3.71 | `RET` |
| 4.51 | `b''` |
| 4.71 | `RET` |
| 5.51 | `lab-ssh lab-web` |
| 5.71 | `RET` |
| 6.71 | `cat status.txt; tail -n 3 service.log` |
| 6.91 | `RET` |
| 7.91 | `export STUDY_KEEP=web-session-alive` |
| 8.11 | `RET` |
| 8.91 | `C-c C-j: term line mode` |
| 9.31 | `C-z c: create screen` |
| 9.72 | `M-x` |
| 10.02 | `ansi-term` |
| 10.52 | `RET` |
| 11.32 | `b''` |
| 11.52 | `RET` |
| 12.32 | `lab-ssh lab-db` |
| 12.52 | `RET` |
| 13.52 | `cat status.txt; tail -n 3 service.log` |
| 13.72 | `RET` |
| 14.72 | `C-c C-j: term line mode` |
| 15.12 | `C-z p: previous screen` |
| 15.53 | `C-c C-k: term char mode` |
| 15.93 | `printenv STUDY_KEEP` |
| 16.13 | `RET` |
