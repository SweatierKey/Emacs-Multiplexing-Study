# multi-buffer

Categoria: **gestore**. [Sorgente upstream](https://gitlab.com/vslavkin/multi-buffer.el). Revisione: `4459d83bb0e2a5399d5cace0016f13778a1f5869`.

## Funzionamento

Piccolo progetto GitLab: minor mode che rinomina per major-mode e indice e aggiorna gli indici alla chiusura; manca un launcher/cycler proprio.

## Utilizzo umano e limiti

Abilitato con eat-mode-hook nel profilo; poi M-x eat. Il README propone wrapper personalizzati, che non vengono spacciati per comandi predefiniti.

## Evidenza

- Acquisizione: `fetched`.
- Caricamento isolato: `error`.
- [Indice dei simboli e riferimenti alle righe](../code-index/multi-buffer.md).
- [Log del caricamento](../../results/load/multi-buffer.log).

Errore di caricamento osservato (non necessariamente difetto del progetto):

```text
Loading file /home/admin/Emacs-Multiplexing-Study/sources/multi-buffer/multi-buffer.el failed to provide feature ‘multi-buffer’
```

### Scenario multi-buffer: passed

[Esito e snapshot](../../results/multi-buffer.json) · [Traccia dei tasti](../../results/multi-buffer-keys.json) · [Registrazione asciinema](../../recordings/multi-buffer.cast) · [Player](../../index.html#multi-buffer)

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
| 2.91 | `eat` |
| 3.41 | `RET` |
| 4.73 | `lab-ssh lab-web` |
| 4.93 | `RET` |
| 5.93 | `cat status.txt; tail -n 3 service.log` |
| 6.13 | `RET` |
| 7.13 | `export STUDY_KEEP=web-session-alive` |
| 7.33 | `RET` |
| 8.13 | `M-x` |
| 8.43 | `eat` |
| 8.93 | `RET` |
| 10.25 | `lab-ssh lab-db` |
| 10.45 | `RET` |
| 11.45 | `cat status.txt; tail -n 3 service.log` |
| 11.65 | `RET` |
| 12.65 | `C-x b: switch-to-buffer` |
| 13.05 | `*eat 1*` |
| 13.45 | `RET` |
| 13.87 | `printenv STUDY_KEEP` |
| 14.07 | `RET` |
| 14.77 | `less service.log` |
| 14.97 | `RET` |
| 15.67 | `q: leave less` |
| 16.17 | `printf 'PAGER_%s\n' RETURNED` |
| 16.37 | `RET` |
