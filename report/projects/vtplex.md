# vtplex

Categoria: **gestore**. [Sorgente upstream](https://github.com/mitch-kyle/vtplex). Revisione: `f853c0f6f32499b24300a0519d348356645c1a33`.

## Funzionamento

Piccolo wrapper di vterm con prefisso C-a e comandi create/next/prev.

## Utilizzo umano e limiti

Nel nostro snapshot vtplex-create richiama vterm senza forzare un nuovo buffer: il secondo terminale viene riutilizzato. Il test fallisce la separazione richiesta; non è stato corretto il codice upstream.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/vtplex.md).
- [Log del caricamento](../../results/load/vtplex.log).

### Scenario vtplex: failed

[Esito e snapshot](../../results/vtplex.json) · [Traccia dei tasti](../../results/vtplex-keys.json) · [Registrazione asciinema](../../recordings/vtplex.cast) · [Player](../../index.html#vtplex)

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
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ lab-ssh lab-db
bash: lab-ssh: command not found
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ cat status.txt; tail -n 3 service.log
role=web
service=active
version=1.0
INFO web health=ok
WARN web disk threshold=75
INFO web requests=42
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ 










Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.33 | `M-x` |
| 2.62 | `vtplex-create` |
| 3.12 | `RET` |
| 4.43 | `lab-ssh lab-web` |
| 4.63 | `RET` |
| 5.63 | `cat status.txt; tail -n 3 service.log` |
| 5.83 | `RET` |
| 6.83 | `export STUDY_KEEP=web-session-alive` |
| 7.03 | `RET` |
| 7.83 | `native create key` |
| 9.33 | `lab-ssh lab-db` |
| 9.53 | `RET` |
| 10.53 | `cat status.txt; tail -n 3 service.log` |
| 10.73 | `RET` |
