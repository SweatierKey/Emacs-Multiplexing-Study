# tmux-view

Categoria: **viewer**. [Sorgente upstream](https://github.com/mgalgs/tmux-view.el). Revisione: `3f0339f568a68f128a678e684ebf351a0b647bd2`.

## Funzionamento

Cattura la pane tmux e rende lo scrollback/ANSI in un buffer di visualizzazione.

## Utilizzo umano e limiti

M-x tmux-view sceglie pane web/db con Vertico; nel test legge output SSH predisposto nella fixture. Il video dimostra consultazione, non input interattivo o resize sincronizzato.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/tmux-view.md).
- [Log del caricamento](../../results/load/tmux-view.log).

### Scenario tmux-view: passed

[Esito e snapshot](../../results/tmux-view.json) · [Traccia dei tasti](../../results/tmux-view-keys.json) · [Registrazione asciinema](../../recordings/tmux-view.cast) · [Player](../../index.html#tmux-view)

- `completion_enabled`: `True`
- `remote_web_capture_visible`: `True`
- `remote_db_capture_visible`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 3.55 | `M-x` |
| 3.85 | `tmux-view` |
| 4.35 | `RET` |
| 5.15 | `ops/web/0:` |
| 5.35 | `RET` |
| 6.76 | `M-x` |
| 7.06 | `tmux-view` |
| 7.56 | `RET` |
| 8.36 | `ops/db/0:` |
| 8.56 | `RET` |
