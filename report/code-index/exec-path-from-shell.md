# Indice del codice: exec-path-from-shell

Fonte: https://github.com/purcell/exec-path-from-shell.git

Revisione: `6146fdc16e9882df270be7e58ae8d628032d6bc4`.


## exec-path-from-shell.el

- L78: `(require 'cl-lib)`
- L79: `(require 'json)`
- L86: `(defcustom exec-path-from-shell-variables`
- L92: `(defcustom exec-path-from-shell-warn-duration-millis 500`
- L96: `(defcustom exec-path-from-shell-shell-name nil`
- L108: `(defun exec-path-from-shell--double-quote (s)`
- L112: `(defun exec-path-from-shell--shell ()`
- L121: `(defcustom exec-path-from-shell-arguments`
- L134: `(defun exec-path-from-shell--debug (msg &rest args)`
- L139: `(defun exec-path-from-shell--nushell-p (shell)`
- L143: `(defun exec-path-from-shell--standard-shell-p (shell)`
- L147: `(defmacro exec-path-from-shell--warn-duration (&rest body)`
- L160: `(defun exec-path-from-shell-printf (str &optional args)`
- L196: `(defun exec-path-from-shell-getenvs--nushell (names)`
- L245: `(defun exec-path-from-shell-getenvs (names)`
- L271: `(defun exec-path-from-shell-getenv (name)`
- L278: `(defun exec-path-from-shell-setenv (name value)`
- L290: `(defun exec-path-from-shell-copy-envs (names)`
- L303: `(defun exec-path-from-shell-copy-env (name)`
- L313: `(defun exec-path-from-shell-initialize ()`
- L323: `(provide 'exec-path-from-shell)`
