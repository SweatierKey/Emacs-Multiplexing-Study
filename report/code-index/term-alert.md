# Indice del codice: term-alert

Fonte: https://codeberg.org/calliecameron/term-alert.git

Revisione: `2236864975b9909e8499780a7fc4d92022c17b61`.


## term-alert-pkg.el


## term-alert.el

- L56: `;;     (define-key term-raw-map (kbd "C-#") 'term-alert-next-command-toggle)`
- L57: `;;     (define-key term-raw-map (kbd "M-#") 'term-alert-all-toggle)`
- L58: `;;     (define-key term-raw-map (kbd "C-'") 'term-alert-runtime)`
- L82: `(require 'term)`
- L83: `(require 'term-cmd)`
- L84: `(require 'alert)`
- L85: `(require 'f)`
- L86: `(require 'eat nil t)`
- L105: `(define-minor-mode term-alert-mode`
- L121: `(defun term-alert--set-count (number)`
- L132: `(defun term-alert-next-command-toggle (num)`
- L138: `(defun term-alert-all-toggle ()`
- L143: `(defun term-alert--get-runtime ()`
- L154: `(defun term-alert--get-message ()`
- L164: `(defun term-alert-runtime ()`
- L177: `(defun term-alert--started-callback ()`
- L183: `(defun term-alert--done-callback ()`
- L193: `(defun term-alert--default-alert ()`
- L200: `(defun term-alert--ensure-file (name)`
- L208: `(defmacro term-alert--install-command (command callback)`
- L215: `(defun term-alert--init ()`
- L228: `(provide 'term-alert)`
