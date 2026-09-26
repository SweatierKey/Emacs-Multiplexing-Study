# Indice del codice: eshell-z

Fonte: https://github.com/xuchunyang/eshell-z.git

Revisione: `337cb241e17bd472bd3677ff166a0800f684213c`.


## eshell-z-test.el

- L20: `(require 'ert)`
- L21: `(require 'eshell-z)`

## eshell-z.el

- L73: `(require 'cl-lib)`
- L74: `(require 'eshell)`
- L75: `(require 'em-dirs)`
- L76: `(require 'pcomplete)`
- L82: `(defcustom eshell-z-freq-dir-hash-table-file-name`
- L90: `(defcustom eshell-z-exclude-dirs '("/tmp/" "~/.emacs.d/elpa")`
- L95: `(defcustom eshell-z-change-dir-function`
- L112: `(defun eshell-z--now ()`
- L116: `(defun eshell-z--read-freq-dir-hash-table ()`
- L148: `(defun eshell-z--write-freq-dir-hash-table ()`
- L175: `(defun eshell-z--expand-directory-name (directory)`
- L179: `(defun eshell-z--directory-within-p (directory root)`
- L194: `(defun eshell-z--common-root (dirs)`
- L205: `(defun eshell-z--add ()`
- L240: `(defun eshell-z--remove ()`
- L256: `(defun eshell-z--frecent (value)`
- L267: `(defun eshell-z--rank (value)`
- L271: `(defun eshell-z--time (value)`
- L275: `(defun eshell-z--float-to-string (number)`
- L284: `(defun eshell-z--ensure-hash-table ()`
- L293: `(defun eshell-z--cd (value)`
- L298: `(defun eshell/z (&rest args)`
- L387: `(defun pcomplete/z ()`
- L403: `(defun eshell-z (dir)`
- L424: `(provide 'eshell-z)`
