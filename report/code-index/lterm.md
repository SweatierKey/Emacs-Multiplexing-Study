# Indice del codice: lterm

Fonte: https://github.com/TaylanUB/lterm.git

Revisione: `734cb5bd91fff337cefd266c4e43a9ae306e4c51`.


## lterm-mud.el

- L27: `(require 'lterm)`
- L28: `(require 'format-spec)`
- L30: `(define-derived-mode lterm-mud-mode lterm-mode "Linewise-MUD"`
- L40: `(defun lterm-mud (host port)`
- L53: `(provide 'lterm-mud)`

## lterm-muds/lterm-mud-godwars2.el

- L1: `(defun godwars2 ()`
- L5: `(defun gw2-exec (cmd)`
- L8: `(defun gw2-combo (list)`

## lterm.el

- L48: `(require 'lui)`
- L50: `(require 'xterm-color)`
- L60: `(defcustom lterm-default-program nil`
- L64: `(defcustom lterm-default-prompt "> "`
- L68: `(defcustom lterm-echo-before-filters nil`
- L72: `(defcustom lterm-echo-after-filters nil`
- L78: `(defcustom lterm-convert-crlf t`
- L82: `(defcustom lterm-input-filters nil`
- L89: `(defcustom lterm-output-filters nil`
- L103: `(define-derived-mode lterm-mode lui-mode "Linewise-Term"`
- L115: `(defmacro with-lterm-conversions (&rest body)`
- L121: `(defun lterm-start-process (name program &rest program-args)`
- L130: `(defun lterm-start-network-connection (name host port)`
- L136: `(defun lterm (program)`
- L148: `(defun lnet (host port)`
- L160: `(defmacro lterm--filter (filters string)`
- L170: `(defun lterm-user-input-handler (string)`
- L210: `(defun lterm-process-output-handler (process string)`
- L235: `(defun lterm-process-output-line-handler (line)`
- L241: `(provide 'lterm)`
