# Indice del codice: term-mux

Fonte: https://github.com/merrickluo/term-mux.el.git

Revisione: `0b1770318c892de0d9dce5a5eb6cde38b9c03d78`.


## term-mux-frame.el

- L25: `(require 'term-mux)`
- L26: `(require 'uuid)`
- L27: `(require 'vterm nil t)`
- L28: `(require 'ghostel nil t)`
- L34: `(defcustom term-mux-frame-session-name-fn #'uuid-string`
- L39: `(defcustom term-mux-frame-name "Terminal"`
- L45: `(defun term-mux-frame()`
- L52: `(defun term-mux-frame--exit-fn (&optional buffer _event)`
- L78: `(provide 'term-mux-frame)`

## term-mux-test.el

- L8: `(require 'ert)`
- L9: `(require 'term-mux)`
- L207: `(provide 'term-mux-test)`

## term-mux.el

- L22: `(require 'subr-x)`
- L23: `(require 'project)`
- L26: `(require 'projectile nil t)`
- L29: `(require 'vterm nil t)`
- L30: `(require 'ghostel nil t)`
- L36: `(defcustom term-mux-buffer-prefix "*term-mux-"`
- L41: `(defcustom term-mux-default-terminal-setup-fn #'term-mux--detect-terminal`
- L72: `(defun term-mux--add-to-buffer-table (session buffer)`
- L79: `(defun term-mux--handle-kill-buffer ()`
- L105: `(defun term-mux--current-window ()`
- L116: `(defun term-mux--session-name ()`
- L129: `(defun term-mux--session-root ()`
- L138: `(defun term-mux--new-buffer (session terminal-setup-fn slot)`
- L151: `(defun term-mux--show-buffer (buffer-or-name &optional session window)`
- L164: `(defun term-mux--current-session ()`
- L168: `(defun term-mux--list-buffers (&optional session)`
- L172: `(defun term-mux--detect-terminal ()`
- L179: `(defun term-mux--setup-vterm ()`
- L187: `(defun term-mux--setup-eshell ()`
- L193: `(defun term-mux--setup-ghostel ()`
- L203: `(defun term-mux--buffer-slot (&optional buffer)`
- L206: `(defun term-mux--buffer-session (&optional buffer)`
- L209: `(defun term-mux--find-empty-slot (session)`
- L223: `(defun term-mux--next-buffer (session slot direction)`
- L241: `(defun term-mux-toggle ()`
- L258: `(defun term-mux-create (&optional terminal-setup-fn session)`
- L272: `(defun term-mux-buffer (&optional terminal-setup-fn session)`
- L287: `(defun term-mux-create-eshell (&optional session)`
- L292: `(defun term-mux-create-vterm (&optional session)`
- L298: `(defun term-mux-create-ghostel (&optional session)`
- L303: `(defun term-mux-switch-to (buffer-or-name)`
- L309: `(defun term-mux-next (&optional direction)`
- L320: `(defun term-mux-prev ()`
- L325: `(defun term-mux-session-empty-p (&optional session)`
- L333: `(defvar term-mux-command-map`
- L335: `(define-key map "n" #'term-mux-next)`
- L336: `(define-key map "p" #'term-mux-prev)`
- L337: `(define-key map "s" #'term-mux-switch-to)`
- L338: `(define-key map "c" #'term-mux-create)`
- L339: `(define-key map "e" #'term-mux-create-eshell)`
- L340: `(define-key map "g" #'term-mux-create-ghostel)`
- L341: `(define-key map "v" #'term-mux-create-vterm)`
- L347: `(define-minor-mode term-mux-mode`
- L355: `(provide 'term-mux)`
