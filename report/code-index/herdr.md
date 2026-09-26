# Indice del codice: herdr

Fonte: https://github.com/eddof13/herdr.el.git

Revisione: `6500aa6e272aaf125111150a62dd12c7644f1825`.


## herdr-agents.el

- L22: `(require 'subr-x)`
- L23: `(require 'herdr-state)`
- L24: `(require 'herdr-cmd)`
- L26: `(defcustom herdr-notify-statuses nil`
- L32: `(defcustom herdr-agents-buffer-name "*herdr-agents*"`
- L43: `(defun herdr-agents--counts (state)`
- L52: `(defun herdr-agents--segment (state)`
- L74: `(defun herdr-agents--refresh-segment (&rest _)`
- L86: `(define-key map [mode-line mouse-1]`
- L91: `(defun herdr-agents--ensure-global-mode-string ()`
- L111: `(define-minor-mode herdr-agents-mode-line-mode`
- L131: `(defun herdr-agents--notify (title body)`
- L139: `(defun herdr-agents--maybe-notify (&rest _)`
- L155: `(defvar herdr-agents-mode-map`
- L157: `(define-key map (kbd "RET") #'herdr-agents-visit)`
- L158: `(define-key map "p" #'herdr-agents-prompt)`
- L159: `(define-key map "r" #'herdr-agents-read)`
- L160: `(define-key map "g" #'herdr-agents-refresh)`
- L161: `(define-key map "q" #'quit-window)`
- L165: `(define-derived-mode herdr-agents-mode special-mode "herdr-agents"`
- L170: `(defun herdr-agents--pane-at-point ()`
- L175: `(defun herdr-agents-visit ()`
- L184: `(defun herdr-agents-prompt ()`
- L189: `(defun herdr-agents-read ()`
- L194: `(defun herdr-agents--insert-tree (state)`
- L219: `(defun herdr-agents-refresh ()`
- L232: `(defun herdr-agents ()`
- L242: `(defun herdr-agents--refresh-hook (&rest _)`
- L250: `(provide 'herdr-agents)`

## herdr-call.el

- L21: `(require 'subr-x)`
- L22: `(require 'herdr-rpc)`
- L23: `(require 'herdr-schema)`
- L24: `(require 'herdr-state)`
- L25: `(require 'herdr-select)`
- L27: `(defun herdr-call--annotate (method)`
- L34: `(defun herdr-call--read-method ()`
- L44: `(defun herdr-call--read-value (method name)`
- L54: `(defun herdr-call (&optional method)`
- L73: `(defun herdr-call--display (method result)`
- L89: `(provide 'herdr-call)`

## herdr-cmd.el

- L25: `(require 'subr-x)`
- L26: `(require 'ansi-color)`
- L27: `(require 'herdr-rpc)`
- L28: `(require 'herdr-state)`
- L29: `(require 'herdr-select)`
- L30: `(require 'herdr-term)`
- L71: `(defcustom herdr-adopt-created-shells t`
- L86: `(defun herdr-cmd--current-pane-id ()`
- L91: `(defun herdr-cmd--created-pane-id (result)`
- L98: `(defun herdr-cmd--follow-new-pane (pane-id)`
- L123: `(defun herdr-cmd--select-pane-when-ready (pane-id)`
- L134: `(defun herdr-cmd--read-source (&optional prompt)`
- L145: `(defun herdr-pane-split-right (&optional target)`
- L155: `(defun herdr-pane-split-down (&optional target)`
- L165: `(defun herdr-pane-close (&optional pane-id)`
- L178: `(defun herdr-pane-zoom (&optional pane-id)`
- L185: `(defun herdr-pane-resize (direction &optional amount pane-id)`
- L195: `(defun herdr-pane-swap (direction &optional pane-id)`
- L203: `(defun herdr-pane-rename (label &optional pane-id)`
- L210: `(defun herdr-pane-focus (&optional pane-id)`
- L223: `(defun herdr-cmd--follow-focus ()`
- L234: `(defun herdr-cmd--offer-to-adopt (pane-id)`
- L252: `(defun herdr-cmd-read-text (result)`
- L262: `(defun herdr-cmd-read-truncated-p (result)`
- L271: `(defun herdr-cmd--display-read (name result)`
- L289: `(defun herdr-pane-read (&optional pane-id source lines)`
- L302: `(defun herdr-pane-send-text (text &optional pane-id)`
- L309: `(defun herdr-pane-run (command &optional pane-id)`
- L318: `(defun herdr-pane-wait-for-output (pattern &optional pane-id timeout)`
- L338: `(defun herdr-tab-create (&optional label)`
- L347: `(defun herdr-tab-close (&optional tab-id)`
- L353: `(defun herdr-tab-focus (&optional tab-id)`
- L361: `(defun herdr-tab-rename (label &optional tab-id)`
- L370: `(defun herdr-workspace-create (cwd &optional label)`
- L381: `(defun herdr-workspace-close (&optional workspace-id)`
- L411: `(defun herdr-workspace-focus (&optional workspace-id)`
- L419: `(defun herdr-workspace-rename (label &optional workspace-id)`
- L429: `(defun herdr-worktree-list ()`
- L442: `(defun herdr-worktree-create (branch &optional base)`
- L454: `(defun herdr-worktree-open (branch)`
- L462: `(defun herdr-worktree-remove (&optional workspace-id force)`
- L476: `(defcustom herdr-agent-kinds`
- L488: `(defun herdr-agent-prompt (text &optional target)`
- L495: `(defun herdr-agent-read (&optional target source lines)`
- L508: `(defun herdr-agent-wait (&optional target until timeout)`
- L526: `(defun herdr-cmd--split-new-shell ()`
- L540: `(defun herdr-agent-start (name kind &optional pane-id)`
- L568: `(defun herdr-agent-explain (&optional target)`
- L576: `(defun herdr-agent-focus (&optional target)`
- L591: `(defun herdr-adopt-shell (&optional pane-id)`
- L618: `(defun herdr-promote-shell (&optional pane-id)`
- L638: `(defun herdr-release-shell (&optional pane-id)`
- L658: `(defun herdr-notification-show (title &optional body)`
- L666: `(provide 'herdr-cmd)`

## herdr-rpc.el

- L27: `(require 'json)`
- L28: `(require 'subr-x)`
- L29: `(require 'cl-lib)`
- L36: `(defcustom herdr-socket-path "~/.config/herdr/herdr.sock"`
- L41: `(defcustom herdr-executable "herdr"`
- L46: `(defcustom herdr-rpc-timeout 10.0`
- L53: `(defun herdr-error-code (err)`
- L57: `(defun herdr-error-message (err)`
- L61: `(defun herdr-rpc--signal (code message)`
- L68: `(defun herdr-rpc--next-id ()`
- L72: `(defun herdr-rpc--params-object (params)`
- L86: `(defun herdr-rpc-array (items)`
- L95: `(defun herdr-rpc-encode (id method params)`
- L103: `(defun herdr-rpc-decode (line)`
- L109: `(defun herdr-rpc-connect (name filter sentinel)`
- L125: `(defun herdr-rpc--result (payload)`
- L132: `(defun herdr-rpc-call (method &optional params)`
- L161: `(defun herdr-rpc-call-async (method params callback)`
- L195: `(provide 'herdr-rpc)`

## herdr-schema.el

- L26: `(require 'json)`
- L27: `(require 'subr-x)`
- L28: `(require 'herdr-rpc)`
- L30: `(defcustom herdr-schema-cache-file`
- L44: `(defun herdr-schema-load-file (path)`
- L52: `(defun herdr-schema--fetch ()`
- L66: `(defun herdr-schema--server-version ()`
- L70: `(defun herdr-schema ()`
- L90: `(defun herdr-schema--request ()`
- L95: `(defun herdr-schema--defs ()`
- L99: `(defun herdr-schema-resolve (node)`
- L116: `(defun herdr-schema--entry (method)`
- L125: `(defun herdr-schema-methods ()`
- L132: `(defun herdr-schema--params-def (method)`
- L138: `(defun herdr-schema-params (method)`
- L144: `(defun herdr-schema-required (method)`
- L148: `(defun herdr-schema-param (method name)`
- L153: `(defun herdr-schema-enum (method name)`
- L157: `(defun herdr-schema-param-type (method name)`
- L172: `(defun herdr-schema--type-symbol (type)`
- L185: `(defun herdr-schema-read-param (method name)`
- L207: `(provide 'herdr-schema)`

## herdr-select.el

- L26: `(require 'subr-x)`
- L27: `(require 'herdr-state)`
- L28: `(require 'herdr-rpc)`
- L29: `(require 'herdr-term)`
- L37: `(defun herdr-select--status-glyph (status)`
- L46: `(defun herdr-select--annotate-pane (pane-id)`
- L64: `(defun herdr-select--annotate-workspace (workspace-id)`
- L76: `(defun herdr-select--annotate-tab (tab-id)`
- L87: `(defun herdr-select--read (prompt candidates category annotator)`
- L99: `(defun herdr-select-pane (&optional prompt)`
- L108: `(defun herdr-select-agent (&optional prompt)`
- L116: `(defun herdr-select--available-shell-ids (state)`
- L128: `(defun herdr-select-available-shell (&optional prompt)`
- L145: `(defun herdr-select-workspace (&optional prompt)`
- L153: `(defun herdr-select-tab (&optional prompt)`
- L161: `(defun herdr-select-current-target (&optional buffer)`
- L167: `(defun herdr-select-target-pane (&optional prompt)`
- L201: `(defun herdr-select--register-marginalia ()`
- L214: `(defvar herdr-select-pane-embark-map`
- L216: `(define-key map "f" #'herdr-pane-focus)`
- L217: `(define-key map "r" #'herdr-pane-read)`
- L218: `(define-key map "p" #'herdr-agent-prompt)`
- L219: `(define-key map "k" #'herdr-pane-close)`
- L220: `(define-key map "z" #'herdr-pane-zoom)`
- L229: `(defun herdr-select-panes-with-buffers ()`
- L239: `(defun herdr-select--consult-visit (pane-id)`
- L245: `(defun herdr-select--consult-source ()`
- L270: `(provide 'herdr-select)`

## herdr-state.el

- L36: `(require 'cl-lib)`
- L37: `(require 'subr-x)`
- L38: `(require 'herdr-rpc)`
- L40: `(defcustom herdr-state-reconnect-min 1.0`
- L45: `(defcustom herdr-state-reconnect-max 30.0`
- L78: `(defun herdr-state-empty ()`
- L82: `(defun herdr-state-from-snapshot (snapshot)`
- L92: `(defun herdr-state-pane (state id)`
- L97: `(defcustom herdr-shell-agent-name "shell"`
- L108: `(defun herdr-state-shell-pane-p (pane)`
- L112: `(defun herdr-state-attachable (state)`
- L118: `(defun herdr-state-agents (state)`
- L124: `(defun herdr-state-pane-directory (pane)`
- L136: `(defun herdr-state--normalize-dir (path)`
- L141: `(defun herdr-state-workspace-for-directory (state directory)`
- L169: `(defun herdr-state-pane-ids (state)`
- L176: `(defun herdr-state--upsert (items key id new)`
- L187: `(defun herdr-state--remove (items key id)`
- L191: `(defun herdr-state--reorder-block (items key ids before)`
- L214: `(defun herdr-state--merge-pane (state pane-id changes)`
- L230: `(defun herdr-state-reduce (state kind data)`
- L336: `(defcustom herdr-state-prime-quiet 0.4`
- L348: `(defcustom herdr-state-ack-timeout 5.0`
- L374: `(defun herdr-state-current ()`
- L378: `(defun herdr-state--dispatch (kind data)`
- L383: `(defun herdr-state--apply-buffered-events ()`
- L392: `(defun herdr-state--handle-line (line)`
- L411: `(defun herdr-state--filter (proc chunk)`
- L422: `(defun herdr-state--close (proc)`
- L432: `(defun herdr-state--sentinel (proc _event)`
- L439: `(defun herdr-state--subscribe (name subscriptions)`
- L449: `(defun herdr-state--pane-subscriptions ()`
- L456: `(defun herdr-state--open-pane-stream ()`
- L465: `(defun herdr-state--resubscribe-panes ()`
- L474: `(defun herdr-state--refresh-statuses ()`
- L489: `(defun herdr-state--note-pane-set-change (kind _data)`
- L498: `(defun herdr-state--schedule-reconnect ()`
- L509: `(defun herdr-state--reconnect ()`
- L519: `(defun herdr-state--open-global-stream ()`
- L529: `(defun herdr-state--wait-for-ack (proc timeout)`
- L539: `(defun herdr-state--bootstrap ()`
- L560: `(defun herdr-state-detected-agent (pane-id)`
- L572: `(defun herdr-state-promote-shell-panes ()`
- L612: `(defun herdr-state--pane-differs-p (known fresh)`
- L618: `(defun herdr-state-reconcile-panes ()`
- L670: `(defun herdr-state-refresh ()`
- L684: `(defun herdr-state-resync ()`
- L694: `(defun herdr-state-start ()`
- L706: `(defun herdr-state-stop ()`
- L724: `(defun herdr-state-running-p ()`
- L728: `(provide 'herdr-state)`

## herdr-term.el

- L41: `(require 'cl-lib)`
- L42: `(require 'subr-x)`
- L43: `(require 'herdr-rpc)`
- L44: `(require 'herdr-state)`
- L49: `(defcustom herdr-terminal-backend 'session`
- L60: `(defcustom herdr-display-action`
- L80: `(defun herdr-term--show (buffer)`
- L84: `(defcustom herdr-server-start-timeout 15.0`
- L94: `(defun herdr-term-agent-buffer-name (pane)`
- L100: `(defun herdr-term-attach-args (pane-id takeover)`
- L105: `(defun herdr-term-session-args ()`
- L109: `(defun herdr-term-reconcile (state buffers)`
- L132: `(defun herdr-server-live-p ()`
- L138: `(defun herdr-term--bootstrap-server ()`
- L166: `(defun herdr-term--live-agent-buffers ()`
- L172: `(defun herdr-term-select-pane (pane-id)`
- L191: `(defun herdr-term--attach-if-possible (pane-id)`
- L198: `(defun herdr-term-select-focused ()`
- L207: `(defun herdr-term-buffer-for-pane (pane-id)`
- L213: `(defun herdr-term-pane-for-buffer (&optional buffer)`
- L226: `(defun herdr-term--attach (pane)`
- L237: `(defun herdr-term--attach-1 (pane pane-id)`
- L264: `(defun herdr-term--rename-stale-buffers ()`
- L278: `(defun herdr-term--sync-agent-windows ()`
- L294: `(defcustom herdr-term-track-directory t`
- L308: `(defcustom herdr-term-directory-interval 5.0`
- L322: `(defcustom herdr-term-directory-debounce 0.4`
- L332: `(defun herdr-term--poll-directories ()`
- L344: `(defun herdr-term--schedule-directory-poll ()`
- L355: `(defun herdr-term--start-directory-timer ()`
- L368: `(defun herdr-term--stop-directory-timer ()`
- L376: `(defun herdr-term--set-directory (buffer pane)`
- L384: `(defun herdr-term--sync-directories ()`
- L400: `(defun herdr-term--on-state-change (_kind _data)`
- L409: `(defun herdr-term-ensure ()`
- L432: `(defun herdr-term-display ()`
- L445: `(defun herdr-term-teardown ()`
- L458: `(provide 'herdr-term)`

## herdr-transient.el

- L19: `(require 'transient)`
- L20: `(require 'herdr-state)`
- L21: `(require 'herdr-term)`
- L22: `(require 'herdr-cmd)`
- L23: `(require 'herdr-select)`
- L24: `(require 'herdr-call)`
- L25: `(require 'herdr-agents)`
- L32: `(defun herdr-transient-tui-p ()`
- L54: `(defun herdr-transient--origin-buffer ()`
- L64: `(defun herdr-transient--target ()`
- L78: `(defun herdr-transient--heading ()`
- L174: `(defun herdr-transient-status ()`
- L189: `(provide 'herdr-transient)`

## herdr.el

- L29: `(require 'herdr-rpc)`
- L30: `(require 'herdr-state)`
- L31: `(require 'herdr-term)`
- L32: `(require 'herdr-cmd)`
- L33: `(require 'herdr-agents)`
- L38: `(defcustom herdr-protocol-version 22`
- L47: `(defun herdr--check-protocol ()`
- L60: `(defun herdr-start ()`
- L72: `(defun herdr-stop ()`
- L80: `(defun herdr-project ()`
- L100: `(defun herdr ()`
- L112: `(require 'herdr-transient)`
- L114: `(provide 'herdr)`
