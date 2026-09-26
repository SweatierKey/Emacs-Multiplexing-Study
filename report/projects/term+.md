# term+

Categoria: **estensione**. [Sorgente upstream](https://github.com/tarao/term-plus-el). Revisione: `c3c9239b339c127231860de43abfa08c44c0201a`.

## Funzionamento

Estende term con editing, logging, cronologia, trasferimento file e protocollo di escape verso Emacs.

## Utilizzo umano e limiti

Il suo routing dei tasti differisce da term standard; il copione generico non completa lo switching. Non equiparare questo esito a un motore terminale completamente guasto.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/term+.md).
- [Log del caricamento](../../results/load/term+.log).

### Scenario term+: failed

[Esito e snapshot](../../results/term+.json) · [Traccia dei tasti](../../results/term+-keys.json) · [Registrazione asciinema](../../recordings/term+.cast) · [Player](../../index.html#term+)

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
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ xansi-term
bash: xansi-term: command not found
web@lab:~/Emacs-Multiplexing-Study/lab/fixtures/web$ 
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
| 2.61 | `M-x` |
| 2.91 | `ansi-term` |
| 3.41 | `RET` |
| 4.21 | `b''` |
| 4.41 | `RET` |
| 5.72 | `lab-ssh lab-web` |
| 5.92 | `RET` |
| 6.92 | `cat status.txt; tail -n 3 service.log` |
| 7.12 | `RET` |
| 8.12 | `export STUDY_KEEP=web-session-alive` |
| 8.32 | `RET` |
| 9.12 | `M-RET: term+ edit mode` |
| 9.53 | `M-x` |
| 9.82 | `ansi-term` |
| 10.32 | `RET` |
| 11.12 | `b''` |
| 11.32 | `RET` |
| 12.64 | `lab-ssh lab-db` |
| 12.84 | `RET` |
| 13.84 | `cat status.txt; tail -n 3 service.log` |
| 14.04 | `RET` |
