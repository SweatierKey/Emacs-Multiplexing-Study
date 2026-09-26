# Indice del codice: ssh

Fonte: https://github.com/emacsmirror/ssh.git

Revisione: `812e27409d01c38d74906a1816640506d6e7e3ef`.


## ssh.el

- L42: `(require 'comint)`
- L43: `(require 'shell)`
- L50: `(defcustom ssh-program "ssh"`
- L55: `(defcustom ssh-explicit-args '()`
- L60: `(defcustom ssh-mode-hook nil`
- L65: `(defcustom ssh-process-connection-type t`
- L76: `(defcustom ssh-directory-tracking-mode 'local`
- L100: `(defcustom ssh-x-display-follow-current-frame t`
- L109: `(defcustom ssh-host nil`
- L114: `(defcustom ssh-remote-user nil`
- L123: `(defvar ssh-mode-map '())`
- L129: `(define-key ssh-mode-map "\C-c\C-c" 'ssh-send-Ctrl-C)`
- L130: `(define-key ssh-mode-map "\C-c\C-d" 'ssh-send-Ctrl-D)`
- L131: `(define-key ssh-mode-map "\C-c\C-z" 'ssh-send-Ctrl-Z)`
- L132: `(define-key ssh-mode-map "\C-c\C-\\" 'ssh-send-Ctrl-backslash)`
- L133: `(define-key ssh-mode-map "\C-d" 'ssh-delchar-or-send-Ctrl-D)`
- L134: `(define-key ssh-mode-map "\C-i" 'ssh-tab-or-complete)))`
- L143: `(defun ssh-hostname-at-point ()`
- L148: `(defun ssh (input-args &optional buffer)`
- L268: `(defun ssh-mode ()`
- L281: `(defun ssh-directory-tracking-mode (&optional prefix)`
- L336: `(defun ssh-with-check-display-override (fn)`
- L368: `(defun ssh-parse-words (line)`
- L393: `(defun ssh-carriage-filter (string)`
- L404: `(defun ssh-send-Ctrl-C ()`
- L408: `(defun ssh-send-Ctrl-D ()`
- L412: `(defun ssh-send-Ctrl-Z ()`
- L416: `(defun ssh-send-Ctrl-backslash ()`
- L420: `(defun ssh-delchar-or-send-Ctrl-D (arg)`
- L428: `(defun ssh-tab-or-complete ()`
- L435: `(provide 'ssh)`
