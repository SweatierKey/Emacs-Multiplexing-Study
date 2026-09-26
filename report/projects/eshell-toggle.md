# eshell-toggle

Categoria: **popup**. [Sorgente upstream](https://github.com/4DA/eshell-toggle). Revisione: `04e501e02c475bd9067eebcf8807c951f2316194`.

## Funzionamento

Mostra/nasconde Eshell e conserva il contesto della finestra.

## Utilizzo umano e limiti

M-x eshell-toggle; nuova Eshell con C-u M-x eshell. Test lineare.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/eshell-toggle.md).
- [Log del caricamento](../../results/load/eshell-toggle.log).

### Scenario eshell-toggle: passed

[Esito e snapshot](../../results/eshell-toggle.json) · [Traccia dei tasti](../../results/eshell-toggle-keys.json) · [Registrazione asciinema](../../recordings/eshell-toggle.cast) · [Player](../../index.html#eshell-toggle)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.35 | `M-x` |
| 2.65 | `eshell-toggle` |
| 3.15 | `RET` |
| 4.45 | `lab-ssh lab-web` |
| 4.65 | `RET` |
| 5.65 | `cat status.txt; tail -n 3 service.log` |
| 5.85 | `RET` |
| 6.85 | `export STUDY_KEEP=web-session-alive` |
| 7.05 | `RET` |
| 7.85 | `C-u` |
| 8.26 | `M-x` |
| 8.55 | `eshell` |
| 9.05 | `RET` |
| 10.36 | `lab-ssh lab-db` |
| 10.56 | `RET` |
| 11.56 | `cat status.txt; tail -n 3 service.log` |
| 11.76 | `RET` |
| 12.76 | `C-x b: switch-to-buffer` |
| 13.16 | `*et:home:admin:Emacs-Multiplexing-Study:*` |
| 13.56 | `RET` |
| 13.97 | `printenv STUDY_KEEP` |
| 14.17 | `RET` |
