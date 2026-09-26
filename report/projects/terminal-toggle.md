# terminal-toggle

Categoria: **popup**. [Sorgente upstream](https://gitlab.com/mtekman/terminal-toggle.el). Revisione: `f824d634aef3600cb7a8e2ddf9e8444c6607c160`.

## Funzionamento

Piccolo progetto GitLab per mostrare/nascondere un terminale interno.

## Utilizzo umano e limiti

M-x terminal-toggle; seconda istanza con ansi-term. Separato da terminal-here, che apre programmi esterni.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/terminal-toggle.md).
- [Log del caricamento](../../results/load/terminal-toggle.log).

### Scenario terminal-toggle: passed

[Esito e snapshot](../../results/terminal-toggle.json) · [Traccia dei tasti](../../results/terminal-toggle-keys.json) · [Registrazione asciinema](../../recordings/terminal-toggle.cast) · [Player](../../index.html#terminal-toggle)

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
| 2.61 | `terminal-toggle` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `C-c C-j: term line mode` |
| 8.22 | `M-x` |
| 8.52 | `ansi-term` |
| 9.02 | `RET` |
| 9.82 | `b''` |
| 10.02 | `RET` |
| 11.32 | `lab-ssh lab-db` |
| 11.52 | `RET` |
| 12.52 | `cat status.txt; tail -n 3 service.log` |
| 12.72 | `RET` |
| 13.73 | `C-c C-j: term line mode` |
| 14.13 | `C-x b: switch-to-buffer` |
| 14.53 | `*myterm*` |
| 14.93 | `RET` |
| 15.33 | `C-c C-k: term char mode` |
| 15.73 | `printenv STUDY_KEEP` |
| 15.93 | `RET` |
| 16.63 | `less service.log` |
| 16.83 | `RET` |
| 17.53 | `q: leave less` |
| 18.03 | `printf 'PAGER_%s\n' RETURNED` |
| 18.23 | `RET` |
