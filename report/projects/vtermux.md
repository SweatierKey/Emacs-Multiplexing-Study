# vtermux

Categoria: **gestore**. [Sorgente upstream](https://github.com/pcmantz/vtermux). Revisione: `98db8bfde835ba2c100e5dd835d5772ab2becf0a`.

## Funzionamento

Macro che genera launcher per programmi e backend vterm/ghostel/term; liste di istanze, etichette e cycling.

## Utilizzo umano e limiti

Il profilo dichiara un'applicazione bash con vtermux-define; è configurazione necessaria, non un comando incluso nel pacchetto. Launcher generato e nomi richiesti sono registrati.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/vtermux.md).
- [Log del caricamento](../../results/load/vtermux.log).

### Scenario vtermux: passed

[Esito e snapshot](../../results/vtermux.json) · [Traccia dei tasti](../../results/vtermux-keys.json) · [Registrazione asciinema](../../recordings/vtermux.cast) · [Player](../../index.html#vtermux)

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
| 2.91 | `study-bash` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.12 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `M-x` |
| 8.42 | `study-bash` |
| 8.92 | `RET` |
| 9.72 | `db` |
| 9.92 | `RET` |
| 11.22 | `lab-ssh lab-db` |
| 11.42 | `RET` |
| 12.42 | `cat status.txt; tail -n 3 service.log` |
| 12.62 | `RET` |
| 13.62 | `C-x b: switch-to-buffer` |
| 14.03 | `*study-bash - /home/admin/Emacs-Multiplexing-Study/*` |
| 14.43 | `RET` |
| 14.84 | `printenv STUDY_KEEP` |
| 15.04 | `RET` |
| 15.74 | `less service.log` |
| 15.94 | `RET` |
| 16.65 | `q: leave less` |
| 17.15 | `printf 'PAGER_%s\n' RETURNED` |
| 17.35 | `RET` |
