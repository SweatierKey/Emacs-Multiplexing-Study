# Indice del codice: eee

Fonte: https://github.com/eval-exec/eee.el.git

Revisione: `ba62f385963d67d48abdec56c70fb08a3a14f656`.


## eee-eat.el

- L11: `(require 'eat)`
- L15: `(define-derived-mode ee-eat-mode eat-mode "Eat[EEE]" )`
- L17: `(defun ee-eat--setup-buffer ()`
- L36: `(defun ee-eat-start-terminal (name command callback)`
- L53: `(provide 'eee-eat)`

## eee-transient.el

- L28: `(require 'cl-lib)`
- L29: `(require 'transient)`
- L41: `(defun ee--rewrite-sanitize-overlays ()`
- L52: `(defun ee--set-with-scope (sym value &optional scope)`
- L75: `(defun ee--get-directive (args)`
- L83: `(defun ee--instructions-make-overlay (text &optional ov)`
- L122: `(defun ee--read-with-prefix (prefix)`
- L177: `(defun ee--transient-read-variable (prompt initial-input history)`
- L185: `(defun ee-system-prompt--format (&optional message)`
- L210: `(defun ee--crowdsourced-prompts ()`
- L505: `(defun ee--setup-directive-menu (sym msg &optional external)`
- L1005: `(defun ee--merge-additional-directive (additional &optional full)`
- L1030: `(defun ee--regenerate ()`
- L1053: `(defun ee--read-crowdsourced-prompt ()`
- L1101: `(defun ee--edit-directive (sym &optional callback-cmd)`
- L1215: `(provide 'ee-transient)`

## eee-vterm.el

- L11: `(require 'vterm)`
- L13: `(define-derived-mode ee-vterm-mode vterm-mode "VTerm[EEE]")`
- L16: `(defun ee-vterm-start-terminal (name command callback)`
- L35: `(provide 'eee-vterm)`

## eee.el

- L15: `(defcustom ee-terminal-command "wezterm"`
- L20: `(defcustom ee-terminal-options`
- L36: `(defcustom ee-debug-message nil`
- L41: `(defun ee-message (format-string &rest args)`
- L47: `(defun ee-get-terminal-options()`
- L55: `(defun ee-script-path(script-name)`
- L86: `(defun ee-start-external-terminal (name command callback)`
- L100: `(defcustom ee-start-terminal-function #'ee-start-external-terminal`
- L107: `(defun ee-start-process-shell-command-in-terminal (name command callback)`
- L123: `(defun ee--normalize-path (path)`
- L126: `(defun ee-get-project-dir-or-current-dir()`
- L135: `(defun ee-integer-p(str)`
- L139: `(defun ee-jump (destination)`
- L192: `(defun ee-jump-from (destination-file)`
- L201: `(defun ee-join-args(args)`
- L207: `(defun ee-run(name working-directory command &optional args callback)`
- L241: `(defmacro ee-define (name working-directory script-path &optional args callback)`
- L256: `(defun ee-region-text()`
- L344: `(defun ee-recentf-dump ()`
- L367: `(defvar ee-keymap (make-sparse-keymap)`
- L369: `(define-key ee-keymap (kbd "f") 'ee-find)`
- L370: `(define-key ee-keymap (kbd "g") 'ee-lazygit)`
- L371: `(define-key ee-keymap (kbd "y") 'ee-yazi)`
- L372: `(define-key ee-keymap (kbd "Y") 'ee-yazi-project)`
- L373: `(define-key ee-keymap (kbd "r") 'ee-rg)`
- L374: `(define-key ee-keymap (kbd "l") 'ee-line)`
- L377: `(provide 'eee)`
