# vterm-ring

Categoria: **gestore**. [Sorgente upstream](https://github.com/daniel-ts/vterm-ring). Revisione: `b251259cb7a73fe468dcead17beac2901e952fbf`.

## Funzionamento

Anello di buffer vterm e hook di pulizia, con creazione e navigazione.

## Utilizzo umano e limiti

M-x vterm-ring-new per creare; il test torna al primo con C-x b, quindi certifica il mantenimento del processo ma non tutte le scorciatoie del ring.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/vterm-ring.md).
- [Log del caricamento](../../results/load/vterm-ring.log).

### Scenario vterm-ring: passed

[Esito e snapshot](../../results/vterm-ring.json) · [Traccia dei tasti](../../results/vterm-ring-keys.json) · [Registrazione asciinema](../../recordings/vterm-ring.cast) · [Player](../../index.html#vterm-ring)

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
| 2.61 | `vterm-ring-new` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.82 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `vterm-ring-new` |
| 8.62 | `RET` |
| 9.92 | `lab-ssh lab-db` |
| 10.12 | `RET` |
| 11.12 | `cat status.txt; tail -n 3 service.log` |
| 11.32 | `RET` |
| 12.32 | `C-x b: switch-to-buffer` |
| 12.73 | `*vterm*<0>` |
| 13.13 | `RET` |
| 13.53 | `printenv STUDY_KEEP` |
| 13.73 | `RET` |
| 14.43 | `less service.log` |
| 14.63 | `RET` |
| 15.33 | `q: leave less` |
| 15.83 | `printf 'PAGER_%s\n' RETURNED` |
| 16.03 | `RET` |
