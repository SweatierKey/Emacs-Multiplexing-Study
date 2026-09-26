# eaf-terminal

Categoria: **emulatore-gui**. [Sorgente upstream](https://github.com/emacs-eaf/eaf-terminal). Revisione: `46cbe4f1730970e3db34b3ad86d3fa48fbe92c5b`.

## Funzionamento

Frontend EAF/Python/Qt con xterm.js, WebSocket e backend node-pty; richiede una sessione grafica EAF.

## Utilizzo umano e limiti

M-x eaf-open-terminal dopo installazione dell'applicazione EAF. Non eseguito nel laboratorio Emacs -nw; il probe Lisp non è una verifica dello stack Qt/Node.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `error`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eaf-terminal.md).
- [Log del caricamento](../../results/load/eaf-terminal.log).

Errore di caricamento osservato (non necessariamente difetto del progetto):

```text
Symbol’s value as variable is void: eaf-app-binding-alist
```

**Nessuna dimostrazione end-to-end prodotta per questo progetto.** La descrizione del comportamento deriva dal codice/documentazione, non da una prova eseguita.
