# Indice del codice: ghostherd

Fonte: https://github.com/ionrock/ghostherd.git

Revisione: `2a505e62512e97d2090d76a2ea004e10f86a6a3d`.


## lisp/ghostherd-client.el

- L39: `(require 'json)`
- L40: `(require 'cl-lib)`
- L47: `(defcustom ghostherd-herdr-program "herdr"`
- L51: `(defcustom ghostherd-socket-path nil`
- L58: `(defcustom ghostherd-session nil`
- L62: `(defcustom ghostherd-request-timeout 5.0`
- L66: `(defcustom ghostherd-herdr-auto-start t`
- L74: `(defcustom ghostherd-herdr-start-timeout 10.0`
- L83: `(defun ghostherd-client--config-dir ()`
- L90: `(defun ghostherd-client-socket-path ()`
- L106: `(defun ghostherd-client--connect (name filter sentinel path)`
- L118: `(defun ghostherd-client--start-herdr (path)`
- L149: `(defun ghostherd-client--open (name filter &optional sentinel)`
- L169: `(defun ghostherd-client--json-encode (object)`
- L174: `(defun ghostherd-client--json-parse (line)`
- L184: `(defun ghostherd-client-request (method &optional params)`
- L226: `(defun ghostherd-client-ping ()`
- L230: `(defun ghostherd-client-snapshot ()`
- L268: `(defun ghostherd-client--events-filter (_proc chunk)`
- L305: `(defun ghostherd-client--events-sentinel (_proc event)`
- L318: `(defun ghostherd-client--subscription-specs ()`
- L325: `(defun ghostherd-client-events-connect ()`
- L347: `(defun ghostherd-client-events-reconnect ()`
- L364: `(defun ghostherd-client-events-disconnect ()`
- L371: `(provide 'ghostherd-client)`

## lisp/ghostherd-notify.el

- L21: `(require 'ghostherd)`
- L23: `(defcustom ghostherd-notify-function #'ghostherd-notify-message`
- L31: `(defcustom ghostherd-notify-statuses '("blocked" "done")`
- L49: `(defun ghostherd-notify--face (status)`
- L59: `(defun ghostherd-notify--pane-desc (pane)`
- L68: `(defun ghostherd-notify-message (pane status)`
- L81: `(defun ghostherd-notify--pane-visible-p (pane-id)`
- L87: `(defun ghostherd-notify--on-event (name data)`
- L121: `(defun ghostherd-notify--counts ()`
- L132: `(defvar ghostherd-notify-lighter-map`
- L134: `(define-key map [mode-line mouse-1] #'ghostherd-sidebar-toggle)`
- L139: `(defun ghostherd-notify--update-lighter ()`
- L169: `(define-minor-mode ghostherd-notify-mode`
- L202: `(provide 'ghostherd-notify)`

## lisp/ghostherd-sidebar.el

- L27: `(require 'ghostherd)`
- L28: `(require 'ghostherd-notify)                   ; faces`
- L30: `(defcustom ghostherd-sidebar-buffer-name "*ghostherd*"`
- L35: `(defcustom ghostherd-sidebar-width 34`
- L40: `(defcustom ghostherd-sidebar-side 'left`
- L45: `(defcustom ghostherd-sidebar-refresh-interval 2.0`
- L63: `(defun ghostherd-sidebar--forget-frame (frame)`
- L71: `(defun ghostherd-sidebar--status-glyph (status)`
- L82: `(defun ghostherd-sidebar--insert-space (w)`
- L113: `(defun ghostherd-sidebar--render ()`
- L129: `(defun ghostherd-sidebar--tab-at-point ()`
- L132: `(defun ghostherd-sidebar--space-at-point ()`
- L137: `(defun ghostherd-sidebar--visible-p ()`
- L142: `(defun ghostherd-sidebar--stop-refresh-timer ()`
- L149: `(defun ghostherd-sidebar--refresh-tick ()`
- L162: `(defun ghostherd-sidebar--start-refresh-timer ()`
- L174: `(defun ghostherd-sidebar--tab-candidates ()`
- L191: `(defun ghostherd-sidebar--read-layout-tabs ()`
- L203: `(defun ghostherd-sidebar--prepare-buffer ()`
- L213: `(defun ghostherd-sidebar--display-window ()`
- L221: `(defun ghostherd-sidebar--main-leaf-window (frame)`
- L228: `(defun ghostherd-sidebar--install-terminal-windows (main buffers)`
- L244: `(defun ghostherd-sidebar-layout (tab-ids)`
- L275: `(defun ghostherd-sidebar-restore-layout ()`
- L289: `(defun ghostherd-sidebar-visit ()`
- L299: `(defun ghostherd-sidebar-toggle-fold ()`
- L308: `(defun ghostherd-sidebar-new-tab ()`
- L316: `(defun ghostherd-sidebar-new-space ()`
- L321: `(defun ghostherd-sidebar-close ()`
- L328: `(defun ghostherd-sidebar-rename ()`
- L338: `(defun ghostherd-sidebar-refresh ()`
- L343: `(defvar ghostherd-sidebar-mode-map`
- L345: `(define-key map (kbd "RET") #'ghostherd-sidebar-visit)`
- L346: `(define-key map (kbd "TAB") #'ghostherd-sidebar-toggle-fold)`
- L347: `(define-key map (kbd "c") #'ghostherd-sidebar-new-tab)`
- L348: `(define-key map (kbd "C") #'ghostherd-sidebar-new-space)`
- L349: `(define-key map (kbd "k") #'ghostherd-sidebar-close)`
- L350: `(define-key map (kbd "r") #'ghostherd-sidebar-rename)`
- L351: `(define-key map (kbd "b") #'ghostherd-next-blocked)`
- L352: `(define-key map (kbd "g") #'ghostherd-sidebar-refresh)`
- L353: `(define-key map (kbd "l") #'ghostherd-sidebar-layout)`
- L354: `(define-key map (kbd "L") #'ghostherd-sidebar-restore-layout)`
- L355: `(define-key map (kbd "n") #'next-line)`
- L356: `(define-key map (kbd "p") #'previous-line)`
- L360: `(define-derived-mode ghostherd-sidebar-mode special-mode "ghostherd"`
- L369: `(defun ghostherd-sidebar-open ()`
- L378: `(defun ghostherd-sidebar-toggle ()`
- L391: `(define-key ghostherd-command-map (kbd "w") #'ghostherd-sidebar-toggle)`
- L393: `(provide 'ghostherd-sidebar)`

## lisp/ghostherd.el

- L26: `(require 'ghostherd-client)`
- L27: `(require 'cl-lib)`
- L28: `(require 'subr-x)`
- L29: `(require 'project)`
- L35: `(defcustom ghostherd-attach-buffer-name-format "*herd:%s/%s*"`
- L64: `(defun ghostherd--schedule-resync ()`
- L95: `(defun ghostherd--cache-reset (snapshot)`
- L138: `(defun ghostherd--apply-event (name data)`
- L259: `(defun ghostherd--sync-pane-subscriptions ()`
- L285: `(defun ghostherd-connect ()`
- L300: `(defun ghostherd-disconnect ()`
- L309: `(defun ghostherd--on-subscribe-error (err)`
- L329: `(defun ghostherd-resync ()`
- L335: `(defun ghostherd--ensure ()`
- L344: `(defun ghostherd-spaces ()`
- L351: `(defun ghostherd-tabs (workspace-id)`
- L361: `(defun ghostherd-tab-pane (tab-id)`
- L382: `(defun ghostherd-current-space ()`
- L393: `(defun ghostherd--space-annotation (w)`
- L400: `(defun ghostherd--read-space (prompt)`
- L420: `(defun ghostherd--read-tab (prompt workspace-id)`
- L434: `(defun ghostherd--attach-buffer-name (workspace-id tab-id)`
- L442: `(defun ghostherd--find-attach-buffer (tab-id)`
- L452: `(defun ghostherd--attach (tab-id &optional display)`
- L482: `(defun ghostherd-detach ()`
- L492: `(defun ghostherd-switch-space (workspace-id)`
- L504: `(defun ghostherd-new-space (dir &optional label)`
- L534: `(defun ghostherd-switch-tab (tab-id)`
- L542: `(defun ghostherd-new-tab (&optional label)`
- L564: `(defun ghostherd--tabs-around (tab-id)`
- L576: `(defun ghostherd-next-tab ()`
- L583: `(defun ghostherd-previous-tab ()`
- L590: `(defun ghostherd-close-tab (tab-id)`
- L608: `(defun ghostherd-rename-tab (tab-id name)`
- L619: `(defun ghostherd-rename-space (workspace-id name)`
- L632: `(defun ghostherd-blocked-panes ()`
- L642: `(defun ghostherd-next-blocked ()`
- L655: `(defvar ghostherd-command-map`
- L657: `(define-key map (kbd "s") #'ghostherd-switch-space)`
- L658: `(define-key map (kbd "S") #'ghostherd-new-space)`
- L659: `(define-key map (kbd "t") #'ghostherd-switch-tab)`
- L660: `(define-key map (kbd "c") #'ghostherd-new-tab)`
- L661: `(define-key map (kbd "n") #'ghostherd-next-tab)`
- L662: `(define-key map (kbd "p") #'ghostherd-previous-tab)`
- L663: `(define-key map (kbd "b") #'ghostherd-next-blocked)`
- L664: `(define-key map (kbd "k") #'ghostherd-close-tab)`
- L665: `(define-key map (kbd "r") #'ghostherd-rename-tab)`
- L666: `(define-key map (kbd "R") #'ghostherd-rename-space)`
- L667: `(define-key map (kbd "g") #'ghostherd-resync)`
- L677: `(provide 'ghostherd)`
