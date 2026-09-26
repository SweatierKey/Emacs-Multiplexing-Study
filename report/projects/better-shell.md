# better-shell

Categoria: **gestore**. [Sorgente upstream](https://github.com/killdash9/better-shell). Revisione: `70c787b981caeef8c5f8012b170eb7b9f167cd13`.

## Funzionamento

Rileva shell inattive e directory per riuso, con helper host remoti e privilegi.

## Utilizzo umano e limiti

M-x better-shell-shell tende a riusare la shell della stessa directory; nel test il secondo buffer è creato con C-u M-x shell. Non vengono dimostrati sudo o tutte le funzioni remote.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/better-shell.md).
- [Log del caricamento](../../results/load/better-shell.log).

### Scenario better-shell: failed

[Esito e snapshot](../../results/better-shell.json) · [Traccia dei tasti](../../results/better-shell-keys.json) · [Registrazione asciinema](../../recordings/better-shell.cast) · [Player](../../index.html#better-shell)

- `completion_enabled`: `True`
- `ssh_web`: `True`

Errore finale: Launch did not enter a terminal: {'name': ' *Minibuf-1*', 'mode': 'minibuffer-mode', 'vertico': True, 'marginalia': True, 'text': 'Shell buffer (default *shell*<2>): '}

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.34 | `M-x` |
| 2.64 | `better-shell-shell` |
| 3.14 | `RET` |
| 4.45 | `lab-ssh lab-web` |
| 4.65 | `RET` |
| 5.65 | `cat status.txt; tail -n 3 service.log` |
| 5.85 | `RET` |
| 6.85 | `export STUDY_KEEP=web-session-alive` |
| 7.05 | `RET` |
| 7.85 | `C-u` |
| 8.25 | `M-x` |
| 8.55 | `shell` |
| 9.05 | `RET` |
