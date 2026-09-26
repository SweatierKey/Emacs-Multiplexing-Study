# eyebrowse

Categoria: **workspace**. [Sorgente upstream](https://depp.brause.cc/eyebrowse). Revisione: `473381f4f9e847eb50a40ef2306c027432789754`.

## Funzionamento

Slot numerati di configurazioni di finestre con ripristino dei buffer.

## Utilizzo umano e limiti

M-x eyebrowse-switch-to-window-config-2 e -1; due ansi-term verificati.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eyebrowse.md).
- [Log del caricamento](../../results/load/eyebrowse.log).

### Scenario eyebrowse: passed

[Esito e snapshot](../../results/eyebrowse.json) · [Traccia dei tasti](../../results/eyebrowse-keys.json) · [Registrazione asciinema](../../recordings/eyebrowse.cast) · [Player](../../index.html#eyebrowse)

- `ssh_web`: `True`
- `ssh_db`: `True`
- `layout_restores_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `ansi-term` |
| 3.41 | `RET` |
| 4.21 | `b''` |
| 4.41 | `RET` |
| 5.21 | `lab-ssh lab-web` |
| 5.41 | `RET` |
| 6.41 | `cat status.txt; tail -n 3 service.log` |
| 6.61 | `RET` |
| 7.61 | `export STUDY_KEEP=web-session-alive` |
| 7.81 | `RET` |
| 8.61 | `C-c C-j: term line mode` |
| 9.02 | `M-x` |
| 9.31 | `eyebrowse-switch-to-window-config-2` |
| 9.81 | `RET` |
| 10.62 | `M-x` |
| 10.92 | `ansi-term` |
| 11.42 | `RET` |
| 12.22 | `b''` |
| 12.42 | `RET` |
| 13.22 | `lab-ssh lab-db` |
| 13.42 | `RET` |
| 14.42 | `cat status.txt; tail -n 3 service.log` |
| 14.62 | `RET` |
| 15.63 | `C-c C-j: term line mode` |
| 16.04 | `M-x` |
| 16.34 | `eyebrowse-switch-to-window-config-1` |
| 16.84 | `RET` |
| 17.64 | `C-c C-k: term char mode` |
| 18.04 | `printenv STUDY_KEEP` |
| 18.24 | `RET` |
