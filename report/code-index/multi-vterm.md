# Indice del codice: multi-vterm

Fonte: https://github.com/suonlight/multi-vterm.git

Revisione: `36746d85870dac5aaee6b9af4aa1c3c0ef21a905`.


## multi-vterm.el

- L33: `(require 'cl-lib)`
- L34: `(require 'vterm)`
- L35: `(require 'project)`
- L41: `(defcustom multi-vterm-program nil`
- L47: `(defcustom multi-vterm-buffer-name "vterminal"`
- L52: `(defcustom multi-vterm-dedicated-window-height 30`
- L57: `(defcustom multi-vterm-dedicated-window-height-percent nil`
- L81: `(defun multi-vterm ()`
- L91: `(defun multi-vterm-project ()`
- L107: `(defun multi-vterm-dedicated-open ()`
- L124: `(defun multi-vterm-dedicated-close ()`
- L136: `(defun multi-vterm-dedicated-toggle ()`
- L144: `(defun multi-vterm-dedicated-select ()`
- L151: `(defun multi-vterm-get-buffer (&optional dedicated-window)`
- L173: `(defun multi-vterm-project-root ()`
- L182: `(defun multi-vterm-project-get-buffer-name ()`
- L186: `(defun multi-vterm-rename-buffer (name)`
- L191: `(defun multi-vterm-format-buffer-name (name)`
- L195: `(defun multi-vterm-format-buffer-index (index)`
- L199: `(defun multi-vterm-handle-close ()`
- L207: `(defun multi-vterm-next (&optional offset)`
- L213: `(defun multi-vterm-prev (&optional offset)`
- L219: `(defun multi-vterm-switch (direction offset)`
- L228: `(defun multi-vterm-internal ()`
- L233: `(defun multi-vterm-kill-buffer-hook ()`
- L240: `(defun multi-vterm-shell-name ()`
- L246: `(defun multi-vterm-dedicated-get-window ()`
- L253: `(defun multi-vterm-current-window-height (&optional window)`
- L260: `(defun multi-vterm-dedicated-calc-window-height ()`
- L272: `(defun multi-vterm-dedicated-get-buffer-name ()`
- L276: `(defun multi-vterm-dedicated-exist-p ()`
- L281: `(defun multi-vterm-window-exist-p (window)`
- L285: `(defun multi-vterm-buffer-exist-p (buffer)`
- L290: `(defun multi-vterm-switch-internal (direction offset)`
- L305: `(provide 'multi-vterm)`
