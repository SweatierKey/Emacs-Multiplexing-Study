# ghostel-mux

Categoria: **gestore**. [Sorgente upstream](https://github.com/SweatierKey/ghostel-mux). Revisione: `c03055c8c081f5afe9ea35cfa431b844f415f949`.

## Funzionamento

Sessioni, finestre e pannelli Emacs contenenti Ghostel; gestione del layout e dell'input sincronizzato.

## Utilizzo umano e limiti

M-x ghostel-mux; C-b c nuova finestra e C-b p precedente. Conservazione SSH verificata. Questa gestione in Emacs da sola non è un server persistente.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/ghostel-mux.md).
- [Log del caricamento](../../results/load/ghostel-mux.log).

### Scenario ghostel-mux: passed

[Esito e snapshot](../../results/ghostel-mux.json) · [Traccia dei tasti](../../results/ghostel-mux-keys.json) · [Registrazione asciinema](../../recordings/ghostel-mux.cast) · [Player](../../index.html#ghostel-mux)

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
| 2.91 | `ghostel-mux` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `native create key` |
| 9.62 | `lab-ssh lab-db` |
| 9.82 | `RET` |
| 10.82 | `cat status.txt; tail -n 3 service.log` |
| 11.02 | `RET` |
| 12.02 | `native previous key` |
| 13.03 | `printenv STUDY_KEEP` |
| 13.23 | `RET` |
| 13.93 | `less service.log` |
| 14.13 | `RET` |
| 14.83 | `q: leave less` |
| 15.33 | `printf 'PAGER_%s\n' RETURNED` |
| 15.53 | `RET` |
