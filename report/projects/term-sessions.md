# term-sessions

Categoria: **persistenza**. [Sorgente upstream](https://github.com/ArthurHeymans/emacs-term-sessions). Revisione: `29084b6a8a73b612f60a73ef798303384bd44215`.

## Funzionamento

Frontend Emacs per sessioni zmx; adapter term/vterm/eat/ghostel/ebb/shell e integrazione Org/TRAMP.

## Utilizzo umano e limiti

M-x term-sessions-open con nomi web/db; backend predefinito term. Prova separata verifica la sessione dopo chiusura e riapertura di Emacs.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term-sessions.md).
- [Log del caricamento](../../results/load/term-sessions.log).

### Scenario term-sessions: passed

[Esito e snapshot](../../results/term-sessions.json) · [Traccia dei tasti](../../results/term-sessions-keys.json) · [Registrazione asciinema](../../recordings/term-sessions.cast) · [Player](../../index.html#term-sessions)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.62 | `M-x` |
| 2.92 | `term-sessions-open` |
| 3.42 | `RET` |
| 4.22 | `web` |
| 4.42 | `RET` |
| 5.74 | `lab-ssh lab-web` |
| 5.94 | `RET` |
| 6.94 | `cat status.txt; tail -n 3 service.log` |
| 7.14 | `RET` |
| 8.14 | `export STUDY_KEEP=web-session-alive` |
| 8.34 | `RET` |
| 9.14 | `C-c C-j: term line mode` |
| 9.54 | `M-x` |
| 9.84 | `term-sessions-open` |
| 10.34 | `RET` |
| 11.14 | `db` |
| 11.35 | `RET` |
| 12.65 | `lab-ssh lab-db` |
| 12.85 | `RET` |
| 13.85 | `cat status.txt; tail -n 3 service.log` |
| 14.05 | `RET` |
| 15.05 | `C-c C-j: term line mode` |
| 15.45 | `C-x b: switch-to-buffer` |
| 15.85 | `*term-session:web: ~/Emacs-Multiplexing-Study*` |
| 16.25 | `RET` |
| 16.66 | `C-c C-k: term char mode` |
| 17.05 | `printenv STUDY_KEEP` |
| 17.25 | `RET` |
| 17.96 | `less service.log` |
| 18.16 | `RET` |
| 18.86 | `q: leave less` |
| 19.36 | `printf 'PAGER_%s\n' RETURNED` |
| 19.56 | `RET` |

### Scenario term-sessions-persistence: passed

[Esito e snapshot](../../results/term-sessions-persistence.json) · [Traccia dei tasti](../../results/term-sessions-persistence-keys.json) · [Registrazione asciinema](../../recordings/term-sessions-persistence.cast) · [Player](../../index.html#term-sessions)

- `survives_emacs_exit`: `True`
- `restart_reconnect`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.62 | `M-x` |
| 2.92 | `term-sessions-open` |
| 3.42 | `RET` |
| 4.22 | `ops` |
| 4.42 | `RET` |
| 5.42 | `lab-ssh lab-web` |
| 5.62 | `RET` |
| 6.62 | `cat status.txt; tail -n 3 service.log` |
| 6.82 | `RET` |
| 7.83 | `export STUDY_KEEP=web-session-alive` |
| 8.03 | `RET` |

[Registrazione della riconnessione](../../recordings/term-sessions-persistence-resume.cast).
