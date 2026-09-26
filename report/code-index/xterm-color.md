# Indice del codice: xterm-color

Fonte: https://github.com/atomontage/xterm-color.git

Revisione: `ffdad85e584dfc0857f2a1fb970f5ef0f5d31ba3`.


## xterm-color.el

- L82: `(require 'subr-x)`
- L83: `(require 'cl-lib)`
- L96: `(defcustom xterm-color-debug nil`
- L101: `(defcustom xterm-color-use-bold-for-bright nil`
- L106: `(defcustom xterm-color-names`
- L119: `(defcustom xterm-color-names-bright`
- L198: `(cl-defun xterm-color--string-properties (string)`
- L218: `(defun xterm-color--convert-text-properties-to-overlays (beg end)`
- L237: `(defun xterm-color--message (format-string &rest args)`
- L474: `(defmacro xterm-color--with-ANSI-macro-helpers (&rest body)`
- L592: `(defun xterm-color-filter-strip (string)`
- L655: `(defun xterm-color-filter (string)`
- L679: `(defun xterm-color-256 (color)`
- L711: `(cl-defun xterm-color-colorize-buffer (&optional use-overlays)`
- L732: `(defun xterm-color-clear-cache ()`
- L754: `(defmacro xterm-color--bench (path &optional repetitions)`
- L775: `(defun xterm-color--test-ansi ()`
- L860: `(defun xterm-color--test-xterm ()`
- L912: `(defun xterm-color-test ()`
- L935: `(defun xterm-color-test-raw ()`
- L950: `(provide 'xterm-color)`
