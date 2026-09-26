# Indice del codice: helm-switch-shell

Fonte: https://github.com/jamesnvc/helm-switch-shell.git

Revisione: `8d7ba1d99ff12a8f1d6ce3b9684ae8aebf494cf3`.


## helm-switch-shell.el

- L37: `;; (global-set-key (kbd "<f3>") #'helm-switch-shell)`
- L73: `(require 'cl-lib)`
- L74: `(require 'helm)`
- L75: `(require 'helm-lib)`
- L76: `(require 'subr-x)`
- L84: `(defcustom helm-switch-shell-new-shell-type 'eshell`
- L91: `(defcustom helm-switch-shell-truncate-lines t`
- L96: `(defcustom helm-switch-shell-show-shell-indicator t`
- L125: `(defun helm-switch-shell--pwd-replace-home (directory)`
- L132: `(defun helm-switch-shell--candidate-name (buf)`
- L146: `(defun helm-switch-shell--new-shell ()`
- L150: `(defun helm-switch-shell--shell-select ()`
- L156: `(defun helm-switch-shell--create-new (&optional type)`
- L168: `(defun helm-switch-shell--get-candidates ()`
- L228: `(defun helm-switch-shell--move-to-first-real-candidate ()`
- L234: `(defun helm-switch-shell--open-split (splitf candidate)`
- L246: `(defun helm-switch-shell--horiz-split (candidate)`
- L250: `(defun helm-switch-shell--vert-split (candidate)`
- L254: `(defun helm-switch-shell--horiz-split-command ()`
- L260: `(defun helm-switch-shell--vert-split-command ()`
- L269: `(define-key map (kbd "C-s") #'helm-switch-shell--horiz-split-command)`
- L270: `(define-key map (kbd "C-v") #'helm-switch-shell--vert-split-command)`
- L329: `(defun helm-switch-shell ()`
- L342: `(provide 'helm-switch-shell)`
