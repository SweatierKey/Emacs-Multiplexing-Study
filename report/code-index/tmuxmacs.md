# Indice del codice: tmuxmacs

Fonte: https://github.com/andrewppar/tmuxmacs.git

Revisione: `e569afd48a7649607bd569af388c5311763fd935`.


## tmuxmacs-core.el

- L18: `(defun tmuxmacs-core--output (fields)`
- L25: `(defun tmuxmacs-core/execute (command &rest fields)`
- L37: `(defun tmuxmacs-core/pane-output (pane-id)`
- L41: `(defun tmuxmacs-core/entity-map ()`
- L46: `(defun tmuxmacs-core/lookup (key value)`
- L51: `(defun tmuxmacs-core/id-type (identifier)`
- L57: `(provide 'tmuxmacs-core)`

## tmuxmacs-face.el

- L25: `(provide 'tmuxmacs-face)`

## tmuxmacs-pane.el

- L16: `(require 'tmuxmacs-core)`
- L17: `(require 'tmuxmacs-window)`
- L18: `(require 'cl-lib)`
- L19: `(require 'subr-x)`
- L21: `(defun tmuxmacs-pane/list ()`
- L24: `(defun tmuxmacs-pane/focused ()`
- L27: `(defun tmuxmacs-pane/find (pane-id)`
- L32: `(defun tmuxmacs-pane/window (pane-id)`
- L41: `(defun tmuxmacs-pane/focus (pane-id)`
- L45: `(defun tmp--quote (item)`
- L48: `(defun tmp--parse-split (split)`
- L54: `(cl-defun tmuxmacs-pane/new (&key window split directory command)`
- L63: `(defun tmuxmacs-pane/send-command (pane-id command)`
- L68: `(defun tmuxmacs-pane/session (pane-id)`
- L71: `(defun tmuxmacs-pane/kill (pane-id)`
- L74: `(defun tmuxmacs-pane--pad-line (line-max line)`
- L81: `(cl-defun tmuxmacs-pane/tail (pane-id &key lines width)`
- L95: `(cl-defun tmuxmacs-pane/move (pane-id window-id &key horizontal?)`
- L100: `(provide 'tmuxmacs-pane)`

## tmuxmacs-session.el

- L16: `(require 'tmuxmacs-core)`
- L18: `(defun tmuxmacs-session--id (session-name)`
- L23: `(defun tmuxmacs-session--name (session-name)`
- L28: `(defun tmuxmacs-session/focus (session-id)`
- L31: `(defun tmuxmacs-session/focused ()`
- L36: `(defun tmuxmacs-session/new (&optional session-name)`
- L42: `(defun tmuxmacs-session/rename (session-id new-name)`
- L46: `(defun tmuxmacs-session/find (session-name-or-id)`
- L51: `(defun tmuxmacs-session/kill (session-id)`
- L54: `(provide 'tmuxmacs-session)`

## tmuxmacs-view.el

- L21: `(require 'cl-lib)`
- L22: `(require 'tmuxmacs-pane)`
- L23: `(require 'subr-x)`
- L24: `(require 'tmuxmacs-face)`
- L26: `(define-derived-mode tmuxmacs-mode fundamental-mode`
- L29: `(define-key tmuxmacs-mode-map`
- L32: `(defun tmv--plist-get-in (plist keys)`
- L42: `(defun tmv--plist-put-in (plist keys value)`
- L61: `(defun tmv--plist-update-in (plist keys function &rest args)`
- L69: `(defun tmv--add-item (lista item)`
- L78: `(defun tmv--pane-data->session-data (pane-data)`
- L95: `(defun tmv--plist-keys (plist)`
- L106: `(defmacro tmv--with-tmux-session-buffer (data &rest body)`
- L128: `(defun tmv--format-line (id name face)`
- L134: `(defun tmv--format-pane (pane-id session-data last? last-window?)`
- L142: `(defun tmv--format-window (session-id window-id session-data last?)`
- L154: `(defun tmv--format-session (session-id session-data)`
- L176: `(defun tmuxmacs-view/sessions ()`
- L203: `(defun tmv--line ()`
- L207: `(defun tmuxmacs-view/id-at-point ()`
- L211: `(defun tmuxmacs-view/type-at-point ()`
- L214: `(defun tmuxmacs-view/name-at-point ()`
- L219: `(defun tmuxmacs-view--selection (prompt name-key id-key)`
- L228: `(defun tmuxmacs-view/session-selection ()`
- L231: `(defun tmuxmacs-view/window-selection ()`
- L234: `(defun tmv--trim-line (line max-length)`
- L240: `(defun tmv--frame (lines)`
- L251: `(defun tmv--frame-start-line? (line)`
- L254: `(defun tmv--frame-end-line? (line)`
- L257: `(defun tmv--within-frame? ()`
- L276: `(defun tmv--show-pane-tail ()`
- L288: `(defun tmv--delete-frame ()`
- L302: `(defun tmv--pane-at-point? ()`
- L305: `(defun tmv--hide-pane-tail ()`
- L313: `(defun tmuxmacs-view/goto-id (id)`
- L322: `(defun tmuxmacs-view/pane-tail-showing? ()`
- L327: `(defun tmuxmacs-view/toggle-pane-tail ()`
- L335: `(defun tmuxmacs-view/pane-tail-refresh ()`
- L341: `(provide 'tmuxmacs-view)`

## tmuxmacs-window.el

- L16: `(require 'tmuxmacs-core)`
- L17: `(require 'tmuxmacs-session)`
- L18: `(require 'cl-lib)`
- L20: `(defun tmw--quote (item)`
- L23: `(defun tmuxmacs-window/list ()`
- L26: `(cl-defun tmuxmacs-window/new (&key session name directory command)`
- L49: `(defun tmuxmacs-window/session (window-id)`
- L52: `(defun tmuxmacs-window/focus (window-id)`
- L57: `(defun tmuxmacs-window/rename (window-id new-name)`
- L61: `(defun tmuxmacs-window/kill (window-id)`
- L64: `(defun tmuxmacs-window/move (window-id session-id)`
- L67: `(defun tmuxmacs-window/find (window-name-or-id)`
- L74: `(defun tmuxmacs-window/focused ()`
- L79: `(provide 'tmuxmacs-window)`

## tmuxmacs.el

- L21: `(require 'tmuxmacs-view)`
- L22: `(require 'tmuxmacs-session)`
- L23: `(require 'tmuxmacs-window)`
- L24: `(require 'tmuxmacs-pane)`
- L26: `(defmacro tmuxmacs--with-buffer-refresh (&rest body)`
- L31: `(defmacro tmuxmacs/save-excursion (&rest body)`
- L40: `(defun tmuxmacs ()`
- L44: `(defun tmuxmacs/focus ()`
- L50: `(defun tmuxmacs/rename ()`
- L64: `(defun tmuxmacs/new-session ()`
- L70: `(defun tmuxmacs--prompt (prompt)`
- L75: `(defun tmuxmacs/new-window ()`
- L86: `(defun tmuxmacs/kill ()`
- L100: `(defun tmuxmacs/send-command ()`
- L115: `(defun tmuxmacs/move-window ()`
- L124: `(defmacro tmuxmacs/save-excursion (&rest body)`
- L130: `(defun tmuxmacs/move-pane ()`
- L141: `(defun tmuxmacs/pane-tail ()`
- L145: `(defun tmuxmacs/pane-tail-refresh ()`
- L149: `(defun tmuxmacs--formatted-panes ()`
- L159: `(defun tmuxmacs/pane-send-command ()`
- L166: `(provide 'tmuxmacs)`
