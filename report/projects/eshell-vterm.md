# eshell-vterm

Categoria: **integrazione**. [Sorgente upstream](https://github.com/iostapyshyn/eshell-vterm). Revisione: `20f4b246fa605a1533cdfbe3cb7faf31a24e3d2e`.

## Funzionamento

Delega programmi visuali di Eshell a vterm; non sostituisce l'interprete Eshell.

## Utilizzo umano e limiti

Attivare eshell-vterm-mode, poi Eshell. La registrazione SSH non copre ogni regola di dispatch dei visual commands.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eshell-vterm.md).
- [Log del caricamento](../../results/load/eshell-vterm.log).

### Scenario eshell-vterm: passed

[Esito e snapshot](../../results/eshell-vterm.json) · [Traccia dei tasti](../../results/eshell-vterm-keys.json) · [Registrazione asciinema](../../recordings/eshell-vterm.cast) · [Player](../../index.html#eshell-vterm)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.61 | `M-x` |
| 2.91 | `eshell` |
| 3.41 | `RET` |
| 4.71 | `lab-ssh lab-web` |
| 4.91 | `RET` |
| 5.91 | `cat status.txt; tail -n 3 service.log` |
| 6.11 | `RET` |
| 7.11 | `export STUDY_KEEP=web-session-alive` |
| 7.32 | `RET` |
| 8.12 | `C-u` |
| 8.52 | `M-x` |
| 8.82 | `eshell` |
| 9.32 | `RET` |
| 10.62 | `lab-ssh lab-db` |
| 10.82 | `RET` |
| 11.82 | `cat status.txt; tail -n 3 service.log` |
| 12.02 | `RET` |
| 13.02 | `C-x b: switch-to-buffer` |
| 13.42 | `*eshell*` |
| 13.82 | `RET` |
| 14.23 | `printenv STUDY_KEEP` |
| 14.43 | `RET` |
