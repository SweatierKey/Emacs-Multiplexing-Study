# libgterm

Categoria: **emulatore**. [Sorgente upstream](https://github.com/rwc9u/emacs-libgterm). Revisione: `5f5516dccb0de06b2233b3492f175c3477f00ef0`.

## Funzionamento

Prototipo distinto di integrazione Ghostty via Zig e modulo dinamico; dipendenza vendor/ghostty.

## Utilizzo umano e limiti

Build tentata con Zig 0.15.2: download di dipendenze transitivamente richieste fallito con TemporaryNameServerFailure. Nessuna demo funzionante; log allegato.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `error`.
- [Indice dei simboli e riferimenti alle righe](../code-index/libgterm.md).
- [Log del caricamento](../../results/load/libgterm.log).

Errore di caricamento osservato (non necessariamente difetto del progetto):

```text
gterm module not compiled. Compile now? (y or n) {"status":"error","error":"End of file during parsing: Error reading from stdin"}
```

**Nessuna dimostrazione end-to-end prodotta per questo progetto.** La descrizione del comportamento deriva dal codice/documentazione, non da una prova eseguita.
