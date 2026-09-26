# alacritty

Categoria: **emulatore**. [Sorgente upstream](https://github.com/ArthurHeymans/emacs-alacritty). Revisione: `a81152af4702bd3b8fd8c737ce8a5abeb7593121`.

## Funzionamento

ArthurHeymans/emacs-alacritty: modulo Rust che espone il motore Alacritty a un terminale nel buffer.

## Utilizzo umano e limiti

M-x alacritty crea terminali; ritorno con C-x b. Modulo costruito nell'acquisizione e verificato nel laboratorio; non è l'applicazione grafica Alacritty incorporata.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `loaded`.
- [Indice dei simboli e riferimenti alle righe](../code-index/alacritty.md).
- [Log del caricamento](../../results/load/alacritty.log).

### Scenario alacritty: passed

[Esito e snapshot](../../results/alacritty.json) · [Traccia dei tasti](../../results/alacritty-keys.json) · [Registrazione asciinema](../../recordings/alacritty.cast) · [Player](../../index.html#alacritty)

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
| 2.61 | `alacritty` |
| 3.11 | `RET` |
| 4.41 | `lab-ssh lab-web` |
| 4.61 | `RET` |
| 5.61 | `cat status.txt; tail -n 3 service.log` |
| 5.81 | `RET` |
| 6.81 | `export STUDY_KEEP=web-session-alive` |
| 7.01 | `RET` |
| 7.82 | `M-x` |
| 8.12 | `alacritty` |
| 8.62 | `RET` |
| 9.92 | `lab-ssh lab-db` |
| 10.12 | `RET` |
| 11.12 | `cat status.txt; tail -n 3 service.log` |
| 11.32 | `RET` |
| 12.32 | `C-x b: switch-to-buffer` |
| 12.72 | `*alacritty*` |
| 13.12 | `RET` |
| 13.53 | `printenv STUDY_KEEP` |
| 13.72 | `RET` |
| 14.43 | `less service.log` |
| 14.63 | `RET` |
| 15.33 | `q: leave less` |
| 15.83 | `printf 'PAGER_%s\n' RETURNED` |
| 16.03 | `RET` |
