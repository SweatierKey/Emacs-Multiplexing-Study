# Indice del codice: shell-command-x

Fonte: https://github.com/elizagamedev/shell-command-x.el.git

Revisione: `d2fe4d08be306d6570f3c316ea06b0e6931ea5d5`.


## shell-command-x.el

- L49: `(require 'cl-lib)`
- L50: `(require 'comint)`
- L51: `(require 'shell)`
- L52: `(require 'simple)`
- L58: `(defcustom shell-command-x-buffer-name-function`
- L69: `(defcustom shell-command-x-buffer-name-format "*shell:%n*"`
- L80: `(defcustom shell-command-x-buffer-name-async-format "*shell:%n*"`
- L91: `(defcustom shell-command-x-exit-hook`
- L119: `(defun shell-command-x-format-buffer-name (command async-p)`
- L163: `(defun shell-command-x-bob-exit-hook ()`
- L183: `(defun shell-command-x-bob-smart-exit-hook ()`
- L198: `(defun shell-command-x-emulate-special-mode-exit-hook ()`
- L214: `(defun shell-command-x--shell-command-advice`
- L261: `(defun shell-command-x--shell-command-sentinel-advice (process _)`
- L274: `(defun shell-command-x--comint-send-advice (&rest _)`
- L282: `(define-minor-mode shell-command-x-mode`
- L305: `(provide 'shell-command-x)`
