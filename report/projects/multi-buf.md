# multi-buf

Categoria: **gestore**. [Sorgente upstream](https://github.com/djr7C4/multi-buf). Revisione: `dcd28e9d18b4757431eb99a22b2193efb8f87841`.

## Funzionamento

Backend modulari e registro di buffer, con classi e comandi DWIM coerenti fra terminali e altri modi.

## Utilizzo umano e limiti

M-x multi-buf-vterm-dwim; C-u forza una nuova istanza; doppio prefisso per selezione. Il profilo carica esplicitamente vterm, come farebbero gli autoload di un'installazione normale.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/multi-buf.md).
- [Log del caricamento](../../results/load/multi-buf.log).

### Scenario multi-buf: passed

[Esito e snapshot](../../results/multi-buf.json) · [Traccia dei tasti](../../results/multi-buf-keys.json) · [Registrazione asciinema](../../recordings/multi-buf.cast) · [Player](../../index.html#multi-buf)

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
| 2.91 | `multi-buf-vterm-dwim` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.33 | `RET` |
| 8.13 | `C-u` |
| 8.53 | `M-x` |
| 8.83 | `multi-buf-vterm-dwim` |
| 9.33 | `RET` |
| 10.63 | `lab-ssh lab-db` |
| 10.83 | `RET` |
| 11.83 | `cat status.txt; tail -n 3 service.log` |
| 12.03 | `RET` |
| 13.04 | `M-x` |
| 13.34 | `multi-buf-vterm-dwim` |
| 13.84 | `RET` |
| 14.64 | `printenv STUDY_KEEP` |
| 14.84 | `RET` |
| 15.55 | `less service.log` |
| 15.75 | `RET` |
| 16.45 | `q: leave less` |
| 16.95 | `printf 'PAGER_%s\n' RETURNED` |
| 17.15 | `RET` |
