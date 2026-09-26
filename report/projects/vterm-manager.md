# vterm-manager

Categoria: **gestore**. [Sorgente upstream](https://github.com/laishulu/emacs-vterm-manager). Revisione: `d770fd8cff7c24688199392ad93c01485c6a9569`.

## Funzionamento

Feature vtm, non vterm-manager; apre file .vtm contenenti plist con nome e sequenze di comandi da inviare a vterm.

## Utilizzo umano e limiti

C-x C-f (find-file) sui profili web.vtm/db.vtm forniti; la modalità apre il vterm nominato e chiude il buffer di configurazione. Scenario SSH/pager verificato.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/vterm-manager.md).
- [Log del caricamento](../../results/load/vterm-manager.log).

### Scenario vterm-manager: passed

[Esito e snapshot](../../results/vterm-manager.json) · [Traccia dei tasti](../../results/vterm-manager-keys.json) · [Registrazione asciinema](../../recordings/vterm-manager.cast) · [Player](../../index.html#vterm-manager)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`
- `pager_roundtrip`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `find-file` |
| 3.11 | `RET` |
| 3.91 | `/home/admin/Emacs-Multiplexing-Study/lab/vtm/web.vtm` |
| 4.11 | `RET` |
| 5.41 | `lab-ssh lab-web` |
| 5.61 | `RET` |
| 6.61 | `cat status.txt; tail -n 3 service.log` |
| 6.81 | `RET` |
| 7.81 | `export STUDY_KEEP=web-session-alive` |
| 8.01 | `RET` |
| 8.82 | `M-x` |
| 9.12 | `find-file` |
| 9.62 | `RET` |
| 10.42 | `/home/admin/Emacs-Multiplexing-Study/lab/vtm/db.vtm` |
| 10.62 | `RET` |
| 11.92 | `lab-ssh lab-db` |
| 12.12 | `RET` |
| 13.12 | `cat status.txt; tail -n 3 service.log` |
| 13.32 | `RET` |
| 14.32 | `C-x b: switch-to-buffer` |
| 14.72 | `*>web*` |
| 15.12 | `RET` |
| 15.53 | `printenv STUDY_KEEP` |
| 15.73 | `RET` |
| 16.43 | `less service.log` |
| 16.63 | `RET` |
| 17.33 | `q: leave less` |
| 17.83 | `printf 'PAGER_%s\n' RETURNED` |
| 18.03 | `RET` |
