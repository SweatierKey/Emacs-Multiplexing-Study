# Indice del codice: term+

Fonte: https://github.com/tarao/term-plus-el.git

Revisione: `c3c9239b339c127231860de43abfa08c44c0201a`.


## term+.el

- L28: `(require 'term)`
- L29: `(require 'term+vars)`
- L30: `(require 'term+edit)`
- L31: `(require 'term+logging)`
- L32: `(require 'term+file-transfer)`
- L33: `(require 'term+shell-history)`
- L58: `(defun term+pass-through (char)`
- L63: `(defun term+send-esc ()`
- L68: `(defun term+yank ()`
- L78: `(defun term+send-input-and-char-mode ()`
- L84: `(defun term+mark-or-copy ()`
- L110: `(defun term+maybe-remote-directory (dir)`
- L124: `(defun term+update-default-directory ()`
- L127: `(defun term+set-hostname (host)`
- L132: `(defun term+set-user (user)`
- L137: `(defun term+set-directory (dir)`
- L142: `(defun term+set-shell (shell)`
- L204: `(defun term+control-command-list-1 ()`
- L226: `(defun term+control-command-list ()`
- L236: `(defmacro term+with-original-documentation (fun bind &rest body)`
- L245: `(defun term+control-command-documentation (&optional fun start end)`
- L270: `(defun term+zero-width-truncation ()`
- L302: `(defun term+setup ()`
- L326: `(provide 'term+)`

## term+edit.el

- L27: `(require 'term)`
- L28: `(require 'term+vars)`
- L29: `(require 'term+input)`
- L31: `(defun term+edit-post-command ()`
- L36: `(defun term+edit-initialize-buffer (beg end text)`
- L43: `(define-minor-mode term+edit-mode`
- L90: `(defun term+edit (&optional beg end text)`
- L101: `(defun term+edit-at-point (&optional text)`
- L107: `(defun term+edit-to-eol (&optional text)`
- L115: `(defun term+edit-as-expected (&optional text)`
- L124: `(defun term+edit-insert (text)`
- L151: `(provide 'term+edit)`

## term+file-transfer.el

- L27: `(require 'term+vars)`
- L33: `(defun term+find-file (file &optional other-window)`
- L38: `(define-minor-mode term+temporal-view-mode`
- L43: `(defun term+view-file (file &optional other-window)`
- L50: `(defun term+resolve-file-name (file)`
- L60: `(defun term+open (files &optional find-file)`
- L84: `(defun term+view (files)`
- L90: `(defun term+copy-files (files target)`
- L108: `(defun term+read-file-name (files prompt dir default)`
- L113: `(defun term+get (files)`
- L140: `(defun term+put (&optional arg)`
- L165: `(defun term+put-one (files)`
- L169: `(defun term+put-multi ()`
- L184: `(defun term+put-mode-noselect (dir)`
- L189: `(define-derived-mode term+put-mode dired-mode`
- L194: `(define-key term+put-mode-map (kbd "C-c C-c") #'exit-recursive-edit)`
- L195: `(define-key term+put-mode-map (kbd "q") #'exit-recursive-edit)`
- L196: `(define-key term+put-mode-map (kbd "Q") #'term+put-mode-abort)`
- L197: `(define-key term+put-mode-map (kbd "C-c C-g") #'term+put-mode-abort))`
- L199: `(defun term+put-mode-abort ()`
- L206: `(provide 'term+file-transfer)`

## term+input.el

- L27: `(require 'term+vars)`
- L33: `(defun term+input-beg ()`
- L37: `(defun term+input-end ()`
- L41: `(defun term+input-reset-range ()`
- L48: `(defun term+input-in-range-p (&optional pos)`
- L54: `(defun term+input-reset (&optional no-delete)`
- L78: `(defun term+input-set-range (beg end &optional no-delete)`
- L112: `(defun term+input-constrain-to-field ()`
- L117: `(define-minor-mode term+input-mode`
- L128: `(defun term+beginning-of-line (&optional arg)`
- L139: `(defun term+end-of-line (&optional arg)`
- L150: `(defun term+kill-line (&optional arg)`
- L174: `(defun term+kill-input (&optional arg)`
- L232: `(provide 'term+input)`

## term+logging.el

- L27: `(require 'term)`
- L28: `(require 'term+vars)`
- L34: `(defun term+hardcopy (file &optional append whole-buffer)`
- L58: `(defun term+make-hardcopy-separator-from-list (list &rest args)`
- L74: `(defun term+make-hardcopy-separator ()`
- L94: `(define-minor-mode term+buffer-log-mode`
- L119: `(defun term+start-buffer-log (file)`
- L135: `(defun term+stop-buffer-log ()`
- L143: `(defun term+toggle-buffer-log ()`
- L152: `(defun term+buffer-log-save (&optional buffer)`
- L192: `(defun term+buffer-log-save-truncate (beg hist-pos end)`
- L203: `(defun term+buffer-log-save-buffer (beg hist-pos end)`
- L238: `(define-minor-mode term+record-mode`
- L263: `(defun term+start-record (file)`
- L270: `(defun term+stop-record ()`
- L276: `(defun term+toggle-record ()`
- L283: `(defun term+mouse-stop-record (event)`
- L297: `(defun term+record-show-overlay (&optional window start)`
- L330: `(defun term+record-write (time str)`
- L352: `(provide 'term+logging)`

## term+shell-history.el

- L27: `(require 'term+vars)`
- L29: `(defun term+set-shell-history-file (path)`
- L42: `(defun term+shell-history-file ()`
- L49: `(defun term+shell-history-buffer (file)`
- L56: `(defun term+parse-shell-history ()`
- L76: `(defun term+default-shell-history (initial)`
- L83: `(defun term+shell-history (&optional initial)`
- L105: `(provide 'term+shell-history)`

## term+vars.el

- L27: `(require 'term)`
- L28: `(require 'dired)`
- L29: `(require 'dired-aux)`
- L50: `(defmacro term+make-composed-keymap (maps &optional parent)`
- L55: `(defvar term+char-map`
- L58: `(define-key map (kbd "C-x") nil)`
- L59: `(define-key map (kbd "M-x") nil)`
- L60: `(define-key map (kbd "M-:") nil)`
- L62: `(define-key map (kbd "C-M-j") #'term+edit-as-expected)`
- L63: `(define-key map (kbd "M-RET") #'term+edit-as-expected)`
- L64: `(define-key map (kbd "C-q") #'term+pass-through)`
- L65: `(define-key map (kbd "C-c C-e") #'term+send-esc)`
- L66: `(define-key map (kbd "C-c C-c") #'term-interrupt-subjob)`
- L67: `(define-key map (kbd "C-c h") #'term+hardcopy)`
- L68: `(define-key map (kbd "C-c l") #'term+toggle-buffer-log)`
- L69: `(define-key map (kbd "C-c r") #'term+toggle-record)`
- L70: `(define-key map (kbd "C-y") #'term+yank)`
- L89: `\(define-key term+char-map KEY nil).")`
- L90: `(defvar term+line-map`
- L93: `(define-key map (kbd "C-M-j") #'term-char-mode)`
- L94: `(define-key map (kbd "M-RET") #'term-char-mode)`
- L95: `(define-key map (kbd "RET") #'term+send-input-and-char-mode)`
- L96: `(define-key map (kbd "C-a") #'term+beginning-of-line)`
- L97: `(define-key map (kbd "C-e") #'term+end-of-line)`
- L98: `(define-key map (kbd "M-p") #'term-previous-input)`
- L99: `(define-key map (kbd "M-n") #'term-next-input)`
- L100: `(define-key map (kbd "C-k") #'term+kill-line)`
- L101: `(define-key map (kbd "C-c C-u") #'term+kill-input)`
- L102: `(define-key map (kbd "C-c C-w") #'backward-kill-word)`
- L109: `(defvar term+input-map-overlay nil)`
- L111: `(defvar term+input-map term+line-map)`
- L112: `(defvar term+input-readonly-map`
- L114: `(define-key map " " #'term+mark-or-copy)`
- L115: `(define-key map (kbd "RET") #'term-char-mode)`
- L116: `(define-key map (kbd "ESC") #'term-char-mode)`
- L195: `(defcustom term+kill-buffer-at-exit t`
- L199: `(defcustom term+edit-kill-to-eol nil`
- L206: `(defcustom term+edit-restore-last-pos t`
- L211: `(defcustom term+edit-quit-commands '(kill-ring-save)`
- L215: `(defcustom term+open-in-other-window nil`
- L220: `(defcustom term+default-user nil`
- L226: `(defcustom term+shell-history-dont-exec nil`
- L231: `(defcustom term+download-directory nil`
- L235: `(defcustom term+upload-directory nil`
- L239: `(defcustom term+hardcopy-visible-contents t`
- L245: `(defcustom term+hardcopy-append nil`
- L249: `(defcustom term+hardcopy-separator '(">" "=" " %s@%s %s " "=" "<")`
- L266: `(defcustom term+hardcopy-separator-args '(user host time)`
- L278: `(defcustom term+buffer-log-interval 5`
- L284: `(defcustom term+record-append nil`
- L288: `(defcustom term+record-message`
- L298: `(define-key map [mouse-1] #'term+mouse-stop-record)`
- L306: `(provide 'term+vars)`

## xterm-256color.el

- L27: `(require 'term)`
- L28: `(require 'cl-lib)`
- L188: `(defun term-ansi-256-setup ()`
- L216: `(defun term-ansi-16-color (i &optional prop)`
- L224: `(defun term-ansi-set-16-color (color &optional background bright)`
- L230: `(defun term-ansi-256-color (parameter &optional prop)`
- L250: `(defun term-ansi-set-256-color (color &optional background)`
- L254: `(defun term-warn-unknown-color (parameter)`
- L370: `(defun term-need-filling ()`
- L374: `(defun term-fill-char (char count)`
- L378: `(defun term-fill-lines (count)`
- L384: `(defun term-fill-region (start end)`
- L398: `(defun term-erase-to-eol ()`
- L405: `(defun term-erase-in-display (kind)`
- L471: `(defun term-warn-unknown-sequence (char)`
- L563: `(provide 'xterm-256color)`
