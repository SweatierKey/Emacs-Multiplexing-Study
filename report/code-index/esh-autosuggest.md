# Indice del codice: esh-autosuggest

Fonte: https://github.com/dieggsy/esh-autosuggest.git

Revisione: `8f44a045cf7855893965f4430e2a2ccfa23312d5`.


## esh-autosuggest.el

- L35: `(require 'company)`
- L36: `(require 'cl-lib)`
- L38: `(require 'em-prompt)`
- L44: `(defcustom esh-autosuggest-delay 0`
- L49: `(defcustom esh-autosuggest-use-company-map nil`
- L58: `(defcustom esh-autosuggest-executables t`
- L63: `(defvar esh-autosuggest-active-map`
- L65: `(define-key keymap (kbd "<right>") 'company-complete-selection)`
- L66: `(define-key keymap (kbd "C-f") 'company-complete-selection)`
- L67: `(define-key keymap (kbd "M-<right>") 'esh-autosuggest-complete-word)`
- L68: `(define-key keymap (kbd "M-f") 'esh-autosuggest-complete-word)`
- L73: `(defun esh-autosuggest-candidates (prefix)`
- L97: `(defun esh-autosuggest-complete-word ()`
- L111: `(defun esh-autosuggest--prefix ()`
- L127: `(defun esh-autosuggest (command &optional arg &rest _ignored)`
- L138: `(define-minor-mode esh-autosuggest-mode`
- L177: `(provide 'esh-autosuggest)`
