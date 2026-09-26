# Indice del codice: tmux-cc

Fonte: https://github.com/wcy123/tmux-cc.git

Revisione: `7f493a8d7f15e16fdf47da44756e1212e438dc6b`.


## tmux-cc.el

- L27: `(require 'seq)`
- L28: `(require 'shell)`
- L45: `(defun tmux-cc--convert-keys(strings)`
- L59: `(defun tmux-cc--delete-process-on-exit()`
- L65: `(defun tmux-cc--maybe-start-shell-process ()`
- L74: `(defun tmux-cc--tmux-cmd (&rest args)`
- L88: `(defun tmux-cc-send-keys (strings)`
- L120: `(defun tmux-cc-send-region(begin end)`
- L127: `(defun tmux-cc--begining-of-line()`
- L136: `(defun tmux-cc--end-of-line()`
- L144: `(defun tmux-cc-send-current-line ()`
- L201: `(defun tmux-cc-set-target-window (target-window)`
- L205: `(defun tmux-cc-get-panel ()`
- L222: `(defun tmux-cc-clear ()`
- L227: `(defun tmux-cc-run-single-command (command)`
- L237: `(defun tmux-cc-bind-command (command &rest args)`
- L242: `(defun convert-key (key)`
- L267: `(defun tmux-start-special-key ()`
- L284: `(defun tmux-cc-send-keys-from-a-file (file)`
- L297: `(defun tmux-cc-send-a-key (key)`
- L301: `(defvar tmux-cc-key-map`
- L304: `(define-key map (kbd "C-b") 'tmux-start-special-key)`
- L305: `(define-key map (kbd "g") 'tmux-cc-get-panel)`
- L306: `(define-key map (kbd "C-l") 'tmux-cc-clear)`
- L307: `(define-key map "%"	      (tmux-cc-bind-command "split-window" "-h"))`
- L308: `(define-key map "0"	      (tmux-cc-bind-command "select-window" "-t"  ":=0"))`
- L309: `(define-key map "1"	      (tmux-cc-bind-command "select-window" "-t"  ":=1"))`
- L310: `(define-key map "2"	      (tmux-cc-bind-command "select-window" "-t"  ":=2"))`
- L311: `(define-key map "3"	      (tmux-cc-bind-command "select-window" "-t"  ":=3"))`
- L312: `(define-key map "4"	      (tmux-cc-bind-command "select-window" "-t"  ":=4"))`
- L313: `(define-key map "5"	      (tmux-cc-bind-command "select-window" "-t"  ":=5"))`
- L314: `(define-key map "6"	      (tmux-cc-bind-command "select-window" "-t"  ":=6"))`
- L315: `(define-key map "7"	      (tmux-cc-bind-command "select-window" "-t"  ":=7"))`
- L316: `(define-key map "8"	      (tmux-cc-bind-command "select-window" "-t"  ":=8"))`
- L317: `(define-key map "9"	      (tmux-cc-bind-command "select-window" "-t"  ":=9"))`
- L318: `(define-key map "c"	      (tmux-cc-bind-command "new-window"))`
- L319: `(define-key map "o"	      (tmux-cc-bind-command "last-pane" "-t" ":.+"))`
- L320: `(define-key map "l"	      (tmux-cc-bind-command "last-window"))`
- L321: `(define-key map "z"	      (tmux-cc-bind-command "resize-pane" "-Z"))`
- L322: `(define-key map "q"	      #'tmux-cc-send-a-key)`
- L323: `(define-key map (kbd "C-c")	      (tmux-cc-bind-command "send-key"`
- L327: `(provide 'tmux-cc)`
