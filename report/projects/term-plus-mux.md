# term-plus-mux

Categoria: **gestore**. [Sorgente upstream](https://github.com/tarao/term-plus-mux-el). Revisione: `cd12a3744d4b7d37a002f4f7fcc4a45ea5be95c3`.

## Funzionamento

Sessioni e tab-group sopra term+, con helper SSH e connessioni persistenti lato SSH.

## Utilizzo umano e limiti

M-x term+mux-new. Il routing del prefisso dipende dalla modalità term+. Il nostro copione non completa lo scenario; registrazione negativa disponibile.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term-plus-mux.md).
- [Log del caricamento](../../results/load/term-plus-mux.log).

### Scenario term-plus-mux: failed

[Esito e snapshot](../../results/term-plus-mux.json) · [Traccia dei tasti](../../results/term-plus-mux-keys.json) · [Registrazione asciinema](../../recordings/term-plus-mux.cast) · [Player](../../index.html#term-plus-mux)

- `completion_enabled`: `True`
- `ssh_web`: `True`

Errore finale: Missing actual remote role output: local@lab:/home/admin/Emacs-Multiplexing-Study$ lab-ssh lab-web

SSH LAB: web (loopback fixture, same kernel)
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ cat status.txt; tail -n 3 service.log
role=web
service=active
version=1.0
INFO web health=ok
WARN web disk threshold=75
INFO web requests=42
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ export STUDY_KEEP=web-session-alive
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ lab-ssh lab-dbcat status.txt; tail -n 3 service.logterm+mux-new

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `term+mux-new` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.92 | `RET` |
| 5.92 | `cat status.txt; tail -n 3 service.log` |
| 6.12 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `M-RET: term+ edit mode` |
| 8.52 | `M-x` |
| 8.82 | `term+mux-new` |
| 9.32 | `RET` |
| 10.62 | `M-RET: term+ char mode` |
| 11.03 | `lab-ssh lab-db` |
| 11.23 | `RET` |
| 12.23 | `cat status.txt; tail -n 3 service.log` |
| 12.43 | `RET` |
