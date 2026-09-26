# Indice del codice: tmux-view

Fonte: https://github.com/mgalgs/tmux-view.el.git

Revisione: `3f0339f568a68f128a678e684ebf351a0b647bd2`.


## tmux-view-test.el

- L29: `(require 'ert)`
- L30: `(require 'cl-lib)`
- L31: `(require 'tmux-view)`
- L41: `(defun tmux-view-test--mock-shell-command-to-string (command)`
- L52: `(defun tmux-view-test--with-mock-shell (thunk)`
- L184: `(provide 'tmux-view-test)`

## tmux-view.el

- L45: `(require 'ansi-color)`
- L57: `(defun tmux-view--truncate-string (str max-len)`
- L64: `(defun tmux-view--list-panes ()`
- L92: `(defun tmux-view--capture-pane (pane-id)`
- L101: `(defun tmux-view--create-buffer (session window pane pane-id)`
- L122: `(defun tmux-view--display (session window pane pane-id)`
- L131: `(defvar tmux-view-mode-map`
- L133: `(define-key map "g" #'tmux-view-refresh)`
- L134: `(define-key map "q" #'quit-window)`
- L135: `(define-key map "s" #'tmux-view-save)`
- L139: `(define-derived-mode tmux-view-mode special-mode "Tmux-View"`
- L150: `(defun tmux-view-refresh ()`
- L166: `(defun tmux-view-save ()`
- L176: `(defun tmux-view ()`
- L192: `(provide 'tmux-view)`
