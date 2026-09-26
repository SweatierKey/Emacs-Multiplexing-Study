# multi-eshell

Categoria: **gestore**. [Sorgente upstream](https://github.com/emacsattic/multi-eshell). Revisione: `ac10d93d64e6ea9706ae4396df186faeecaaea12`.

## Funzionamento

Gestore storico di shell: il costruttore predefinito nello snapshot è shell, non Eshell nonostante il nome.

## Utilizzo umano e limiti

M-x multi-eshell; controllare major-mode nelle snapshot anziché dedurre il motore dal nome.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/multi-eshell.md).
- [Log del caricamento](../../results/load/multi-eshell.log).

### Scenario multi-eshell: passed

[Esito e snapshot](../../results/multi-eshell.json) · [Traccia dei tasti](../../results/multi-eshell-keys.json) · [Registrazione asciinema](../../recordings/multi-eshell.cast) · [Player](../../index.html#multi-eshell)

- `completion_enabled`: `True`
- `ssh_web`: `True`
- `ssh_db`: `True`
- `distinct_buffers`: `True`
- `return_preserves_shell`: `True`

Sequenza realmente inviata (secondi dall’avvio, incluso RET):

| t | Tasto / input |
|---:|---|
| 2.31 | `M-x` |
| 2.61 | `multi-eshell` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `multi-eshell` |
| 8.62 | `RET` |
| 9.92 | `lab-ssh lab-db` |
| 10.12 | `RET` |
| 11.12 | `cat status.txt; tail -n 3 service.log` |
| 11.32 | `RET` |
| 12.32 | `C-x b: switch-to-buffer` |
| 12.72 | `*shell*` |
| 13.12 | `RET` |
| 13.53 | `printenv STUDY_KEEP` |
| 13.73 | `RET` |
