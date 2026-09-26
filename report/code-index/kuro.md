# Indice del codice: kuro

Fonte: https://github.com/takeokunn/kuro.git

Revisione: `30a4ff96bdde62c789f42a443766632e8c379873`.


## emacs-lisp/core/kuro-config-logic.el

- L14: `(require 'subr-x)`
- L15: `(require 'kuro-config-macros)`
- L28: `(defvar kuro--keymap nil`
- L43: `(defun kuro--kuro-buffers ()`
- L66: `(defun kuro--set-shell (symbol value)`
- L94: `(defun kuro--set-font (symbol value)`
- L100: `(defun kuro--set-keymap-exceptions (symbol value)`
- L112: `(defun kuro--set-input-echo-delay (symbol value)`
- L123: `(defun kuro--validate-config ()`
- L140: `(defun kuro-validate-config ()`
- L151: `(provide 'kuro-config-logic)`

## emacs-lisp/core/kuro-config-macros.el

- L14: `(defmacro kuro--broadcast-to-buffers (fn &rest args)`
- L21: `(defmacro kuro--in-all-buffers (&rest body)`
- L27: `(defmacro kuro--with-mode (mode msg &rest body)`
- L34: `(defmacro kuro--with-kuro-mode (&rest body)`
- L38: `(defmacro kuro--check-positive-integer (var errors)`
- L43: `(defmacro kuro--check-positive-integer-symbol (var errors)`
- L50: `(defmacro kuro--check-positive-integer-vars (vars errors)`
- L55: `(defmacro kuro--check-optional-positive-integer-vars (vars errors)`
- L61: `(defmacro kuro--check-hex-color (var errors)`
- L70: `(defmacro kuro--def-positive-int-setter (name err-msg doc &rest body)`
- L84: `(provide 'kuro-config-macros)`

## emacs-lisp/core/kuro-config.el

- L15: `(require 'kuro-config-logic)`
- L16: `(require 'kuro-colors)`
- L42: `(defcustom kuro-module-binary-path nil`
- L67: `(defcustom kuro-keymap-exceptions`
- L89: `(defcustom kuro-shell (or (getenv "SHELL") "/bin/bash")`
- L98: `(defcustom kuro-shell-integration t`
- L104: `(defcustom kuro-scrollback-size 10000`
- L114: `(defcustom kuro-clipboard-policy 'write-only`
- L124: `(defcustom kuro-notifications-enabled t`
- L132: `(defcustom kuro-notification-function 'kuro--default-notify`
- L146: `(defcustom kuro-progress-enabled t`
- L156: `(defcustom kuro-progress-format " %s%d%% "`
- L165: `(defcustom kuro-progress-state-glyphs`
- L176: `(defcustom kuro-frame-rate 120`
- L187: `(defcustom kuro-tui-frame-rate 30`
- L212: `(defcustom kuro-streaming-latency-mode t`
- L220: `(defcustom kuro-kill-buffer-on-exit t`
- L226: `(defcustom kuro-typewriter-effect nil`
- L233: `(defcustom kuro-use-binary-ffi t`
- L253: `(defcustom kuro-typewriter-chars-per-second 120`
- L260: `(defcustom kuro-input-echo-delay 0.01`
- L274: `(defcustom kuro-font-family nil`
- L283: `(defcustom kuro-font-size nil`
- L305: `(provide 'kuro-config)`

## emacs-lisp/core/kuro-copy-macros.el

- L15: `(defmacro kuro--def-copy-window-move (name arg docstring)`
- L21: `(defmacro kuro--def-copy-search (name search-fn fallback-fn wrap-pos docstring)`
- L40: `(defmacro kuro--def-copy-goto-prompt (name direction fallback docstring)`
- L52: `(defmacro kuro--define-copy-mode-bindings (map bindings)`
- L58: `(define-key ,map`
- L62: `(defmacro kuro--def-copy-search-enter (name search-fn docstring)`
- L73: `(provide 'kuro-copy-macros)`

## emacs-lisp/core/kuro-copy.el

- L16: `(require 'cl-lib)`
- L17: `(require 'kuro-config)`
- L18: `(require 'kuro-ffi)`
- L19: `(require 'kuro-copy-macros)`
- L22: `(defvar kuro-mode-map)`
- L26: `(defvar kuro--emulation-mode-map-alist)`
- L56: `(defcustom kuro-copy-mode-auto-exit t`
- L63: `(defcustom kuro-copy-mode-hl-line t`
- L73: `(defun kuro--copy-clear-selection-state (&optional cancel-rect)`
- L80: `(defun kuro--copy-begin-selection (&optional linewise)`
- L90: `(defun kuro--copy-clear-selection-and-deactivate ()`
- L95: `(defun kuro--copy-mode-save-and-exit ()`
- L103: `(defun kuro--copy-finalize (&optional cancel-rect)`
- L109: `(defun kuro--copy-copy-region-and-exit ()`
- L142: `(defun kuro--copy-set-mark ()`
- L150: `(defun kuro--copy-set-mark-line ()`
- L160: `(defun kuro--copy-append-region ()`
- L179: `(defun kuro--copy-rectangle-toggle ()`
- L208: `(defun kuro--copy-search-word-forward ()`
- L220: `(defun kuro--prompt-overlay-positions ()`
- L230: `(defun kuro--copy-find-prompt (direction)`
- L284: `(defvar kuro--copy-mode-map`
- L294: `(defun kuro--enter-copy-mode ()`
- L317: `(defun kuro--exit-copy-mode ()`
- L335: `(defun kuro-copy-mode ()`
- L363: `(defun kuro-occur (regexp)`
- L374: `(provide 'kuro-copy)`

## emacs-lisp/core/kuro-keymap-macros.el

- L13: `(defmacro kuro--define-key-bindings (map bindings key-fn command-fn)`
- L28: `'(define-key ,map ,(funcall key-fn binding)`
- L32: `(defmacro kuro--bind-keys (map command &rest keys)`
- L41: `'(define-key ,map-sym ,key ,command-sym))`
- L44: `(defmacro kuro--define-keymap (&rest bindings)`
- L52: `'(define-key map ,(if (stringp key) '(kbd ,key) key)`
- L57: `(provide 'kuro-keymap-macros)`

## emacs-lisp/core/kuro-keymap.el

- L14: `(require 'kuro-keymap-macros)`
- L16: `(provide 'kuro-keymap)`

## emacs-lisp/core/kuro-lifecycle-commands-macros.el

- L12: `(defmacro kuro--def-control-key (name sequence doc)`
- L17: `(provide 'kuro-lifecycle-commands-macros)`

## emacs-lisp/core/kuro-lifecycle-commands.el

- L15: `(require 'seq)`
- L16: `(require 'kuro-faces-macros)`
- L17: `(require 'kuro-lifecycle-commands-macros)`
- L18: `(require 'kuro-lifecycle-module)`
- L61: `(defvar kuro--font-remap-cookie)`
- L64: `(defun kuro-create (&optional command buffer-name)`
- L86: `(defun kuro-send-string (string)`
- L94: `(defun kuro--most-recent-buffer ()`
- L103: `(defun kuro-send-region (start end)`
- L130: `(defun kuro--cleanup-render-state ()`
- L164: `(defun kuro-kill ()`
- L177: `(defun kuro--list-sessions-safe ()`
- L183: `(defun kuro--detached-sessions (sessions)`
- L188: `(defun kuro--session-candidates (sessions)`
- L196: `(defun kuro--read-attach-session-id ()`
- L211: `(defun kuro--attach-buffer (session-id)`
- L217: `(defun kuro-attach (session-id)`
- L236: `(provide 'kuro-lifecycle-commands)`

## emacs-lisp/core/kuro-lifecycle-macros.el

- L15: `(defmacro kuro--clear-session-state ()`
- L21: `(defmacro kuro--detach-and-clear-session-state (session-id)`
- L31: `(defmacro kuro--run-session-setup-fns ()`
- L37: `(provide 'kuro-lifecycle-macros)`

## emacs-lisp/core/kuro-lifecycle-module.el

- L14: `(require 'kuro-module)`
- L45: `(defun kuro--module-loadable-p ()`
- L51: `(defun kuro--try-load-module ()`
- L58: `(defun kuro--install-and-load-module (install-fn install-name)`
- L67: `(defun kuro--prompt-and-install-module ()`
- L81: `(defun kuro--ensure-module-installed ()`
- L90: `(provide 'kuro-lifecycle-module)`

## emacs-lisp/core/kuro-lifecycle.el

- L21: `(require 'kuro-ffi)`
- L22: `(require 'kuro-renderer)`
- L23: `(require 'kuro-faces)`
- L24: `(require 'kuro-render-buffer)`
- L25: `(require 'kuro-dnd)`
- L26: `(require 'kuro-compilation)`
- L27: `(require 'kuro-bookmark)`
- L28: `(require 'kuro-color-scheme)`
- L29: `(require 'kuro-sessions)`
- L30: `(require 'kuro-lifecycle-module)`
- L31: `(require 'kuro-lifecycle-macros)`
- L102: `(defvar kuro--font-remap-cookie nil`
- L156: `(defun kuro--shell-integration-dir ()`
- L170: `(defun kuro--setup-shell-integration-env ()`
- L182: `(defun kuro--terminal-dimensions ()`
- L187: `(defun kuro--session-buffer-name (session-id)`
- L191: `(defun kuro--show-buffer-if-interactive (buffer)`
- L197: `(defun kuro--create-session-buffer (&optional buffer-name)`
- L207: `(defun kuro--initialize-session-buffer (buffer rows cols)`
- L214: `(defun kuro--start-session-in-buffer (buffer command)`
- L243: `(defun kuro--do-attach (session-id rows cols)`
- L255: `(defun kuro--rollback-attach (session-id buffer err)`
- L263: `(defun kuro--teardown-session ()`
- L275: `(defun kuro--prefill-buffer (rows)`
- L286: `(defun kuro--schedule-initial-render (buf)`
- L310: `(defun kuro--init-session-buffer (buffer rows cols)`
- L324: `(require 'kuro-lifecycle-commands)`
- L326: `(provide 'kuro-lifecycle)`

## emacs-lisp/core/kuro-module-install.el

- L13: `(require 'cl-lib)`
- L14: `(require 'kuro-module-platform)`
- L15: `(require 'subr-x)`
- L16: `(require 'url)`
- L18: `(defun kuro-module--ensure-https-base-url (base-url)`
- L25: `(defcustom kuro-module-installation-method nil`
- L36: `(defcustom kuro-module-release-base-url`
- L57: `(defun kuro-module--parse-sha256 (value source)`
- L64: `(defun kuro-module--verify-sha256 (file expected-hash)`
- L76: `(defun kuro-module--target-path ()`
- L86: `(defun kuro-module--ensure-private-install-directory (dir)`
- L108: `(defun kuro-module--ensure-single-link-regular-file (file role)`
- L122: `(defun kuro-module--ensure-install-destination (file)`
- L136: `(defun kuro-module--copy-validated-module-file (source destination)`
- L152: `(defun kuro-module--shared-library-name ()`
- L156: `(defun kuro-module--installed-module-path (target-dir)`
- L160: `(defun kuro-module--release-spec (&optional version)`
- L178: `(defun kuro-module--http-response-body-start (source)`
- L187: `(defun kuro-module--http-response-body-string (source)`
- L192: `(defun kuro-module--fetch-sha256 (sha-url)`
- L204: `(defun kuro-module--write-http-body-to-file (buffer file source)`
- L212: `(defun kuro-module--download-release-archive (url sha-url tmp-file)`
- L228: `(defun kuro-module--archive-members (tar-bin archive)`
- L236: `(defun kuro-module--extract-archive-member (tar-bin archive destination member)`
- L243: `(defun kuro-module--validate-release-archive (tar-bin tmp-file)`
- L252: `(defun kuro-module--install-release-archive (tar-bin tmp-file target-dir)`
- L282: `(defun kuro-module-download (&optional version)`
- L310: `(defun kuro-module--locate-cargo-toml ()`
- L328: `(defun kuro-module--cargo-built-library-path (cargo-toml)`
- L334: `(defun kuro-module--install-built-library (built dest)`
- L343: `(defun kuro-module-build ()`
- L370: `(provide 'kuro-module-install)`

## emacs-lisp/core/kuro-module-macros.el

- L17: `(defmacro kuro--module-try (path-expr)`
- L23: `(defmacro kuro--run-module-search-tiers ()`
- L28: `(provide 'kuro-module-macros)`

## emacs-lisp/core/kuro-module-platform.el

- L16: `(defun kuro-module--platform-extension ()`
- L23: `(defun kuro-module--shared-extension ()`
- L28: `(defun kuro-module--platform-string (&optional system-type-override system-configuration-override)`
- L52: `(defun kuro-module--lib-name ()`
- L57: `(provide 'kuro-module-platform)`

## emacs-lisp/core/kuro-module.el

- L15: `(require 'cl-lib)`
- L16: `(require 'kuro-config)  ;; for kuro-module-binary-path defcustom`
- L17: `(require 'kuro-module-platform)`
- L18: `(require 'kuro-module-install)`
- L19: `(require 'kuro-module-macros)`
- L28: `(defun kuro-module--library-candidate-error (source path reason)`
- L33: `(defun kuro-module--library-candidate-from-path (path &optional required source)`
- L74: `(defun kuro-module--library-candidate-active-path (candidate)`
- L87: `(defun kuro-module--tier-custom ()`
- L93: `(defun kuro-module--tier-env ()`
- L101: `(defun kuro-module--tier-xdg ()`
- L105: `(defun kuro-module--tier-dev ()`
- L129: `(defun kuro-module--find-library ()`
- L138: `(defun kuro-module-load ()`
- L153: `(defun kuro--ensure-module-loaded ()`
- L163: `(provide 'kuro-module)`

## emacs-lisp/core/kuro-scrollback.el

- L14: `(require 'kuro-config)`
- L15: `(require 'kuro-keymap)`
- L25: `(defvar kuro--scrollback-edit-keymap`
- L32: `(define-derived-mode kuro-scrollback-edit-mode text-mode "Kuro-Edit"`
- L48: `(defun kuro-edit-scrollback ()`
- L76: `(defun kuro-scrollback-send ()`
- L94: `(defun kuro-scrollback-discard ()`
- L100: `(provide 'kuro-scrollback)`

## emacs-lisp/core/kuro.el

- L36: `(require 'kuro-module)`
- L37: `(require 'kuro-config)`
- L38: `(require 'kuro-ffi)`
- L39: `(require 'kuro-faces)`
- L40: `(require 'kuro-keymap)`
- L41: `(require 'kuro-scrollback)`
- L42: `(require 'kuro-overlays)`
- L43: `(require 'kuro-navigation)`
- L44: `(require 'kuro-input)`
- L47: `(require 'kuro-stream)`
- L48: `(require 'kuro-render-buffer)`
- L49: `(require 'kuro-renderer)`
- L50: `(require 'kuro-lifecycle)`
- L71: `(defvar kuro-mode-map`
- L93: `(require 'kuro-input-mode)`
- L94: `(require 'kuro-copy)`
- L96: `(defun kuro--window-size-change (frame)`
- L124: `(defun kuro--make-focus-change-fn (prev)`
- L135: `(define-derived-mode kuro-mode fundamental-mode "Kuro"`
- L211: `(provide 'kuro)`

## emacs-lisp/faces/kuro-colors-macros.el

- L13: `(defmacro kuro--defcolor (suffix default label index)`
- L23: `(provide 'kuro-colors-macros)`

## emacs-lisp/faces/kuro-colors.el

- L29: `(require 'kuro-colors-macros)`
- L81: `(defun kuro--rebuild-named-colors ()`
- L93: `(defun kuro--set-color (symbol value)`
- L122: `(provide 'kuro-colors)`

## emacs-lisp/faces/kuro-faces-attrs.el

- L20: `(require 'kuro-faces-color)`
- L82: `(defun kuro--decode-attrs (attr-flags)`
- L152: `(defun kuro--attrs-to-face-props (fg bg attr-flags underline-color)`
- L212: `(provide 'kuro-faces-attrs)`

## emacs-lisp/faces/kuro-faces-color.el

- L26: `(require 'kuro-colors)`
- L131: `(defmacro kuro--define-color-type-dispatch (color)`
- L139: `(defun kuro--color-to-emacs (color)`
- L149: `(defun kuro--indexed-to-emacs (idx)`
- L214: `(provide 'kuro-faces-color)`

## emacs-lisp/faces/kuro-faces-macros.el

- L13: `(defmacro kuro--with-face-remap (cookie-var &rest remap-body)`
- L27: `(provide 'kuro-faces-macros)`

## emacs-lisp/faces/kuro-faces.el

- L35: `(require 'cl-lib)`
- L36: `(require 'kuro-config)`
- L37: `(require 'kuro-ffi)`
- L38: `(require 'kuro-ffi-osc)`
- L39: `(require 'kuro-faces-color)`
- L40: `(require 'kuro-faces-attrs)`
- L41: `(require 'kuro-faces-macros)`
- L42: `(require 'kuro-char-width)`
- L80: `(defun kuro--apply-font-to-buffer (buf)`
- L98: `(defun kuro--make-face (fg bg flags underline-color)`
- L102: `(defun kuro--get-cached-face-raw--miss (fg-enc bg-enc flags ul-normalized)`
- L181: `(defun kuro--remap-default-face (fg-str bg-str)`
- L193: `(defun kuro--apply-default-colors ()`
- L212: `(defun kuro--apply-palette-entry (idx r g b)`
- L224: `(defun kuro--apply-palette-update-entry (entry)`
- L229: `(defun kuro--apply-palette-update-entries (entries)`
- L237: `(defun kuro--apply-palette-updates ()`
- L246: `(provide 'kuro-faces)`

## emacs-lisp/features/kuro-activity.el

- L35: `(require 'kuro-config)`
- L36: `(require 'kuro-poll-modes)`
- L37: `(require 'kuro-prompt-status)`
- L38: `(require 'kuro-keymap)`
- L39: `(require 'tabulated-list)`
- L50: `(defcustom kuro-activity-notify-threshold 10.0`
- L59: `(defcustom kuro-activity-notify-on-exit t`
- L66: `(defcustom kuro-activity-notify-on-bell t`
- L73: `(defcustom kuro-activity-bell-message "Bell"`
- L78: `(defcustom kuro-activity-log-max-length 200`
- L105: `(defun kuro--activity-notify (title body)`
- L129: `(defun kuro--activity-on-command-complete (exit-code duration-ms`
- L151: `(defun kuro--activity-bell-advice (&rest _args)`
- L160: `(defun kuro--activity-check-exit ()`
- L174: `(define-minor-mode kuro-activity-mode`
- L198: `(defun kuro-activity-list-delete-entry ()`
- L207: `(defvar kuro-activity-list-mode-map`
- L219: `(defun kuro-activity-list--entries ()`
- L228: `(defun kuro-activity-list--refresh ()`
- L233: `(define-derived-mode kuro-activity-list-mode tabulated-list-mode`
- L244: `(defun kuro-activity-list ()`
- L257: `(defun kuro-activity-clear ()`
- L269: `(provide 'kuro-activity)`

## emacs-lisp/features/kuro-bookmark.el

- L14: `(require 'bookmark)`
- L18: `(defun kuro-bookmark--string-has-control-character-p (value)`
- L22: `(defun kuro-bookmark--safe-directory (directory)`
- L31: `(defun kuro-bookmark--safe-buffer-name (name)`
- L38: `(defun kuro-bookmark-make-record ()`
- L52: `(defun kuro-bookmark-jump (bookmark)`
- L64: `(defun kuro--setup-bookmark ()`
- L68: `(provide 'kuro-bookmark)`

## emacs-lisp/features/kuro-char-width-macros.el

- L13: `(defmacro kuro--set-fontset-font-both (range spec)`
- L22: `(provide 'kuro-char-width-macros)`

## emacs-lisp/features/kuro-char-width.el

- L25: `(require 'seq)`
- L26: `(require 'kuro-char-width-macros)`
- L128: `(defun kuro--apply-char-width-overrides ()`
- L134: `(defun kuro--reapply-char-width-in-all-buffers ()`
- L148: `(defun kuro-char-width-setup ()`
- L156: `(defun kuro--assign-mono-fonts ()`
- L196: `(defun kuro--probe-glyph-metrics (probe-char)`
- L221: `(defun kuro--rescale-font-for-glyph (probe-char range cell-width cell-height)`
- L245: `(defun kuro--refine-glyph-widths ()`
- L293: `(defun kuro--setup-char-width-table ()`
- L316: `(defun kuro--detect-nerd-font ()`
- L327: `(defun kuro--setup-fontset ()`
- L342: `(provide 'kuro-char-width)`

## emacs-lisp/features/kuro-color-scheme.el

- L17: `(require 'cl-lib)`
- L18: `(require 'kuro-config)`
- L33: `(defcustom kuro-color-scheme-debounce-seconds 0.05`
- L48: `(defun kuro--color-scheme-luminance (hex-or-name)`
- L56: `(defun kuro--color-scheme-detect-dark-p (&optional frame)`
- L76: `(defun kuro--color-scheme-apply-now ()`
- L90: `(defun kuro--color-scheme-schedule (&rest _args)`
- L102: `(defun kuro-color-scheme-refresh ()`
- L111: `(defun kuro--color-scheme-install-hook ()`
- L128: `(defun kuro--color-scheme-uninstall-hook ()`
- L136: `(provide 'kuro-color-scheme)`

## emacs-lisp/features/kuro-compilation.el

- L14: `(require 'compile)`
- L16: `(defcustom kuro-compilation-navigation t`
- L23: `(defun kuro--setup-compilation ()`
- L30: `(defun kuro--teardown-compilation ()`
- L35: `(provide 'kuro-compilation)`

## emacs-lisp/features/kuro-debug-perf.el

- L26: `(require 'kuro-config)`
- L30: `(defcustom kuro-debug-perf nil`
- L48: `(defun kuro--perf-report (ffi-ms apply-ms cursor-ms total-ms dirty face-count)`
- L74: `(defvar kuro--col-to-buf-map)`
- L77: `(defun kuro-debug-state ()`
- L113: `(defun kuro-debug-line-widths ()`
- L142: `(provide 'kuro-debug-perf)`

## emacs-lisp/features/kuro-dnd.el

- L14: `(require 'cl-lib)`
- L15: `(require 'dnd)`
- L22: `(defun kuro-dnd--path-has-control-character-p (path)`
- L26: `(defun kuro-dnd--file-uri-p (uri)`
- L32: `(defun kuro-dnd--local-file-path-p (path)`
- L41: `(defun kuro-dnd--quoted-local-file-path (uri)`
- L48: `(defun kuro-dnd-handle-uri (uri _action)`
- L56: `(defun kuro--setup-dnd ()`
- L64: `(defun kuro--teardown-dnd ()`
- L68: `(provide 'kuro-dnd)`

## emacs-lisp/features/kuro-hyperlinks-macros.el

- L13: `(defmacro kuro--make-hyperlink-overlay (beg end uri)`
- L24: `(provide 'kuro-hyperlinks-macros)`

## emacs-lisp/features/kuro-hyperlinks.el

- L16: `(require 'kuro-ffi-osc)`
- L17: `(require 'kuro-keymap)`
- L18: `(require 'kuro-hyperlinks-macros)`
- L19: `(require 'kuro-url-safety)`
- L37: `(defun kuro--hyperlink-range-entry-p (entry)`
- L50: `(defun kuro--hyperlink-buffer-range-p (beg end)`
- L58: `(defun kuro-open-hyperlink-at-point ()`
- L68: `(defun kuro--clear-hyperlink-overlays ()`
- L73: `(defun kuro--apply-hyperlink-ranges ()`
- L90: `(provide 'kuro-hyperlinks)`

## emacs-lisp/features/kuro-mux-ext-macros.el

- L15: `(defmacro kuro--install-mux-lifecycle-hooks ()`
- L21: `(defmacro kuro--uninstall-mux-lifecycle-hooks ()`
- L27: `(provide 'kuro-mux-ext-macros)`

## emacs-lisp/features/kuro-mux-ext.el

- L42: `(require 'kuro-config)`
- L43: `(require 'kuro-mux-ext-macros)`
- L60: `(defun kuro-mux-break-pane ()`
- L77: `(defun kuro-mux-join-pane (name)`
- L97: `(defun kuro-mux-rename (name)`
- L110: `(defun kuro-mux--name-lighter ()`
- L118: `(defun kuro-mux-send-to-session (name text)`
- L140: `(defun kuro-mux--tab-bar-update ()`
- L159: `(defun kuro-mux--tab-bar-session-tab-p (name)`
- L165: `(defun kuro-mux--on-session-created ()`
- L171: `(defun kuro-mux--on-session-killed ()`
- L183: `(defun kuro-mux--install-hooks ()`
- L187: `(defun kuro-mux--uninstall-hooks ()`
- L192: `(define-minor-mode kuro-mux-tab-bar-mode`
- L209: `(defcustom kuro-mux-layout-file`
- L216: `(defcustom kuro-mux-auto-save-layout nil`
- L224: `(defun kuro-mux--auto-save-on-exit ()`
- L231: `(provide 'kuro-mux-ext)`

## emacs-lisp/features/kuro-mux-ext2.el

- L16: `(require 'kuro-keymap)`
- L17: `(require 'kuro-mux-monitor)`
- L18: `(require 'cl-lib)`
- L80: `(defun kuro-mux--session-spec (buf)`
- L93: `(defun kuro-mux-save-layout ()`
- L112: `(defun kuro-mux--skip-layout-trivia ()`
- L121: `(defun kuro-mux--read-layout-file ()`
- L140: `(defun kuro-mux--proper-list-p (value)`
- L158: `(defun kuro-mux--proper-keyword-plist-p (value)`
- L170: `(defun kuro-mux--non-empty-string-p (value)`
- L174: `(defun kuro-mux--string-has-control-character-p (value)`
- L178: `(defun kuro-mux--valid-layout-name-p (value)`
- L183: `(defun kuro-mux--valid-layout-directory-p (value)`
- L191: `(defun kuro-mux--safe-layout-name (value)`
- L196: `(defun kuro-mux--safe-layout-directory (value)`
- L203: `(defun kuro-mux--layout-spec-allowed-keys-p (spec)`
- L213: `(defun kuro-mux--layout-session-from-plist (spec)`
- L223: `(defun kuro-mux--layout-session-to-plist (session)`
- L232: `(defun kuro-mux--valid-layout-spec-p (spec)`
- L239: `(defun kuro-mux--restore-session (spec)`
- L260: `(defun kuro-mux-restore-layout ()`
- L287: `(defun kuro-mux--parse-layout-plists (raw)`
- L364: `(defvar kuro-mux-prefix-map`
- L371: `(define-key map (kbd (number-to-string n))`
- L383: `(defcustom kuro-mux-prefix-key "C-c m"`
- L393: `(defun kuro-mux-create (&optional command)`
- L402: `(defun kuro-mux-install-keys (&optional keymap)`
- L410: `(define-key map (kbd kuro-mux-prefix-key) kuro-mux-prefix-map)`
- L416: `(defun kuro-mux--help-insert ()`
- L423: `(defun kuro-mux-help ()`
- L432: `(defun kuro-mux-clock ()`
- L451: `(defun kuro-mux--broadcast-send (text)`
- L466: `(defun kuro-mux-broadcast-toggle ()`
- L484: `(defcustom kuro-mux-install-prefix-keys t`
- L491: `(defun kuro-mux-setup ()`
- L506: `(provide 'kuro-mux-ext2)`

## emacs-lisp/features/kuro-mux-layout-macros.el

- L14: `(defmacro kuro--dispatch-layout (layout win buffers)`
- L25: `(provide 'kuro-mux-layout-macros)`

## emacs-lisp/features/kuro-mux-layout.el

- L17: `(require 'kuro-mux-layout-macros)`
- L42: `(defun kuro-mux--visible-session-buffers ()`
- L55: `(defun kuro-mux--layout-chain (window buffers side)`
- L65: `(defun kuro-mux--layout-main (main-win buffers main-side sub-side)`
- L75: `(defun kuro-mux--fill-band (band buffers start cols)`
- L89: `(defun kuro-mux--layout-tiled (buffers)`
- L110: `(defun kuro-mux-select-layout (layout)`
- L138: `(defun kuro-mux--cycle-layout (step)`
- L153: `(defun kuro-mux-next-layout ()`
- L161: `(defun kuro-mux-previous-layout ()`
- L168: `(provide 'kuro-mux-layout)`

## emacs-lisp/features/kuro-mux-macros.el

- L15: `(defmacro kuro--def-mux-nav (name nav-fn docstring)`
- L29: `(defmacro kuro--def-mux-split (name split-fn docstring)`
- L40: `(defmacro kuro--def-mux-swap (name window-nav-fn docstring)`
- L53: `(defmacro kuro--mux-resize-dispatch (direction delta)`
- L62: `(provide 'kuro-mux-macros)`

## emacs-lisp/features/kuro-mux-monitor.el

- L14: `(require 'kuro-config)`
- L15: `(require 'kuro-activity)`
- L16: `(require 'cl-lib)`
- L17: `(require 'subr-x)`
- L20: `(defcustom kuro-mux-monitor-activity-debounce 2.0`
- L26: `(defcustom kuro-mux-pipe-pane-directory`
- L52: `(defun kuro-mux--activity-watcher (_beg _end _old-len)`
- L66: `(defun kuro-mux--silence-watcher (_beg _end _old-len)`
- L85: `(defun kuro-mux-monitor-activity-toggle ()`
- L103: `(defun kuro-mux-monitor-silence (seconds)`
- L126: `(defun kuro-mux--pipe-pane-directory-path ()`
- L131: `(defun kuro-mux--pipe-pane-path-mode (path)`
- L138: `(defun kuro-mux--pipe-pane-existing-safe-directory ()`
- L156: `(defun kuro-mux--pipe-pane-safe-directory ()`
- L170: `(defun kuro-mux--pipe-pane-validate-filename (file)`
- L186: `(defun kuro-mux--pipe-pane-file-in-directory-p (file dir basename)`
- L191: `(defun kuro-mux--pipe-pane-single-link-p (file)`
- L195: `(defun kuro-mux--pipe-pane-file-attributes (file)`
- L200: `(defun kuro-mux--pipe-pane-target-from-attributes (file attributes)`
- L211: `(defun kuro-mux--pipe-pane-validate-existing-regular-file`
- L232: `(defun kuro-mux--pipe-pane-ensure-regular-file (file)`
- L246: `(defun kuro-mux--pipe-pane-prepare-file (file)`
- L260: `(defun kuro-mux--pipe-pane-validate-active-file (target)`
- L284: `(defun kuro-mux--pipe-pane-watcher (beg end _old-len)`
- L300: `(defun kuro-mux-pipe-pane (file)`
- L322: `(provide 'kuro-mux-monitor)`

## emacs-lisp/features/kuro-mux-windows.el

- L16: `(require 'kuro-config)`
- L17: `(require 'kuro-mux-macros)`
- L32: `(defun kuro-mux--track-window-change (_frame)`
- L44: `(defun kuro-mux-last ()`
- L59: `(defun kuro-mux-find-window (name)`
- L95: `(defun kuro-mux-detach ()`
- L112: `(defun kuro-mux-zoom ()`
- L128: `(defcustom kuro-mux-kill-confirm t`
- L134: `(defun kuro-mux-kill ()`
- L159: `(defun kuro-mux-resize-pane (direction &optional delta)`
- L177: `(provide 'kuro-mux-windows)`

## emacs-lisp/features/kuro-mux.el

- L53: `(require 'kuro-config)`
- L54: `(require 'kuro-ffi)`
- L55: `(require 'kuro-mux-macros)`
- L90: `(defun kuro-mux--register ()`
- L99: `(defun kuro-mux--unregister ()`
- L105: `(defun kuro-mux--live-sessions ()`
- L111: `(defun kuro-mux--for-each-live-session (fn &optional exclude)`
- L119: `(defun kuro-mux--session-display-name (buf)`
- L125: `(defun kuro-mux--find-session-by-name (name)`
- L134: `(defun kuro-mux--next-buffer (buf sessions)`
- L139: `(defun kuro-mux--prev-buffer (buf sessions)`
- L152: `(defun kuro-mux-switch-by-name (name)`
- L166: `(defun kuro-mux--session-index ()`
- L172: `(defun kuro-mux--mode-line-segment ()`
- L180: `(defcustom kuro-mux-mode-line-segment t`
- L187: `(defun kuro-mux--buffer-mode-line-setup ()`
- L195: `(defun kuro-mux-install-mode-line ()`
- L206: `(defun kuro-mux-other-window ()`
- L221: `(defun kuro-mux--visible-windows ()`
- L231: `(defun kuro-mux-rotate-panes (&optional backward)`
- L257: `(defun kuro-mux-rotate-panes-backward ()`
- L264: `(defun kuro-mux-select-by-index (n)`
- L280: `(require 'kuro-mux-windows)`
- L281: `(require 'kuro-mux-layout)`
- L282: `(require 'kuro-mux-ext)`
- L283: `(require 'kuro-mux-monitor)`
- L284: `(require 'kuro-mux-ext2)`
- L286: `(provide 'kuro-mux)`

## emacs-lisp/features/kuro-navigation-macros.el

- L15: `(defmacro kuro--def-navigator (name type-pred on-found on-miss docstring)`
- L27: `(defmacro kuro--def-nav-cmd (name nav-fn direction docstring)`
- L33: `(defmacro kuro--with-focus-guard (&rest body)`
- L40: `(defmacro kuro--def-focus-handler (name sequence doc)`
- L48: `(provide 'kuro-navigation-macros)`

## emacs-lisp/features/kuro-navigation.el

- L20: `(require 'kuro-ffi)`
- L21: `(require 'kuro-ffi-modes)`
- L22: `(require 'kuro-navigation-macros)`
- L39: `(defun kuro--update-prompt-positions (marks positions max-count)`
- L80: `(defun kuro--find-mark-in-direction (direction type-pred)`
- L112: `(defun kuro--command-output-region ()`
- L138: `(defun kuro-copy-command-output ()`
- L156: `(defun kuro--prompt-line-text (row)`
- L163: `(defun kuro--command-history-entries ()`
- L182: `(defun kuro--command-history-label (exit text)`
- L191: `(defun kuro-command-history ()`
- L237: `(provide 'kuro-navigation)`

## emacs-lisp/features/kuro-poll-modes-macros.el

- L15: `(defmacro kuro--run-tier1-poll-fns ()`
- L21: `(defmacro kuro--dispatch-clipboard-action (action)`
- L42: `(defmacro kuro--gated-poll (cadence fn)`
- L48: `(provide 'kuro-poll-modes-macros)`

## emacs-lisp/features/kuro-poll-modes.el

- L33: `(require 'kuro-config)`
- L34: `(require 'kuro-eval)`
- L35: `(require 'kuro-ffi)`
- L36: `(require 'kuro-ffi-modes)`
- L37: `(require 'kuro-ffi-osc)`
- L38: `(require 'kuro-navigation)`
- L39: `(require 'kuro-prompt-status)`
- L40: `(require 'kuro-hyperlinks)`
- L41: `(require 'kuro-text-size)`
- L42: `(require 'kuro-tramp)`
- L43: `(require 'kuro-poll-modes-macros)`
- L119: `(defun kuro--poll-osc-events ()`
- L129: `(defun kuro--notify-build-action-handler (session-id id)`
- L155: `(defun kuro--sanitize-notification-text (text)`
- L161: `(defun kuro--default-notify (title body &optional id report)`
- L194: `(defun kuro--notification-fields (notif)`
- L203: `(defun kuro--handle-notifications ()`
- L227: `(defun kuro--apply-terminal-modes (modes)`
- L243: `(defun kuro--poll-cwd ()`
- L258: `(defun kuro--progress-state-glyph (state)`
- L263: `(defun kuro--progress-mode-line-string (state percent)`
- L269: `(defun kuro--apply-progress (progress)`
- L283: `(defun kuro--progress-mode-line ()`
- L291: `(defun kuro--poll-progress ()`
- L308: `(defun kuro--poll-user-vars ()`
- L328: `(defun kuro--run-command-complete-hook (marks)`
- L343: `(defun kuro--poll-prompt-mark-updates ()`
- L352: `(defun kuro--poll-image-events ()`
- L357: `(defun kuro--poll-placeholder-events ()`
- L366: `(defun kuro--check-process-exit ()`
- L371: `(defun kuro--send-osc52-clipboard-response ()`
- L413: `(defun kuro--clipboard-sanitize (text)`
- L417: `(defun kuro--clipboard-set-selection (text target)`
- L429: `(defun kuro--clipboard-write (text target)`
- L447: `(defun kuro--clipboard-query (target)`
- L459: `(defun kuro--handle-clipboard-actions ()`
- L468: `(defun kuro--poll-terminal-mode-state ()`
- L478: `(defun kuro--poll-tier1-modes ()`
- L484: `(defun kuro--poll-terminal-modes ()`
- L493: `(provide 'kuro-poll-modes)`

## emacs-lisp/features/kuro-prompt-status.el

- L18: `(require 'kuro-config)`
- L19: `(require 'kuro-ffi)`
- L23: `(defcustom kuro-prompt-status-annotations t`
- L28: `(defcustom kuro-prompt-status-success-indicator "✓"`
- L33: `(defcustom kuro-prompt-status-failure-indicator "✗"`
- L38: `(defcustom kuro-prompt-status-show-extras t`
- L48: `(defcustom kuro-prompt-status-min-duration-ms 0`
- L91: `(defun kuro--prompt-status-indicator (exit-code)`
- L102: `(defun kuro--apply-prompt-status-overlay (row indicator)`
- L114: `(defun kuro--clear-prompt-status-overlays ()`
- L121: `(defun kuro--format-prompt-duration (duration-ms)`
- L146: `(defun kuro--sanitize-prompt-extra (text)`
- L152: `(defun kuro--format-prompt-extras (aid duration-ms err-path)`
- L171: `(defun kuro--apply-prompt-extras-overlay (row aid duration-ms err-path)`
- L187: `(defun kuro--update-prompt-status (marks)`
- L211: `(defun kuro--ensure-left-margin ()`
- L221: `(defun kuro-prompt-status-mode-line-segment ()`
- L240: `(defun kuro-prompt-status-install-mode-line ()`
- L253: `(provide 'kuro-prompt-status)`

## emacs-lisp/features/kuro-sessions.el

- L17: `(require 'cl-lib)`
- L18: `(require 'tabulated-list)`
- L19: `(require 'kuro-keymap)`
- L34: `(defun kuro--session-status (detached-p alive-p)`
- L40: `(defun kuro-sessions--fetch-raw ()`
- L46: `(defun kuro-sessions--entry (entry)`
- L54: `(defun kuro-sessions--entries ()`
- L60: `(defun kuro-sessions-attach ()`
- L71: `(defun kuro-sessions-destroy ()`
- L81: `(defun kuro-sessions-refresh ()`
- L86: `(defvar kuro-sessions-mode-map`
- L96: `(define-derived-mode kuro-sessions-mode tabulated-list-mode "Kuro Sessions"`
- L104: `(defun kuro-list-sessions ()`
- L113: `(provide 'kuro-sessions)`

## emacs-lisp/features/kuro-stream.el

- L40: `(require 'kuro-ffi)`
- L41: `(require 'kuro-ffi-osc)`
- L42: `(require 'kuro-typewriter)`
- L71: `(defun kuro--stream-idle-tick (buf)`
- L95: `(defun kuro--start-stream-idle-timer ()`
- L109: `(defun kuro--stop-stream-idle-timer ()`
- L120: `(provide 'kuro-stream)`

## emacs-lisp/features/kuro-text-size.el

- L37: `(require 'kuro-ffi-osc)`
- L54: `(defun kuro--text-size-permille-to-height (permille)`
- L67: `(defun kuro--clear-text-size-overlays ()`
- L72: `(defun kuro--make-text-size-overlay (beg end height)`
- L84: `(defun kuro--apply-text-size-ranges ()`
- L107: `(provide 'kuro-text-size)`

## emacs-lisp/features/kuro-tramp.el

- L16: `(require 'subr-x)`
- L17: `(require 'tramp)`
- L18: `(require 'kuro-config)`
- L19: `(require 'kuro-ffi-osc)`
- L29: `(defun kuro-tramp--valid-method-p (method)`
- L34: `(defun kuro-tramp--set-method (symbol value)`
- L41: `(defcustom kuro-tramp-method "ssh"`
- L51: `(defun kuro-tramp--valid-host-label-p (label)`
- L60: `(defun kuro-tramp--valid-remote-host-p (host)`
- L72: `(defun kuro-tramp--valid-host-list-p (hosts)`
- L80: `(defun kuro-tramp--set-allowed-hosts (symbol value)`
- L87: `(defcustom kuro-tramp-allowed-hosts nil`
- L98: `(defun kuro-tramp--safe-absolute-path-p (path)`
- L108: `(defun kuro-tramp--host-equal-p (left right)`
- L114: `(defun kuro-tramp--local-host-p (host)`
- L126: `(defun kuro-tramp--host-allowed-p (host)`
- L134: `(defun kuro--tramp-remote-path (host path)`
- L142: `(defun kuro-tramp--target-directory (host cwd)`
- L157: `(defun kuro--apply-cwd-with-tramp ()`
- L167: `(provide 'kuro-tramp)`

## emacs-lisp/features/kuro-tui-mode.el

- L34: `(require 'kuro-ffi)`
- L35: `(require 'kuro-config)`
- L94: `(defun kuro--enter-tui-mode ()`
- L100: `(defun kuro--exit-tui-mode ()`
- L108: `(defun kuro--update-tui-streaming-timer ()`
- L135: `(provide 'kuro-tui-mode)`

## emacs-lisp/features/kuro-url-detect.el

- L14: `(require 'cl-lib)`
- L15: `(require 'kuro-ffi)`
- L16: `(require 'kuro-keymap)`
- L17: `(require 'kuro-url-safety)`
- L21: `(defcustom kuro-url-detection t`
- L26: `(defcustom kuro-url-detection-delay 0.5`
- L48: `(defvar kuro--url-keymap`
- L56: `(defun kuro--clear-url-overlays ()`
- L63: `(defun kuro--url-detect-range-p (beg end)`
- L71: `(defun kuro--make-url-overlay (beg end url)`
- L89: `(defun kuro-open-url-at-point ()`
- L103: `(defun kuro--overlay-with-marker-p (pos marker)`
- L108: `(defun kuro--scan-urls-in-region (beg end)`
- L121: `(defun kuro--url-detect-visible ()`
- L139: `(defun kuro--start-url-detection ()`
- L146: `(defun kuro--stop-url-detection ()`
- L153: `(provide 'kuro-url-detect)`

## emacs-lisp/features/kuro-url-safety.el

- L15: `(require 'cl-lib)`
- L16: `(require 'url-parse)`
- L25: `(defun kuro--terminal-web-url-characters-valid-p (url)`
- L31: `(defun kuro--terminal-web-url-port-valid-p (port)`
- L38: `(defun kuro--terminal-web-url-dns-label-valid-p (label)`
- L47: `(defun kuro--terminal-web-url-dns-host-valid-p (host)`
- L59: `(defun kuro--terminal-web-url-ipv4-looking-p (host)`
- L64: `(defun kuro--terminal-web-url-decimal-octet-valid-p (octet)`
- L70: `(defun kuro--terminal-web-url-ipv4-address-valid-p (host)`
- L78: `(defun kuro--terminal-web-url-ipv6-h16-valid-p (group)`
- L83: `(defun kuro--terminal-web-url-ipv6-split-side (side)`
- L89: `(defun kuro--terminal-web-url-ipv6-group-count (groups allow-ipv4-at-end)`
- L118: `(defun kuro--terminal-web-url-ipv6-address-valid-p (address)`
- L147: `(defun kuro--terminal-web-url-ipv6-host-valid-p (host)`
- L154: `(defun kuro--terminal-web-url-host-valid-p (host)`
- L169: `(defun kuro--terminal-web-url-target-summary (url)`
- L175: `(defun kuro--terminal-web-url-valid-p (url)`
- L196: `(provide 'kuro-url-safety)`

## emacs-lisp/ffi/kuro-binary-decoder-macros.el

- L12: `(defmacro kuro--decode-face-range-step (result vec pos base ul-p)`
- L69: `(provide 'kuro-binary-decoder-macros)`

## emacs-lisp/ffi/kuro-binary-decoder.el

- L49: `(require 'kuro-binary-decoder-macros)`
- L137: `(defun kuro--binary-decode-error (format-string &rest args)`
- L145: `(defun kuro--binary-require-count (count section)`
- L151: `(defun kuro--binary-require-available (vec pos byte-count section)`
- L167: `(defun kuro--binary-require-byte-range (vec pos byte-count section)`
- L180: `(defun kuro--binary-normalize-frame (payload)`
- L200: `(defun kuro--binary-require-text-strings (text-strings num-rows)`
- L239: `(defun kuro--decode-face-ranges (vec pos num-face-ranges v2-p)`
- L311: `(defun kuro--decode-binary-updates-with-strings (text-strings vec)`
- L402: `(defun kuro--poll-updates-binary-optimised (session-id)`
- L440: `(provide 'kuro-binary-decoder)`

## emacs-lisp/ffi/kuro-eval.el

- L19: `(require 'cl-lib)`
- L20: `(require 'kuro-config)`
- L21: `(require 'kuro-ffi-osc)`
- L22: `(require 'subr-x)`
- L28: `(defcustom kuro-eval-allowed-commands`
- L52: `(defcustom kuro-eval-denied-env-name-regexp`
- L104: `(defun kuro--eval-proper-list-p (value)`
- L122: `(defun kuro--eval-command-allowed-name-p (name)`
- L128: `(defun kuro--eval-string-without-controls-p (value)`
- L133: `(defun kuro--eval-local-absolute-directory-p (path)`
- L141: `(defun kuro--eval-env-name-p (name)`
- L146: `(defun kuro--eval-env-name-denied-p (name)`
- L154: `(defun kuro--eval-validate-command-string (cmd)`
- L163: `(defun kuro--eval-osc51-command--build (name args source)`
- L193: `(defun kuro--eval-command-allowed-p (cmd)`
- L201: `(defun kuro--eval-osc51-command-form (cmd)`
- L221: `(defun kuro--eval-osc51-dispatch-command (command)`
- L233: `(defun kuro--eval-osc51-command (cmd)`
- L243: `(defun kuro--poll-eval-command-updates ()`
- L251: `(provide 'kuro-eval)`

## emacs-lisp/ffi/kuro-ffi-macros.el

- L14: `(defmacro kuro--when-divisible (counter divisor &rest body)`
- L25: `(defmacro kuro--defvar-permanent-local (name value &optional doc)`
- L40: `(defmacro kuro--def-ffi-getter (name core-fn default doc)`
- L46: `(defmacro kuro--def-ffi-unary (name core-fn default arg doc)`
- L52: `(defmacro kuro--def-ffi-binary (name core-fn default arg1 arg2 doc)`
- L59: `(defmacro kuro--define-ffi-binary-getters (&rest entries)`
- L74: `(defmacro kuro--define-ffi-getters (&rest entries)`
- L87: `(defmacro kuro--define-ffi-unary-getters (&rest entries)`
- L101: `(defmacro kuro--call (fallback &rest body)`
- L118: `(provide 'kuro-ffi-macros)`

## emacs-lisp/ffi/kuro-ffi-modes.el

- L19: `(require 'kuro-ffi)`
- L126: `(provide 'kuro-ffi-modes)`

## emacs-lisp/ffi/kuro-ffi-osc.el

- L20: `(require 'kuro-ffi)`
- L246: `(defun kuro--notify-action-response (session-id id button close)`
- L264: `(provide 'kuro-ffi-osc)`

## emacs-lisp/ffi/kuro-ffi.el

- L32: `(require 'kuro-config)`
- L33: `(require 'kuro-ffi-macros)`
- L39: `(defcustom kuro-log-errors t`
- L69: `(defun kuro-show-log ()`
- L111: `(defun kuro--init (command &optional shell-args rows cols)`
- L138: `(defun kuro--shutdown ()`
- L149: `(defun kuro--send-key (data)`
- L160: `(defun kuro--send-paste (text)`
- L178: `(defun kuro--resize (rows cols)`
- L183: `(defun kuro--set-cell-pixel-size (width height)`
- L192: `(defun kuro--push-cell-pixel-size-from-font ()`
- L220: `(provide 'kuro-ffi)`

## emacs-lisp/input/kuro-input-encode.el

- L14: `(require 'kuro-ffi)`
- L17: `(require 'kuro-input-keys-data)`
- L32: `(defun kuro--named-key-sequence-dispatch (base sequences)`
- L42: `(defun kuro--encode-key-event (event)`
- L65: `(defun kuro-send-next-key ()`
- L89: `(provide 'kuro-input-encode)`

## emacs-lisp/input/kuro-input-keymap-data.el

- L107: `(provide 'kuro-input-keymap-data)`

## emacs-lisp/input/kuro-input-keymap-meta-macros.el

- L13: `(require 'kuro-input-macros)`
- L14: `(require 'kuro-input-keymap-data)`
- L16: `(defmacro kuro--define-meta-letter-bindings (map letters)`
- L34: `(define-key ,map-sym (kbd (format "M-%c" char)) command)`
- L35: `(define-key ,map-sym (vector ?\e char) command))))`
- L38: `(provide 'kuro-input-keymap-meta-macros)`

## emacs-lisp/input/kuro-input-keymap-meta.el

- L15: `(require 'kuro-ffi)`
- L16: `(require 'kuro-input-keymap-data)`
- L17: `(require 'kuro-input-keymap-meta-macros)`
- L18: `(require 'kuro-keymap)`
- L19: `(require 'kuro-keymap-macros)`
- L33: `(defun kuro--send-meta-backspace ()`
- L40: `(defun kuro--meta-exception-char (exc)`
- L46: `(defun kuro--keymap-clear-exception (map exc)`
- L49: `(define-key map (kbd exc) nil)`
- L52: `(define-key map (vector ?\e char) nil)))))`
- L54: `(defun kuro--keymap-setup-meta (map)`
- L90: `(defun kuro--keymap-apply-exceptions (map)`
- L98: `(provide 'kuro-input-keymap-meta)`

## emacs-lisp/input/kuro-input-keymap-navigation-macros.el

- L13: `(require 'kuro-input-macros)`
- L14: `(require 'kuro-input-keymap-data)`
- L16: `(defmacro kuro--modifier-arrow-send-and-render (xterm-seq)`
- L22: `(defmacro kuro--define-modifier-arrow-bindings (map modifiers arrows)`
- L64: `(defmacro kuro--def-shifted-key (name kkp-seq legacy-seq docstring)`
- L77: `(provide 'kuro-input-keymap-navigation-macros)`

## emacs-lisp/input/kuro-input-keymap-navigation.el

- L15: `(require 'kuro-ffi)`
- L16: `(require 'kuro-input-keys-data)`
- L17: `(require 'kuro-input-keymap-data)`
- L18: `(require 'kuro-keymap)`
- L19: `(require 'kuro-keymap-macros)`
- L20: `(require 'kuro-input-keymap-navigation-macros)`
- L89: `(defun kuro--keymap-setup-navigation (map)`
- L121: `(define-key map [S-return] #'kuro--send-shifted-return))`
- L123: `(provide 'kuro-input-keymap-navigation)`

## emacs-lisp/input/kuro-input-keymap.el

- L27: `(require 'kuro-input-keymap-data)`
- L28: `(require 'kuro-input-keymap-meta)`
- L29: `(require 'kuro-input-keymap-navigation)`
- L30: `(require 'kuro-input-macros)`
- L31: `(require 'kuro-input-mouse)`
- L32: `(require 'kuro-input-mouse-scroll)`
- L33: `(require 'kuro-input-paste)`
- L34: `(require 'kuro-keymap)`
- L35: `(require 'kuro-keymap-macros)`
- L67: `(defvar kuro--keymap nil`
- L73: `(defun kuro--keymap-setup-special (map)`
- L82: `(defun kuro--send-escape ()`
- L88: `(defun kuro--keymap-setup-ctrl (map)`
- L98: `(define-key map (kbd "C-v") #'kuro--scroll-aware-ctrl-v)`
- L102: `(define-key map [escape] #'kuro--send-escape))`
- L104: `(defun kuro--keymap-setup-super-hyper (map)`
- L124: `(defun kuro--keymap-setup-mouse (map)`
- L130: `(defun kuro--keymap-setup-yank (map)`
- L141: `(defvar kuro--char-keymap nil`
- L148: `(defun kuro--build-full-keymap ()`
- L153: `(define-key map [remap self-insert-command] #'kuro--self-insert)`
- L163: `(defun kuro--build-keymap ()`
- L175: `(provide 'kuro-input-keymap)`

## emacs-lisp/input/kuro-input-keys-data.el

- L39: `(defun kuro--encode-kitty-key (key modifiers)`
- L131: `(provide 'kuro-input-keys-data)`

## emacs-lisp/input/kuro-input-keys-macros.el

- L12: `(defmacro kuro--def-key-sequence (name doc normal application &optional kkp-cp)`
- L26: `(defmacro kuro--def-shifted-fkey (name legacy-seq kkp-cp doc)`
- L37: `(defmacro kuro--def-keypad-key (name normal-char application-seq doc)`
- L47: `(provide 'kuro-input-keys-macros)`

## emacs-lisp/input/kuro-input-keys.el

- L28: `(require 'kuro-input-keys-macros)`
- L29: `(require 'kuro-input-keys-data)`
- L30: `(require 'kuro-input-macros)`
- L96: `(defmacro kuro--define-shifted-fkeys ()`
- L114: `(defmacro kuro--define-keypad-keys ()`
- L134: `(defun kuro--ctrl-modified (char _modifier)`
- L143: `(defun kuro--alt-modified (char)`
- L155: `(defun kuro--super-modified (char)`
- L167: `(defun kuro--hyper-modified (char)`
- L179: `(provide 'kuro-input-keys)`

## emacs-lisp/input/kuro-input-macros.el

- L13: `(defmacro kuro--def-special-key (name byte doc)`
- L20: `(defmacro kuro--def-kkp-key (name kkp-seq legacy-char doc)`
- L32: `(defmacro kuro--def-key-sender (name encoder-form arg doc)`
- L41: `(defmacro kuro--with-kkp-all-escape (sequence-form &rest legacy-body)`
- L50: `(defmacro kuro--with-kkp-disambiguate (kkp-form legacy-form)`
- L56: `(provide 'kuro-input-macros)`

## emacs-lisp/input/kuro-input-mode-buffer-macros.el

- L24: `(defmacro kuro--line-splice (from to replacement new-point)`
- L35: `(defmacro kuro--line-splice-with-undo (from to replacement new-point)`
- L44: `(defmacro kuro--line-replace-buffer-with-undo (replacement-form)`
- L51: `(defmacro kuro--line-insert-with-undo (from replacement-form)`
- L59: `(defmacro kuro--line-delete-with-undo (from to)`
- L64: `(defmacro kuro--line-replace-range-with-undo (from to replacement-form)`
- L74: `(provide 'kuro-input-mode-buffer-macros)`

## emacs-lisp/input/kuro-input-mode-completion-dispatch.el

- L15: `(defun kuro--line-display-completions (candidates label)`
- L21: `(defun kuro--line-dispatch-completion-candidates`
- L36: `(provide 'kuro-input-mode-completion-dispatch)`

## emacs-lisp/input/kuro-input-mode-completion-history.el

- L13: `(require 'kuro-input-mode-macros)`
- L14: `(require 'kuro-input-mode-completion-dispatch)`
- L21: `(defun kuro--line-all-history-completions (prefix)`
- L35: `(defun kuro--line-complete-history ()`
- L47: `(defun kuro--line-complete-history-multi ()`
- L59: `(defun kuro--line-history-search ()`
- L75: `(provide 'kuro-input-mode-completion-history)`

## emacs-lisp/input/kuro-input-mode-completion-word-macros.el

- L12: `(require 'kuro-input-mode-macros)`
- L14: `(defmacro kuro--line-with-word-span (vars &rest body)`
- L28: `(provide 'kuro-input-mode-completion-word-macros)`

## emacs-lisp/input/kuro-input-mode-completion-word.el

- L13: `(require 'kuro-input-mode-macros)`
- L14: `(require 'kuro-input-mode-completion-dispatch)`
- L15: `(require 'kuro-input-mode-completion-word-macros)`
- L34: `(defun kuro--line-complete-word ()`
- L45: `(defun kuro--line-expand-abbrev ()`
- L58: `(provide 'kuro-input-mode-completion-word)`

## emacs-lisp/input/kuro-input-mode-completion.el

- L13: `(require 'kuro-input-mode-completion-history)`
- L14: `(require 'kuro-input-mode-completion-word)`
- L21: `(defun kuro--line-complete ()`
- L30: `(provide 'kuro-input-mode-completion)`

## emacs-lisp/input/kuro-input-mode-data.el

- L15: `(require 'kuro-config)`
- L16: `(require 'kuro-ffi)`
- L20: `(defvar kuro--keymap)`
- L21: `(defvar kuro--char-keymap)`
- L22: `(defvar kuro-mode-map)`
- L77: `(defun kuro-input-mode-savehist-setup ()`
- L86: `(defcustom kuro-line-history-max-length 100`
- L95: `(defcustom kuro-line-use-minibuffer nil`
- L107: `(defcustom kuro-line-completion-function nil`
- L116: `(defcustom kuro-line-abbrev-alist nil`
- L133: `(defun kuro--input-mode-lighter ()`
- L137: `(provide 'kuro-input-mode-data)`

## emacs-lisp/input/kuro-input-mode-edit.el

- L16: `(require 'kuro-config)`
- L17: `(require 'kuro-keymap)`
- L18: `(require 'kuro-input-mode-macros)`
- L42: `(defvar kuro--line-edit-keymap`
- L49: `(define-derived-mode kuro-line-edit-mode text-mode "Kuro-Line-Edit"`
- L63: `(defun kuro--line-edit-in-buffer ()`
- L92: `(defun kuro-line-edit-send ()`
- L110: `(defun kuro-line-edit-discard ()`
- L122: `(provide 'kuro-input-mode-edit)`

## emacs-lisp/input/kuro-input-mode-ext.el

- L21: `(require 'kuro-config)`
- L22: `(require 'kuro-input-mode-macros)`
- L23: `(require 'kuro-input-mode-line-ops)`
- L24: `(require 'kuro-input-mode-transform)`
- L44: `(defvar kuro--keymap)`
- L45: `(defvar kuro--char-keymap)`
- L46: `(defvar kuro-mode-map)`
- L52: `(require 'kuro-input-mode-yank)`
- L53: `(require 'kuro-input-mode-ext2)`
- L55: `(provide 'kuro-input-mode-ext)`

## emacs-lisp/input/kuro-input-mode-ext2-data.el

- L78: `(provide 'kuro-input-mode-ext2-data)`

## emacs-lisp/input/kuro-input-mode-ext2-keymap.el

- L16: `(require 'kuro-keymap)`
- L17: `(require 'kuro-keymap-macros)`
- L18: `(require 'kuro-input-mode-ext2-data)`
- L19: `(require 'kuro-ffi-macros)`
- L66: `(defvar kuro--keymap)`
- L67: `(defvar kuro--char-keymap)`
- L68: `(defvar kuro-mode-map)`
- L77: `(defvar kuro--line-mode-keymap nil`
- L97: `(defun kuro--resolve-keymap (keymap)`
- L108: `(defun kuro--build-line-mode-keymap ()`
- L113: `(define-key map [remap self-insert-command] #'kuro--line-self-insert)`
- L114: `(define-key map [return] #'kuro--line-commit)`
- L115: `(define-key map [backspace] #'kuro--line-delete)`
- L122: `(defun kuro--install-input-mode-keymap ()`
- L176: `(defun kuro--apply-input-mode ()`
- L189: `(provide 'kuro-input-mode-ext2-keymap)`

## emacs-lisp/input/kuro-input-mode-ext2-mode-macros.el

- L13: `(defmacro kuro--def-input-mode (name mode message &rest pre-apply)`
- L27: `(provide 'kuro-input-mode-ext2-mode-macros)`

## emacs-lisp/input/kuro-input-mode-ext2-mode.el

- L14: `(require 'kuro-config)`
- L19: `(require 'kuro-input-mode-ext2-keymap)`
- L20: `(require 'kuro-input-mode-edit)`
- L21: `(require 'kuro-input-mode-line-nav)`
- L22: `(require 'kuro-input-mode-macros)`
- L88: `(defun kuro-cycle-input-mode ()`
- L98: `(provide 'kuro-input-mode-ext2-mode)`

## emacs-lisp/input/kuro-input-mode-ext2-send.el

- L14: `(require 'kuro-input-mode-line)`
- L15: `(require 'kuro-input-mode-macros)`
- L16: `(require 'kuro-config)`
- L26: `(defun kuro-line-minibuffer-send ()`
- L52: `(provide 'kuro-input-mode-ext2-send)`

## emacs-lisp/input/kuro-input-mode-ext2.el

- L17: `(require 'kuro-input-mode-ext2-data)`
- L18: `(require 'kuro-input-mode-ext2-send)`
- L19: `(require 'kuro-input-mode-ext2-keymap)`
- L20: `(require 'kuro-input-mode-ext2-mode)`
- L22: `(provide 'kuro-input-mode-ext2)`

## emacs-lisp/input/kuro-input-mode-history-nav-state.el

- L13: `(require 'kuro-input-mode-line-state)`
- L35: `(provide 'kuro-input-mode-history-nav-state)`

## emacs-lisp/input/kuro-input-mode-history-nav.el

- L13: `(require 'kuro-input-mode-history-nav-state)`
- L14: `(require 'kuro-input-mode-macros)`
- L59: `(provide 'kuro-input-mode-history-nav)`

## emacs-lisp/input/kuro-input-mode-history.el

- L15: `(require 'kuro-input-mode-completion)`
- L16: `(require 'kuro-input-mode-history-nav)`
- L18: `(provide 'kuro-input-mode-history)`

## emacs-lisp/input/kuro-input-mode-line-display.el

- L24: `(defun kuro--line-mode-update-display ()`
- L46: `(defun kuro--line-clear-overlay ()`
- L57: `(provide 'kuro-input-mode-line-display)`

## emacs-lisp/input/kuro-input-mode-line-nav.el

- L15: `(require 'kuro-input-mode-macros)`
- L53: `(provide 'kuro-input-mode-line-nav)`

## emacs-lisp/input/kuro-input-mode-line-ops.el

- L15: `(require 'kuro-input-mode-macros)`
- L75: `(provide 'kuro-input-mode-line-ops)`

## emacs-lisp/input/kuro-input-mode-line-state.el

- L15: `(require 'seq)`
- L35: `(defun kuro--line-undo-push ()`
- L43: `(defun kuro--line-set-buffer (text)`
- L61: `(provide 'kuro-input-mode-line-state)`

## emacs-lisp/input/kuro-input-mode-line.el

- L14: `(require 'kuro-config)`
- L15: `(require 'kuro-ffi)`
- L16: `(require 'cl-lib)`
- L17: `(require 'kuro-input-mode-line-display)`
- L18: `(require 'kuro-input-mode-macros)`
- L38: `(defun kuro--line-undo ()`
- L51: `(defun kuro--line-word-bounds-forward ()`
- L60: `(defun kuro--line-self-insert ()`
- L77: `(defun kuro--line-quoted-insert ()`
- L90: `(defun kuro--line-delete ()`
- L96: `(defun kuro--line-newline ()`
- L105: `(defun kuro--line-kill-line ()`
- L110: `(defun kuro--line-commit ()`
- L126: `(defun kuro--line-abort ()`
- L132: `(provide 'kuro-input-mode-line)`

## emacs-lisp/input/kuro-input-mode-macros.el

- L26: `(require 'kuro-input-mode-buffer-macros)`
- L27: `(require 'kuro-input-mode-line-state)`
- L32: `(defmacro kuro--with-line-edit (&rest body)`
- L37: `(defmacro kuro--with-line-edit-undo (&rest body)`
- L41: `(defmacro kuro--def-line-command (name docstring &rest body)`
- L52: `(defmacro kuro--def-line-nav (name docstring &rest body)`
- L62: `(defmacro kuro--def-line-history-nav (name docstring guard stashp index-form buffer-form)`
- L113: `(defmacro kuro--line-apply-word-transform (replacement-form)`
- L123: `(defmacro kuro--def-line-word-transform (name docstring replacement-form)`
- L131: `(provide 'kuro-input-mode-macros)`

## emacs-lisp/input/kuro-input-mode-transform.el

- L13: `(require 'kuro-input-mode-line)`
- L14: `(require 'kuro-input-mode-macros)`
- L34: `(defun kuro--line-transpose-words ()`
- L51: `(provide 'kuro-input-mode-transform)`

## emacs-lisp/input/kuro-input-mode-yank.el

- L14: `(require 'kuro-input-mode-macros)`
- L28: `(defun kuro--line-yank ()`
- L39: `(defun kuro--line-yank-pop ()`
- L60: `(defun kuro--line-yank-last-arg ()`
- L91: `(provide 'kuro-input-mode-yank)`

## emacs-lisp/input/kuro-input-mode.el

- L43: `(require 'kuro-input-mode-data)`
- L44: `(require 'kuro-input-mode-line)`
- L45: `(require 'kuro-input-mode-line-state)`
- L46: `(require 'kuro-input-mode-macros)`
- L47: `(require 'kuro-ffi)`
- L49: `(require 'kuro-input-mode-history)`
- L50: `(require 'kuro-input-mode-ext)`
- L52: `(provide 'kuro-input-mode)`

## emacs-lisp/input/kuro-input-mouse-macros.el

- L15: `(defmacro kuro--dispatch-mouse-event (btn press)`
- L30: `(defmacro kuro--def-mouse-cmd (name btn-form press doc)`
- L42: `(defmacro kuro--def-scroll-command (name doc scroll-form offset-form)`
- L58: `(provide 'kuro-input-mouse-macros)`

## emacs-lisp/input/kuro-input-mouse-scroll.el

- L16: `(require 'kuro-input-mouse)`
- L17: `(require 'kuro-input-mouse-macros)`
- L37: `(defun kuro--mouse-scroll-up ()`
- L52: `(defun kuro--mouse-scroll-down ()`
- L62: `(provide 'kuro-input-mouse-scroll)`

## emacs-lisp/input/kuro-input-mouse.el

- L18: `(require 'kuro-ffi)`
- L19: `(require 'kuro-ffi-osc)`
- L20: `(require 'kuro-input-mouse-macros)`
- L52: `(defun kuro--encode-mouse (event button press)`
- L67: `(defun kuro--encode-mouse-sgr (event button press)`
- L85: `(provide 'kuro-input-mouse)`

## emacs-lisp/input/kuro-input-paste.el

- L17: `(require 'kuro-ffi)`
- L39: `(defun kuro--paste-prefix-numeric-value (arg default)`
- L53: `(defun kuro--paste-yank-index (arg)`
- L60: `(defun kuro--paste-yank-pop-index (arg)`
- L64: `(defun kuro--send-paste-or-raw (text)`
- L72: `(defun kuro--yank (&optional arg)`
- L81: `(defun kuro--yank-pop (&optional arg)`
- L92: `(provide 'kuro-input-paste)`

## emacs-lisp/input/kuro-input-render.el

- L15: `(require 'kuro-config)`
- L16: `(require 'kuro-input-macros)`
- L30: `(defun kuro--do-pending-render (buf)`
- L39: `(defun kuro--schedule-immediate-render ()`
- L52: `(provide 'kuro-input-render)`

## emacs-lisp/input/kuro-input-send-scroll.el

- L14: `(require 'kuro-input-macros)`
- L15: `(require 'kuro-input-send)`
- L31: `(defun kuro--scroll-aware-ctrl-v ()`
- L42: `(defun kuro--scroll-aware-meta-v ()`
- L74: `(provide 'kuro-input-send-scroll)`

## emacs-lisp/input/kuro-input-send.el

- L14: `(require 'kuro-ffi)`
- L15: `(require 'kuro-input-macros)`
- L16: `(require 'kuro-input-keys-macros)`
- L17: `(require 'kuro-input-mouse-macros)`
- L18: `(require 'kuro-input-render)`
- L38: `(defun kuro--self-insert ()`
- L54: `(defun kuro--send-special (byte)`
- L90: `(defun kuro--send-key-sequence (normal-sequence application-sequence)`
- L100: `(defun kuro--ctrl-alt-modified (char _modifier)`
- L117: `(provide 'kuro-input-send)`

## emacs-lisp/input/kuro-input.el

- L23: `(require 'kuro-config)`
- L24: `(require 'kuro-ffi)`
- L25: `(require 'kuro-ffi-osc)`
- L26: `(require 'kuro-input-macros)`
- L27: `(require 'kuro-input-render)`
- L34: `(require 'kuro-input-send)`
- L35: `(require 'kuro-input-send-scroll)`
- L36: `(require 'kuro-input-keys)`
- L37: `(require 'kuro-input-mouse)`
- L38: `(require 'kuro-input-mouse-scroll)`
- L44: `(require 'kuro-input-keymap)`
- L45: `(require 'kuro-input-encode)`
- L53: `(provide 'kuro-input)`

## emacs-lisp/rendering/kuro-overlays-macros.el

- L15: `(defmacro kuro--toggle-blink-state (blink-type)`
- L22: `(defmacro kuro--register-blink-overlay (ov blink-type row)`
- L37: `(provide 'kuro-overlays-macros)`

## emacs-lisp/rendering/kuro-overlays.el

- L26: `(require 'seq)`
- L27: `(require 'subr-x)`
- L28: `(require 'kuro-ffi)`
- L29: `(require 'kuro-faces)`
- L30: `(require 'kuro-faces-attrs)`
- L31: `(require 'kuro-overlays-macros)`
- L63: `(defun kuro--recompute-blink-frame-intervals ()`
- L181: `(defun kuro--toggle-blink-phase (blink-type)`
- L195: `(defun kuro--tick-blink-overlays ()`
- L231: `(defun kuro--clear-all-image-overlays ()`
- L242: `(defun kuro--filter-overlays (overlays predicate &optional on-delete)`
- L256: `(defun kuro--clear-row-image-overlays (row)`
- L279: `(defun kuro--finite-proper-list-p (value)`
- L297: `(defun kuro--list-length-p (value expected)`
- L310: `(defun kuro--strict-base64-payload-p (b64)`
- L323: `(defun kuro--image-notification-p (notif)`
- L333: `(defun kuro--placeholder-region-p (region)`
- L352: `(defun kuro--decode-png-image (b64)`
- L363: `(defun kuro--place-image-overlay (img row col cell-width &optional image-id)`
- L384: `(defun kuro--render-image-notification (notif)`
- L403: `(defun kuro--clear-placeholder-overlays ()`
- L410: `(defun kuro--place-placeholder-tile (img row col slice)`
- L425: `(defun kuro--render-placeholder-region (region)`
- L454: `(defun kuro--render-placeholder-regions (regions)`
- L466: `(defun kuro--animation-clamp-gap (gap-ms)`
- L475: `(defun kuro--animation-cancel (image-id)`
- L481: `(defun kuro--animation-overlay-for-id (image-id)`
- L488: `(defun kuro--animation-advance (buffer image-id frame-index)`
- L517: `(defun kuro--maybe-start-animation (image-id)`
- L530: `(defun kuro--clear-all-animations ()`
- L573: `(defun kuro--remove-blink-overlay-from-lists (ov)`
- L582: `(defun kuro--reset-blink-overlays (remaining)`
- L594: `(defun kuro--shift-blink-overlay-rows (up down rows)`
- L655: `(provide 'kuro-overlays)`

## emacs-lisp/rendering/kuro-render-buffer-macros.el

- L13: `(defmacro kuro--with-buffer-edit (&rest body)`
- L21: `(defmacro kuro--with-current-render-row (row &rest body)`
- L30: `(defmacro kuro--with-rewritten-line (row text col-to-buf &rest body)`
- L54: `(provide 'kuro-render-buffer-macros)`

## emacs-lisp/rendering/kuro-render-buffer.el

- L19: `(require 'cl-lib)`
- L20: `(require 'kuro-ffi)`
- L21: `(require 'kuro-ffi-modes)`
- L22: `(require 'kuro-faces)`
- L23: `(require 'kuro-render-buffer-macros)`
- L24: `(require 'kuro-overlays)`
- L60: `(defun kuro--init-row-positions (rows)`
- L64: `(defun kuro--invalidate-row-positions ()`
- L84: `(defun kuro--row-position (row)`
- L98: `(defun kuro--scroll-lines (direction n last-rows)`
- L126: `(defun kuro--apply-buffer-scroll (up down)`
- L146: `(defun kuro--clear-line-blink-overlays (line-start &optional row pre-end)`
- L162: `(defun kuro--clear-line-blink-overlays-from-row (row line-start line-end-before)`
- L175: `(defun kuro--clear-line-blink-overlays-by-scan (line-start line-end-before)`
- L210: `(defun kuro--update-row-position-cache-after-line-change (row old-len new-len new-line-end)`
- L230: `(defun kuro--ensure-buffer-row-exists (row)`
- L277: `(defun kuro--clear-row-overlays (row &optional pre-end)`
- L307: `(defun kuro--update-line-full (row text face-ranges col-to-buf)`
- L326: `(require 'kuro-render-cursor)`
- L328: `(provide 'kuro-render-buffer)`

## emacs-lisp/rendering/kuro-render-cursor-macros.el

- L13: `(defmacro kuro--cache-cursor-state (row col visible shape)`
- L20: `(provide 'kuro-render-cursor-macros)`

## emacs-lisp/rendering/kuro-render-cursor.el

- L17: `(require 'kuro-ffi)`
- L18: `(require 'kuro-ffi-modes)`
- L19: `(require 'kuro-render-cursor-macros)`
- L23: `(defvar kuro--col-to-buf-map)`
- L55: `(defun kuro--grid-col-to-buffer-pos (row col)`
- L73: `(defun kuro--anchor-window-at-pos (win target-pos)`
- L104: `(defun kuro--apply-cursor-blink (visible shape)`
- L119: `(defun kuro--apply-cursor-display (visible shape)`
- L193: `(defun kuro--update-cursor ()`
- L234: `(defun kuro--update-scroll-indicator ()`
- L251: `(provide 'kuro-render-cursor)`

## emacs-lisp/rendering/kuro-renderer-macros.el

- L13: `(defmacro kuro--recompute-budget-vars (rate)`
- L24: `(defmacro kuro--with-frame-coalescing (&rest body)`
- L43: `(defmacro kuro--with-live-render-frame (&rest body)`
- L52: `(provide 'kuro-renderer-macros)`

## emacs-lisp/rendering/kuro-renderer-pipeline-macros.el

- L15: `(defmacro kuro--timed (ms-var &rest body)`
- L23: `(defmacro kuro--with-render-env (&rest body)`
- L33: `(defmacro kuro--reset-cursor-cache ()`
- L43: `(defmacro kuro--with-render-buffer-mutation (&rest body)`
- L50: `(defmacro kuro--with-update-entry (entry-form row text face-ranges col-to-buf &rest body)`
- L64: `(defmacro kuro--do-update-list (update-list row text face-ranges col-to-buf &rest body)`
- L80: `(defmacro kuro--with-core-render-pipeline-body (&rest body)`
- L98: `(defmacro kuro--core-render-pipeline-run (updates-var &rest body)`
- L106: `(defmacro kuro--core-render-pipeline-run-with-timing`
- L126: `(provide 'kuro-renderer-pipeline-macros)`

## emacs-lisp/rendering/kuro-renderer-pipeline.el

- L32: `(require 'kuro-ffi)`
- L33: `(require 'kuro-ffi-osc)`
- L34: `(require 'kuro-config)`
- L35: `(require 'kuro-render-buffer)`
- L36: `(require 'kuro-binary-decoder)`
- L37: `(require 'kuro-debug-perf)`
- L38: `(require 'kuro-poll-modes)`
- L39: `(require 'kuro-renderer-pipeline-macros)`
- L69: `(defvar kuro--col-to-buf-map nil`
- L111: `(defun kuro--sanitize-title (title)`
- L118: `(defun kuro--pending-resize-valid-p (rows cols)`
- L122: `(defun kuro--current-buffer-row-count ()`
- L128: `(defun kuro--adjust-buffer-row-count (rows)`
- L143: `(defun kuro--reset-render-state-after-resize (rows cols)`
- L155: `(defun kuro--handle-pending-resize ()`
- L174: `(defun kuro--apply-title-update ()`
- L185: `(defun kuro--apply-decoded-scroll-shift ()`
- L218: `(defun kuro--col-to-buf-map-should-evict-p ()`
- L224: `(defun kuro--evict-out-of-bounds-col-to-buf-rows ()`
- L231: `(defun kuro--evict-empty-dirty-col-to-buf-rows (dirty-rows)`
- L237: `(defun kuro--evict-stale-col-to-buf-entries (dirty-rows)`
- L257: `(defun kuro--dirty-update-error (format-string &rest args)`
- L265: `(defun kuro--validate-dirty-face-ranges (face-ranges entry-index)`
- L284: `(defun kuro--validate-dirty-col-to-buf (col-to-buf entry-index)`
- L300: `(defun kuro--validate-dirty-update-entry (entry entry-index)`
- L323: `(defun kuro--validate-dirty-update-list (update-list)`
- L335: `(defun kuro--apply-dirty-lines (update-list)`
- L351: `(defun kuro--poll-frame-updates ()`
- L365: `(defun kuro--execute-core-render-steps (&optional timings)`
- L389: `(defun kuro--core-render-pipeline ()`
- L397: `(defun kuro--core-render-pipeline-with-timing ()`
- L408: `(defun kuro--finalize-dirty-updates (update-list)`
- L421: `(defun kuro--apply-dirty-updates ()`
- L434: `(defun kuro--poll-within-budget (frame-start-time)`
- L449: `(provide 'kuro-renderer-pipeline)`

## emacs-lisp/rendering/kuro-renderer.el

- L33: `(require 'kuro-renderer-pipeline)`
- L34: `(require 'kuro-renderer-macros)`
- L35: `(require 'kuro-input)`
- L36: `(require 'kuro-config)`
- L37: `(require 'kuro-faces)`
- L38: `(require 'kuro-overlays)`
- L39: `(require 'kuro-stream)`
- L40: `(require 'kuro-tui-mode)`
- L159: `(defun kuro--update-frame-budget-ratio (duration)`
- L170: `(defun kuro--install-render-timer (rate)`
- L185: `(defun kuro--start-render-loop ()`
- L194: `(defun kuro--stop-render-loop ()`
- L207: `(defun kuro--switch-render-timer (new-rate)`
- L218: `(defun kuro--ring-pending-bell ()`
- L229: `(defun kuro--tick-blink-if-active ()`
- L234: `(defun kuro--render-cycle-stage-2 (frame-start)`
- L246: `(defun kuro--render-cycle ()`
- L270: `(provide 'kuro-renderer)`

## emacs-lisp/rendering/kuro-typewriter.el

- L29: `(require 'kuro-config)`
- L30: `(require 'kuro-ffi)`
- L31: `(require 'kuro-render-buffer)`
- L68: `(defun kuro--start-typewriter-timer ()`
- L81: `(defun kuro--stop-typewriter-timer ()`
- L87: `(defun kuro--typewriter-enqueue (row text)`
- L92: `(defun kuro--typewriter-tick ()`
- L114: `(defun kuro--typewriter-queue-next ()`
- L127: `(defun kuro--typewriter-write-partial (row text)`
- L145: `(provide 'kuro-typewriter)`
