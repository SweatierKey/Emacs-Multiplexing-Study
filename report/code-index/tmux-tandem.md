# Indice del codice: tmux-tandem

Fonte: https://github.com/alberti42/emacs-tmux-tandem.git

Revisione: `82c1e8e4c15ef9576f1472d8b4e387c4b1e96c3a`.


## tmux-tandem.el

- L84: `(require 'cl-lib)`
- L85: `(require 'filenotify)`
- L91: `(defcustom tmux-tandem-cache-subdir "tmux-tandem"`
- L95: `(defcustom tmux-tandem-watch-events '(change)`
- L99: `(defcustom tmux-tandem-stack-option "@emacs_openfile_stack"`
- L115: `(defun tmux-tandem--string-empty-p (s)`
- L119: `(defun tmux-tandem--xdg-cache-home ()`
- L126: `(defun tmux-tandem--cache-dir ()`
- L132: `(defun tmux-tandem--make-cmdfile (window-id pane-id)`
- L150: `(defun tmux-tandem--tmux (&rest args)`
- L158: `(defun tmux-tandem--stack-read (win)`
- L168: `(defun tmux-tandem--stack-write (win entries)`
- L178: `(defun tmux-tandem--lookup-tty (tty)`
- L191: `(defun tmux-tandem--frame-tty (frame)`
- L200: `(defun tmux-tandem--open-spec (spec)`
- L226: `(defun tmux-tandem--read-file (path)`
- L234: `(defun tmux-tandem--pane-for-frame (frame)`
- L240: `(defun tmux-tandem--install-watch (pane cmdfile)`
- L260: `(defun tmux-tandem--deregister-all ()`
- L279: `(defun tmux-tandem--deregister-frame (frame)`
- L297: `(defun tmux-tandem--register-frame ()`
- L317: `(defun tmux-tandem-enable ()`
- L332: `(defun tmux-tandem-disable ()`
- L347: `(provide 'tmux-tandem)`
