# Indice del codice: emux

Fonte: https://github.com/re5et/emux.git

Revisione: `ab000ab78fb6a96b00ac8332575871a31f6f9548`.


## emux-base.el

- L40: `(defcustom emux-completing-read-command`
- L46: `(define-minor-mode emux-mode`
- L55: `(defun emux-set (property value)`
- L59: `(defun emux-get (property)`
- L63: `(defun emux-completing-read (prompt collection)`
- L70: `(defun emux-mode-map-bind (alist)`
- L74: `(define-key emux-mode-map (read-kbd-macro (car pair)) (cdr pair)))`
- L77: `(defun emux-flatten (x)`
- L83: `(provide 'emux-base)`

## emux-screen.el

- L36: `(require 'cl)`
- L37: `(require 'emux-base)`
- L38: `(require 'emux-term)`
- L40: `(defcustom emux-mode-emux-screen-bind-key-alist`
- L53: `(defun emux-screens ()`
- L57: `(defun emux-screen-get (property &optional screen)`
- L64: `(defun emux-screen-set (property value &optional screen)`
- L71: `(defun emux-screen-create (&optional properties terminal-name terminal-command)`
- L95: `(defun emux-screen-current (&optional screen)`
- L102: `(defun emux-screen-rename (name &optional screen)`
- L108: `(defun emux-screen-switch (&optional screen)`
- L137: `(defun emux-screen-from-name (name)`
- L145: `(defun emux-screen-destroy (&optional screen)`
- L156: `(defun emux-screen-save-current ()`
- L170: `(provide 'emux-screen)`

## emux-session.el

- L36: `(require 'emux-screen)`
- L38: `(defcustom emux-default-session`
- L44: `(defcustom emux-mode-emux-session-bind-key-alist`
- L57: `(defun emux-sessions ()`
- L60: `(defun emux-session-create (&optional properties)`
- L73: `(defun emux-filter (condp lst)`
- L77: `(defun emux-session-get (property &optional session)`
- L83: `(defun emux-session-set (property value &optional session)`
- L87: `(defun emux-session-current (&optional session)`
- L92: `(defun emux-session-switch (&optional session)`
- L105: `(defun emux-session-from-name (name)`
- L113: `(defun emux-session-set-default-directory (path)`
- L117: `(defun emux-session-destroy (&optional session)`
- L128: `(defun emux-session-buffer-name (&optional buffer session)`
- L136: `(defun emux-session-name-buffer (&optional form)`
- L182: `(defun emux-session-buffers (&optional session)`
- L188: `(defun emux-session-global-buffers ()`
- L195: `(defun emux-session-jump-to-global-buffer ()`
- L219: `(defun emux-session-jump-to-session-buffer ()`
- L236: `(defmacro emux-session-define-template (name &rest body)`
- L243: `(defun emux-session-load-template ()`
- L270: `(provide 'emux-session)`

## emux-term.el

- L36: `(require 'emux-base)`
- L39: `(defcustom emux-term-program`
- L45: `(defcustom emux-term-command-line-unbind-key-list`
- L51: `(defcustom emux-term-command-line-bind-key-alist`
- L66: `(defcustom emux-mode-emux-term-bind-key-alist`
- L90: `(defun emux-term-create (&optional name command)`
- L106: `(defun emux-term-handle-close ()`
- L114: `(defun emux-term-setup-keys ()`
- L120: `(define-key term-raw-map unbind-key nil))`
- L128: `(define-key term-raw-map bind-key bind-command)))`
- L130: `(defun emux-term-rename (name)`
- L135: `(defun emux-term-split-and-create (split-command &optional name command)`
- L142: `(defun emux-term-vsplit (&optional name command)`
- L148: `(defun emux-term-hsplit (&optional name command)`
- L154: `(defun emux-term-send-raw (string &optional buffer)`
- L163: `(defun emux-term-command (command &optional buffer)`
- L168: `(defun emux-term-previous-command ()`
- L173: `(defun emux-term-next-command ()`
- L178: `(defun emux-term-backward-word ()`
- L183: `(defun emux-term-forward-word ()`
- L188: `(defun emux-term-forward-kill-word ()`
- L193: `(defun emux-term-backward-kill-word ()`
- L198: `(defun emux-term-reverse-search-history ()`
- L203: `(defun emux-term-terminal-ring-yank ()`
- L208: `(defun emux-term-terminal-ring-yank-pop ()`
- L213: `(defun emux-term-emacs-ring-yank ()`
- L221: `(defun emux-term-emacs-ring-yank-pop ()`
- L230: `(defun emux-term-clear-previous-scrollback ()`
- L236: `(defun emux-term-focus-prompt ()`
- L244: `(defun emux-term-blur-prompt ()`
- L249: `(defun emux-term-destroy (&optional buffer)`
- L259: `(defun emux-term-cleanup (process state)`
- L262: `(defun emux-term-beginning-of-buffer ()`
- L267: `(defun emux-term-end-of-buffer ()`
- L271: `(defun emux-term-scroll-down-command ()`
- L276: `(defun emux-term-scroll-up-command ()`
- L282: `(defun emux-term-previous-line ()`
- L287: `(defun emux-term-next-line ()`
- L295: `(defun emux-term-keyboard-quit ()`
- L301: `(defun emux-lines-left ()`
- L309: `(provide 'emux-term)`
