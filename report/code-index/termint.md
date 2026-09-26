# Indice del codice: termint

Fonte: https://github.com/milanglacier/termint.el.git

Revisione: `bf97d0a417902417febc2b6925152dab5610057f`.


## .dir-locals.el


## termint.el

- L66: `(require 'cl-lib)`
- L92: `(defcustom termint-backend 'term`
- L106: `(defcustom termint-region-dispatchers`
- L120: `(defcustom termint-schema-custom-commands nil`
- L137: `(defcustom termint-mode-map-additional-keys`
- L156: `(defun termint--get-session-suffix (session)`
- L164: `(defun termint--repl-buffer-name (repl-name session)`
- L170: `(defun termint-find-binary`
- L199: `(defun termint-ipython-cmd-function ()`
- L208: `(defun termint-python-cmd-function ()`
- L218: `(defun termint--start (repl-name repl-cmd session)`
- L229: `(defun termint--rearrange-session-on-buffer-exit ()`
- L323: `(define-minor-mode termint-mode`
- L359: `(defun termint--send-string (string schema session)`
- L400: `(defun termint--show-source-command-hint (repl-name session original-content source-command)`
- L454: `(defun termint--dispatch-paragraph ()`
- L461: `(defun termint--dispatch-buffer ()`
- L465: `(defun termint--dispatch-defun ()`
- L479: `(defun termint--dispatch-region-and-send`
- L498: `(defun termint--hide-window (repl-name session)`
- L506: `(defun termint--create-source-command (str source-syntax)`
- L519: `(defmacro termint-define (repl-name repl-cmd &rest args)`
- L794: `(define-key map "s" #',start-func-name)`
- L795: `(define-key map "r" #',send-region-func-name)`
- L796: `(define-key map "R" #',source-region-func-name)`
- L797: `(define-key map "e" #',send-string-func-name)`
- L798: `(define-key map "h" #',hide-window-func-name)`
- L800: `(define-key map "r" #',send-region-operator-name)`
- L801: `(define-key map "R" #',source-region-operator-name))`
- L808: `(define-key map key command))))`
- L815: `(defun termint--delete-tmp-file (file)`
- L820: `(defun termint--delete-tmp-files ()`
- L826: `(defun termint--make-tmp-file (str &optional keep-file)`
- L869: `(provide 'termint)`
