# Indice del codice: tmux-pane

Fonte: https://github.com/laishulu/emacs-tmux-pane.git

Revisione: `0ab0d40b497e984a589189358e04e322b8165985`.


## tmux-pane.el

- L30: `(require 'subr-x)`
- L32: `(defcustom tmux-pane-vertical-percent 25`
- L37: `(defcustom tmux-pane-horizontal-percent 25`
- L48: `(defmacro tmux-pane--ensure-dir (&rest body)`
- L54: `(defun tmux-pane--windmove(dir flag)`
- L65: `(defun tmux-pane-open-vertical ()`
- L73: `(defun tmux-pane-open-horizontal ()`
- L81: `(defun tmux-pane-close ()`
- L88: `(defun tmux-pane-rerun ()`
- L96: `(defun tmux-pane-toggle-vertical()`
- L109: `(defun tmux-pane-toggle-horizontal()`
- L122: `(defun tmux-pane-omni-window-last ()`
- L128: `(defun tmux-pane-omni-window-up ()`
- L134: `(defun tmux-pane-omni-window-down ()`
- L140: `(defun tmux-pane-omni-window-left ()`
- L146: `(defun tmux-pane-omni-window-right ()`
- L151: `(defvar tmux-pane--override-map-enable nil`
- L154: `(defvar tmux-pane--override-keymap`
- L156: `(define-key map (kbd "C-\\") #'tmux-pane-omni-window-last)`
- L157: `(define-key map (kbd "C-k") #'tmux-pane-omni-window-up)`
- L158: `(define-key map (kbd "C-j") #'tmux-pane-omni-window-down)`
- L159: `(define-key map (kbd "C-h") #'tmux-pane-omni-window-left)`
- L160: `(define-key map (kbd "C-l") #'tmux-pane-omni-window-right)`
- L164: `(defvar tmux-pane--override-map-alist`
- L170: `(defvar tmux-pane--override-map-alist-order 0`
- L173: `(defun tmux-pane-in-tmux-p ()`
- L183: `(define-minor-mode tmux-pane-mode`
- L197: `(defun windmove-last ()`
- L206: `(provide 'tmux-pane)`
