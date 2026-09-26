# elscreen-multi-term

Categoria: **workspace**. [Sorgente upstream](https://github.com/wamei/elscreen-multi-term). Revisione: `4ea89bae0444d9d4377515929f76cb3e98140f1f`.

## Funzionamento

Collega la creazione di multi-term a schermi ElScreen.

## Utilizzo umano e limiti

M-x emt-multi-term. Il copione generico non completa la seconda connessione; non ereditare il successo dei due componenti separati.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/elscreen-multi-term.md).
- [Log del caricamento](../../results/load/elscreen-multi-term.log).

### Scenario elscreen-multi-term: failed

[Esito e snapshot](../../results/elscreen-multi-term.json) · [Traccia dei tasti](../../results/elscreen-multi-term-keys.json) · [Registrazione asciinema](../../recordings/elscreen-multi-term.cast) · [Player](../../index.html#elscreen-multi-term)

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
| 2.91 | `M-x` |
| 3.21 | `emt-multi-term` |
| 3.71 | `RET` |
| 5.01 | `lab-ssh lab-web` |
| 5.21 | `RET` |
| 6.21 | `cat status.txt; tail -n 3 service.log` |
| 6.41 | `RET` |
| 7.42 | `export STUDY_KEEP=web-session-alive` |
| 7.62 | `RET` |
| 8.42 | `C-c C-j: term line mode` |
| 8.82 | `M-x` |
| 9.12 | `emt-multi-term` |
| 9.62 | `RET` |
| 10.92 | `lab-ssh lab-db` |
| 11.12 | `RET` |
| 12.12 | `cat status.txt; tail -n 3 service.log` |
| 12.32 | `RET` |
