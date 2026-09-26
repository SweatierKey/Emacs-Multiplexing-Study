# Indice del codice: emacs-tunnel

Fonte: https://github.com/mimunzar/emacs-tunnel.git

Revisione: `ace3afdf5d3c68a4acf43d07bf7054ab5b8108c4`.


## tslime-test.el

- L1: `(require 'tslime)`

## tslime.el

- L4: `(defun tslime-s-join (separator seq)`
- L7: `(defun tslime-re-matches (re s)`
- L11: `(defun tslime-append-newline-if-missing (s)`
- L14: `(defun tslime-paste-buffer-to-tmux-panel (f-shell buffer panel)`
- L18: `(defun tslime-send-to-tmux-panel (s conf)`
- L22: `(defun tslime-prompt-for-tmux-conf ()`
- L26: `(defun tslime-paste-buffer-to-screen-panel (f-shell buffer session region)`
- L30: `(defun tslime-send-to-screen-panel (s conf)`
- L34: `(defun tslime-parse-screen-session-list (s)`
- L38: `(defun tslime-prompt-for-screen-session ()`
- L42: `(defun tslime-prompt-for-screen-conf ()`
- L47: `(defun tslime-make-send-multiplexer (f-prompt-conf f-multiplexer-send)`
- L53: `(defun tslime-make-send-dispatch (f-send-screen f-send-tmux)`
- L67: `(defun tslime-send-region (multiplexer &optional forget)`
- L71: `(defun tslime-send (&optional forget)`
- L79: `(defun tslime-forget-send ()`
- L83: `(global-set-key (kbd "C-c C-c") #'tslime-send)`
- L84: `(global-set-key (kbd "C-c C-f") #'tslime-forget-send)`
- L86: `(provide 'tslime)`
