# vterm-toggle

Categoria: **popup**. [Sorgente upstream](https://github.com/jixiuf/vterm-toggle). Revisione: `a0051a8b8eaa85f8df54ddb032f5710c1f62779d`.

## Funzionamento

Mostra/nasconde vterm e offre selezione per progetto e cambi directory.

## Utilizzo umano e limiti

M-x vterm-toggle; seconda istanza con C-u M-x vterm; vterm-toggle-backward. Il prefisso non viene applicato indiscriminatamente al toggle.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/vterm-toggle.md).
- [Log del caricamento](../../results/load/vterm-toggle.log).

### Scenario vterm-toggle: passed

[Esito e snapshot](../../results/vterm-toggle.json) · [Traccia dei tasti](../../results/vterm-toggle-keys.json) · [Registrazione asciinema](../../recordings/vterm-toggle.cast) · [Player](../../index.html#vterm-toggle)

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
| 2.91 | `vterm-toggle` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.11 | `export STUDY_KEEP=web-session-alive` |
| 7.31 | `RET` |
| 8.12 | `C-u` |
| 8.52 | `M-x` |
| 8.82 | `vterm` |
| 9.32 | `RET` |
| 10.62 | `lab-ssh lab-db` |
| 10.82 | `RET` |
| 11.82 | `cat status.txt; tail -n 3 service.log` |
| 12.02 | `RET` |
| 13.04 | `M-x` |
| 13.34 | `vterm-toggle-backward` |
| 13.84 | `RET` |
| 14.64 | `printenv STUDY_KEEP` |
| 14.84 | `RET` |
| 15.54 | `less service.log` |
| 15.74 | `RET` |
| 16.45 | `q: leave less` |
| 16.95 | `printf 'PAGER_%s\n' RETURNED` |
| 17.15 | `RET` |
