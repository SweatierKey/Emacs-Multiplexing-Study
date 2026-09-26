# eev

Categoria: **integrazione**. [Sorgente upstream](https://github.com/edrx/eev). Revisione: `4850e9c7a465684a0fdb79a6be83055e0ef9537b`.

## Funzionamento

Eepitch conserva un buffer sorgente di istruzioni e un target shell/terminale; F8 invia una riga al target o valuta una riga di controllo contrassegnata dalla stella rossa.

## Utilizzo umano e limiti

Il copione usa eev-mode e il suo F8 predefinito, eepitch-shell/eepitch-shell2 per scegliere target, due SSH e ritorno alla shell web. È una forma di interazione riproducibile guidata dal documento, non un nuovo parser VT.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eev.md).
- [Log del caricamento](../../results/load/eev.log).

### Scenario eev: passed

[Esito e snapshot](../../results/eev.json) · [Traccia dei tasti](../../results/eev-keys.json) · [Registrazione asciinema](../../recordings/eev.cast) · [Player](../../index.html#eev)

- `ssh_web`: `True`
- `return_preserves_shell`: `True`
- `ssh_db`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `C-x C-f` |
| 3.01 | `/home/admin/Emacs-Multiplexing-Study/lab/eev-demo.e` |
| 3.21 | `RET` |
| 4.01 | `M-<` |
| 4.41 | `F8: eepitch line 1` |
| 5.61 | `F8: eepitch line 2` |
| 6.81 | `F8: eepitch line 3` |
| 8.01 | `F8: eepitch line 4` |
| 9.21 | `F8: eepitch line 5` |
| 10.41 | `F8: eepitch line 6` |
| 11.61 | `F8: eepitch line 7` |
| 12.81 | `F8: eepitch line 8` |
| 14.01 | `F8: eepitch line 9` |
| 15.21 | `C-x b` |
| 15.61 | `*shell*` |
| 15.81 | `RET` |
| 16.61 | `C-x b` |
| 17.01 | `*shell 2*` |
| 17.21 | `RET` |
