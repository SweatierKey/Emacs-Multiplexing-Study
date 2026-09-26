# tab-bar

Categoria: **workspace**. [Sorgente upstream](https://git.savannah.gnu.org/cgit/emacs). Revisione: `30.1`.

## Funzionamento

Configurazioni di finestre integrate in Emacs; ogni tab può mostrare buffer terminali già vivi.

## Utilizzo umano e limiti

C-x t 2 crea tab, C-x t O torna alla precedente. Due ansi-term e mantenimento SSH verificati. Tab salvata non equivale a processo persistente.

## Evidenza

- Acquisizione: `builtin`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/tab-bar.md).
- [Log del caricamento](../../results/load/tab-bar.log).

### Scenario tab-bar: passed

[Esito e snapshot](../../results/tab-bar.json) · [Traccia dei tasti](../../results/tab-bar-keys.json) · [Registrazione asciinema](../../recordings/tab-bar.cast) · [Player](../../index.html#tab-bar)

- `ssh_web`: `True`
- `ssh_db`: `True`
- `layout_restores_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.60 | `ansi-term` |
| 3.10 | `RET` |
| 3.91 | `b''` |
| 4.11 | `RET` |
| 4.91 | `lab-ssh lab-web` |
| 5.11 | `RET` |
| 6.11 | `cat status.txt; tail -n 3 service.log` |
| 6.31 | `RET` |
| 7.31 | `export STUDY_KEEP=web-session-alive` |
| 7.51 | `RET` |
| 8.31 | `C-c C-j: term line mode` |
| 8.71 | `C-x t 2: new tab` |
| 9.11 | `M-x` |
| 9.41 | `ansi-term` |
| 9.91 | `RET` |
| 10.71 | `b''` |
| 10.91 | `RET` |
| 11.72 | `lab-ssh lab-db` |
| 11.92 | `RET` |
| 12.92 | `cat status.txt; tail -n 3 service.log` |
| 13.12 | `RET` |
| 14.12 | `C-c C-j: term line mode` |
| 14.52 | `C-x t O: previous tab` |
| 14.92 | `C-c C-k: term char mode` |
| 15.32 | `printenv STUDY_KEEP` |
| 15.52 | `RET` |
