# ghostel-switch

Categoria: **gestore**. [Sorgente upstream](https://github.com/JulHee/ghostel-switch). Revisione: `e33a981aaffeb555e453e86b2b4a81a2af40a4e1`.

## Funzionamento

Completamento di buffer Ghostel globali/per progetto con creazione tramite input vuoto.

## Utilizzo umano e limiti

Snapshot incompatibile con Ghostel acquisito: ghostel--all-buffers non definita. Registrazione negativa e messaggi conservati. M-RET serve ad accettare input vuoto in Vertico, non è un binding inventato del pacchetto.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/ghostel-switch.md).
- [Log del caricamento](../../results/load/ghostel-switch.log).

### Scenario ghostel-switch: failed

[Esito e snapshot](../../results/ghostel-switch.json) · [Traccia dei tasti](../../results/ghostel-switch-keys.json) · [Registrazione asciinema](../../recordings/ghostel-switch.cast) · [Player](../../index.html#ghostel-switch)

- `completion_enabled`: `True`

Errore finale: Launch did not enter a terminal: {'name': '*scratch*', 'mode': 'lisp-interaction-mode', 'vertico': True, 'marginalia': True, 'text': ''}

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `ghostel-switch-all` |
| 3.41 | `RET` |
| 4.21 | `M-RET: accept empty input` |
