# popterm

Categoria: **popup**. [Sorgente upstream](https://github.com/ChetanKoneru/popterm.el). Revisione: `d086833f7762d7f9a96954451328ee9a57378b93`.

## Funzionamento

Terminali nominati e per contesto con vari backend e display window/posframe.

## Utilizzo umano e limiti

Nel TTY scelto display window (adattamento strutturale dichiarato), backend vterm caricato; M-x popterm-toggle-named, web/db. La variante posframe GUI non è verificata.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/popterm.md).
- [Log del caricamento](../../results/load/popterm.log).

### Scenario popterm: passed

[Esito e snapshot](../../results/popterm.json) · [Traccia dei tasti](../../results/popterm-keys.json) · [Registrazione asciinema](../../recordings/popterm.cast) · [Player](../../index.html#popterm)

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
| 2.91 | `popterm-toggle-named` |
| 3.41 | `RET` |
| 4.21 | `web` |
| 4.41 | `RET` |
| 5.71 | `lab-ssh lab-web` |
| 5.91 | `RET` |
| 6.91 | `cat status.txt; tail -n 3 service.log` |
| 7.11 | `RET` |
| 8.11 | `export STUDY_KEEP=web-session-alive` |
| 8.31 | `RET` |
| 9.12 | `M-x` |
| 9.42 | `popterm-toggle` |
| 9.92 | `RET` |
| 10.72 | `M-x` |
| 11.02 | `popterm-toggle-named` |
| 11.52 | `RET` |
| 12.32 | `db` |
| 12.52 | `RET` |
| 13.82 | `lab-ssh lab-db` |
| 14.02 | `RET` |
| 15.02 | `cat status.txt; tail -n 3 service.log` |
| 15.22 | `RET` |
| 16.23 | `C-x b: switch-to-buffer` |
| 16.63 | `*popterm-vterm[web]*` |
| 17.03 | `RET` |
| 17.43 | `printenv STUDY_KEEP` |
| 17.63 | `RET` |
| 18.34 | `less service.log` |
| 18.55 | `RET` |
| 19.25 | `q: leave less` |
| 19.75 | `printf 'PAGER_%s\n' RETURNED` |
| 19.95 | `RET` |
