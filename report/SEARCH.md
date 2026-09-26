# Ricerca, provenienza e limiti del censimento

Data: 26 settembre 2026. Sono stati incrociati ricerca web, discussioni Reddit, API GitHub/GitLab/Codeberg, ricette MELPA e riferimenti nei README/codice. La ricerca include progetti molto piccoli, fork storici e nomi ambigui; non impone una soglia minima di stelle.

## Evidenza conservata

| Canale | Traccia riproducibile | Limite |
|---|---|---|
| GitHub | `research/queries.json`, `expanded-queries.json`, `github-search-*.json`, `expanded-github-*.json` | Risultati paginati e limiti API; non è l'intero grafo dei repository |
| GitLab | `research/gitlab-broad-*.json`, `gitlab-emacs-*.json` | Ricerca per parole e pagine, nomi/descriptions spesso insufficienti |
| Codeberg | `research/codeberg-broad-*.json`, `codeberg-emacs-*.json` | API e clone utili anche quando il browser incontra robots; non comprende repository privati/cancellati |
| Google | `research/google-queries.json`, `google-*.html` | HTTP 200 ma pagina/interstitial JavaScript: non rivendichiamo lettura completa dei risultati Google |
| Reddit e ricerca web | Link sotto e `web-discovery.json` | Motore web disponibile non identificato come Google; discussioni usate per scoprire nomi, non come prova del codice |
| MELPA | `research/melpa-recipes/` | Include solo pacchetti presenti nel catalogo e snapshot delle ricette consultate |
| Sorgenti | `research/acquisition*.json`, `source-lock.json`, `source-index.json` | Uno snapshot non è tutta la storia del progetto |

Le query GitHub combinano `emacs terminal emulator`, `terminal multiplexer`, `multiplex`, `vterm`, `terminal manager`, `eshell multiple`, `tmux`, e ricerche nei README per progetti piccoli. Le ricerche GitLab e Codeberg usano combinazioni di Emacs con terminal/shell/tmux/multiplexer. I file grezzi conservano i risultati effettivamente restituiti; le pagine non richieste non sono implicitamente coperte.

## Catene di scoperta verificabili

- [Annuncio multi-buf su Reddit](https://www.reddit.com/r/emacs/comments/1wc2d3v/announcing_multibuf_a_generalized_buffer/) → [djr7C4/multi-buf](https://github.com/djr7C4/multi-buf); commenti → vtermux e multi-buffer.
- [Annuncio storico multi-buffer](https://www.reddit.com/r/emacs/comments/1anp6a4) → [vslavkin/multi-buffer.el su GitLab](https://gitlab.com/vslavkin/multi-buffer.el). Piccolo minor mode di rinomina, acquisito e dimostrato separatamente da multi-buf.
- [Discussione sul workflow tmux in Emacs](https://www.reddit.com/r/emacs/comments/ptqa2g) → [amno1/emacs-term-toggle](https://github.com/amno1/emacs-term-toggle).
- [Ghostel upstream](https://github.com/dakra/ghostel), [documentazione](https://dakra.github.io/ghostel/) e [annuncio](https://www.reddit.com/r/emacs/comments/1sc4n6k/ghostel_terminal_emulator_powered_by_libghostty/) → motore, release e integrazioni. Le prestazioni riportate dai commenti non sono risultati del laboratorio.
- [Ebb](https://github.com/ArthurHeymans/el-be-back), [term-sessions](https://github.com/ArthurHeymans/emacs-term-sessions), [libgterm](https://github.com/rwc9u/emacs-libgterm) e [Kuro](https://github.com/takeokunn/kuro) sono trattati come progetti distinti, senza appiattirli sui nomi più noti.
- [nssh su Codeberg](https://codeberg.org/emacs-weirdware/nssh), [Eat](https://codeberg.org/akib/emacs-eat), [shell-here](https://codeberg.org/emacs-weirdware/shell-here) e i pacchetti term-cmd/term-alert sono stati acquisiti dal loro host.
- [Manuale GNU del terminale Emacs](https://www.gnu.org/software/emacs/manual/html_node/emacs/Terminal-emulator.html) chiarisce la distinzione fra shell e terminale; le versioni effettive sono quelle del laboratorio, non quelle eventualmente cambiate online.

## Inclusioni, duplicati, falsi positivi

Inclusi nel nucleo: motori VT incorporati, shell baseline, gestori di terminali, adapter a multiplexer persistenti. Inclusi per confronto ma separati: popup, workspace, controller send-only, renderer di output, estensioni di colori/tasti, distribuzioni e progetti GUI/Windows.

`term` e `ansi-term` sono due comandi del medesimo term.el. `term+` e `term-plus-xterm` puntano allo stesso upstream. Fork di Eat, multi-term ed emux restano visibili con SHA separati, ma non diventano nuovi motori indipendenti. Repository omonimi emux/herdr/tmux-cc richiedono controllo del percorso realmente caricato.

Esclusi dal nucleo: terminal-here/abysl-term e D-Bus dropdown-remote perché aprono/controllano applicazioni esterne; tmuxbuf per clipboard; myterminal-controls per controlli generici; dotfiles e temi senza implementazione distinta; [eltr](https://gitlab.com/jpellegrini/eltr), che è un REPL Lisp nel terminale, non un terminale dentro Emacs. Non sono stati espansi tutti i fork senza differenze funzionali, tutte le distribuzioni o ogni snippet di configurazione.

Le righe `fetch-failed` non sono prova dell'esistenza di un progetto pertinente. Gli errori dei tentativi iniziali restano nei registri, anche quando un URL successivo è stato corretto.

## Acquisizioni preesistenti e lavoro eseguito

Il repository fornito dall'utente conteneva già workflow e artifact di acquisizione. Sono stati recuperati e riutilizzati, non presentati come esecuzioni nuove di questo laboratorio. Run ID: 36234155070, 36234425022, 36234700164, 36235331001, 36235772598. I workflow in `.github/workflows/` descrivono il recupero iniziale e le build native. Gli script aggiunti importano gli artifact, completano i sorgenti, indicizzano, provano, registrano e costruiscono il dossier.

La chiusura di questa ricerca non dimostra saturazione matematica del web. Nuovi progetti e vecchi frammenti possono continuare a emergere; aggiungerli è possibile mantenendo separate scoperta, acquisizione, analisi e dimostrazione.
