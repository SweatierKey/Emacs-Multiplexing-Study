# eterm-256color

Categoria: **estensione**. [Sorgente upstream](https://git.sr.ht/~dieggsy/eterm-256color). Revisione: `868eeaa958de1deab690fe8ac8f5477452ccdb6a`.

## Funzionamento

Terminfo e hook per colori estesi in term.

## Utilizzo umano e limiti

Richiede compilazione/installazione della terminfo; dopo preparazione e TERMINFO_DIRS il test SSH/pager è riuscito. Il tentativo iniziale fermo alla compilazione resta archiviato. Non un altro emulatore.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eterm-256color.md).
- [Log del caricamento](../../results/load/eterm-256color.log).

### Scenario eterm-256color: passed

[Esito e snapshot](../../results/eterm-256color.json) · [Traccia dei tasti](../../results/eterm-256color-keys.json) · [Registrazione asciinema](../../recordings/eterm-256color.cast) · [Player](../../index.html#eterm-256color)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `ansi-term` |
| 3.41 | `RET` |
| 4.21 | `b''` |
| 4.41 | `RET` |
| 5.71 | `lab-ssh lab-web` |
| 5.91 | `RET` |
| 6.91 | `cat status.txt; tail -n 3 service.log` |
| 7.11 | `RET` |
| 8.12 | `export STUDY_KEEP=web-session-alive` |
| 8.32 | `RET` |
| 9.12 | `C-c C-j: term line mode` |
| 9.53 | `M-x` |
| 9.83 | `ansi-term` |
| 10.33 | `RET` |
| 11.13 | `b''` |
| 11.33 | `RET` |
| 12.64 | `lab-ssh lab-db` |
| 12.84 | `RET` |
| 13.84 | `cat status.txt; tail -n 3 service.log` |
| 14.04 | `RET` |
| 15.04 | `C-c C-j: term line mode` |
| 15.44 | `C-x b: switch-to-buffer` |
| 15.84 | `*ansi-term*` |
| 16.24 | `RET` |
| 16.64 | `C-c C-k: term char mode` |
| 17.04 | `printenv STUDY_KEEP` |
| 17.24 | `RET` |
| 17.95 | `less service.log` |
| 18.14 | `RET` |
| 18.85 | `q: leave less` |
| 19.35 | `printf 'PAGER_%s\n' RETURNED` |
| 19.55 | `RET` |
