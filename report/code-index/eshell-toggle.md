# Indice del codice: eshell-toggle

Fonte: https://github.com/4DA/eshell-toggle.git

Revisione: `04e501e02c475bd9067eebcf8807c951f2316194`.


## eshell-toggle.el

- L33: `(require 'project)`
- L34: `(require 'dash)`
- L35: `(require 'eshell)`
- L36: `(require 'esh-mode)`
- L37: `(require 'term)`
- L38: `(require 'subr-x)`
- L50: `(defcustom eshell-toggle-size-fraction`
- L56: `(defcustom eshell-toggle-window-side`
- L65: `(defcustom eshell-toggle-default-directory`
- L75: `(defcustom eshell-toggle-find-project-root-package`
- L86: `(defcustom eshell-toggle-name-separator`
- L92: `(defcustom eshell-toggle-init-term-char-mode`
- L99: `(defcustom eshell-toggle-run-command`
- L106: `(defcustom eshell-toggle-init-function`
- L112: `(defcustom eshell-toggle-use-git-root`
- L124: `(defun eshell-toggle-get-git-directory (dir)`
- L133: `(defun eshell-toggle--get-directory ()`
- L152: `(defun eshell-toggle--make-buffer-name ()`
- L167: `(defun eshell-toggle-init-eshell (dir buf-name)`
- L177: `(defun eshell-toggle--init-term (&optional input)`
- L187: `(defun eshell-toggle-init-ansi-term (dir buf-name)`
- L193: `(defun eshell-toggle-init-tmux (dir buf-name)`
- L198: `(defun eshell-toggle-init-shell(dir buf-name)`
- L206: `(defun eshell-toggle--window-size ()`
- L212: `(defun eshell-toggle--split-window ()`
- L219: `(defun eshell-toggle--new-buffer (buf-name)`
- L226: `(defun eshell-toggle (&optional keep-visible)`
- L251: `(define-key term-raw-map kb 'eshell-toggle)))`
- L253: `(provide 'eshell-toggle)`
