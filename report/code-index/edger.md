# Indice del codice: edger

Fonte: https://github.com/suderman/edger.git

Revisione: `d7af1643454e8d2025976f31531aee15d0224bb0`.


## emacs/edger.el

- L15: `(require 'windmove)`
- L16: `(require 'tab-bar)`
- L20: `(defcustom edger-executable`
- L26: `(defun edger--pane-context ()`
- L36: `(defun edger--cross (&rest args)`
- L57: `(defun edger--clear ()`
- L61: `(defun edger--navigate (direction)`
- L72: `(defun edger--resize (direction)`
- L87: `(defun edger-resize-left () "Resize left." (interactive) (edger--resize 'left))`
- L88: `(defun edger-resize-down () "Resize down." (interactive) (edger--resize 'down))`
- L89: `(defun edger-resize-up () "Resize up." (interactive) (edger--resize 'up))`
- L90: `(defun edger-resize-right () "Resize right." (interactive) (edger--resize 'right))`
- L92: `(defun edger-horizontal () "Split below and select the new window." (interactive)`
- L94: `(defun edger-vertical () "Split right and select the new window." (interactive)`
- L96: `(defun edger-close () "Close a window, then an editor tab, then its multiplexer pane."`
- L103: `(defun edger-left () "Navigate left." (interactive) (edger--navigate 'left))`
- L104: `(defun edger-down () "Navigate down." (interactive) (edger--navigate 'down))`
- L105: `(defun edger-up () "Navigate up." (interactive) (edger--navigate 'up))`
- L106: `(defun edger-right () "Navigate right." (interactive) (edger--navigate 'right))`
- L108: `(defvar edger-mode-map (make-sparse-keymap)`
- L112: `(define-minor-mode edger-mode`
- L117: `(defun edger-setup (&optional modifier horizontal vertical close)`
- L129: `(keymap-set edger-mode-map (format "%s-%s" modifier (nth 0 binding)) (nth 1 binding))`
- L130: `(keymap-set edger-mode-map`
- L138: `(keymap-set edger-mode-map (format "%s-%s" modifier (car binding)) (cdr binding)))`
- L143: `(provide 'edger)`
