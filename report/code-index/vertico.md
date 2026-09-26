# Indice del codice: vertico

Fonte: https://github.com/minad/vertico.git

Revisione: `a9998a777f1d92348f84d091bb15b87df933a7a2`.


## extensions/vertico-buffer.el

- L37: `(require 'vertico)`
- L39: `(defcustom vertico-buffer-hide-prompt t`
- L44: `(defcustom vertico-buffer-display-action`
- L92: `(defun vertico-buffer--redisplay (_)`
- L122: `(defun vertico-buffer--setup ()`
- L196: `(define-minor-mode vertico-buffer-mode`
- L215: `(provide 'vertico-buffer)`

## extensions/vertico-directory.el

- L30: `;; (keymap-set vertico-map "RET" #'vertico-directory-enter)`
- L31: `;; (keymap-set vertico-map "DEL" #'vertico-directory-delete-char)`
- L32: `;; (keymap-set vertico-map "M-DEL" #'vertico-directory-delete-word)`
- L45: `(require 'vertico)`
- L49: `(defcustom vertico-directory-tidy t`
- L59: `(defun vertico-directory-enter (&optional arg)`
- L86: `(defun vertico-directory-up (&optional n)`
- L105: `(defun vertico-directory-delete-char (n)`
- L113: `(defun vertico-directory-delete-word (n)`
- L120: `(defun vertico-directory-tidy ()`
- L131: `(defvar-keymap vertico-directory-map`
- L140: `(provide 'vertico-directory)`

## extensions/vertico-flat.el

- L39: `(require 'vertico)`
- L42: `(defcustom vertico-flat-max-lines 1`
- L47: `(defcustom vertico-flat-format`
- L62: `(defcustom vertico-flat-annotate nil`
- L67: `(defvar-keymap vertico-flat-map`
- L73: `(define-minor-mode vertico-flat-mode`
- L84: `(defun vertico-flat--format (prop)`
- L141: `(provide 'vertico-flat)`

## extensions/vertico-grid.el

- L35: `(require 'vertico)`
- L40: `(defcustom vertico-grid-min-columns 2`
- L45: `(defcustom vertico-grid-max-columns 8`
- L50: `(defcustom vertico-grid-annotate 0`
- L55: `(defcustom vertico-grid-separator`
- L61: `(defcustom vertico-grid-lookahead 100`
- L67: `(defvar-keymap vertico-grid-map`
- L77: `(defun vertico-grid-left (&optional n)`
- L82: `(defun vertico-grid-right (&optional n)`
- L94: `(defun vertico-grid-scroll-down (&optional n)`
- L99: `(defun vertico-grid-scroll-up (&optional n)`
- L105: `(define-minor-mode vertico-grid-mode`
- L170: `(provide 'vertico-grid)`

## extensions/vertico-indexed.el

- L33: `(require 'vertico)`
- L40: `(defcustom vertico-indexed-start 0`
- L51: `(define-minor-mode vertico-indexed-mode`
- L80: `(provide 'vertico-indexed)`

## extensions/vertico-mouse.el

- L30: `(require 'vertico)`
- L37: `(defun vertico-mouse--index (event)`
- L43: `(defun vertico-mouse--click (key)`
- L53: `(defvar-keymap vertico-mouse-map`
- L65: `(define-minor-mode vertico-mouse-mode`
- L83: `(provide 'vertico-mouse)`

## extensions/vertico-multiform.el

- L59: `(require 'vertico)`
- L62: `(defcustom vertico-multiform-commands nil`
- L72: `(defcustom vertico-multiform-categories nil`
- L82: `(defun vertico-multiform--toggle (arg)`
- L93: `(defun vertico-multiform--lookup (key list)`
- L105: `(defun vertico-multiform--exit ()`
- L110: `(defun vertico-multiform--setup ()`
- L149: `(defvar-keymap vertico-multiform-map`
- L153: `(define-minor-mode vertico-multiform-mode`
- L168: `(defun vertico-multiform--display-menu (menu _event)`
- L170: `(define-key menu [vertico-multiform--display-menu]`
- L183: `(defun vertico-multiform--toggle-mode-1 (mode arg)`
- L204: `(defun vertico-multiform--toggle-mode (mode)`
- L228: `(define-key vertico-multiform-map (vector toggle) (cons label toggle))`
- L229: `(keymap-set vertico-multiform-map (format "M-%c" (aref label 0)) toggle)))`
- L231: `(provide 'vertico-multiform)`

## extensions/vertico-quick.el

- L31: `;; (keymap-set vertico-map "M-q" #'vertico-quick-insert)`
- L32: `;; (keymap-set vertico-map "C-q" #'vertico-quick-exit)`
- L36: `(require 'vertico)`
- L59: `(defcustom vertico-quick1 "asdfgh"`
- L64: `(defcustom vertico-quick2 "jkluionm"`
- L69: `(defun vertico-quick--keys (two index start)`
- L99: `(defun vertico-quick--read (&optional first)`
- L117: `(defun vertico-quick-jump ()`
- L127: `(defun vertico-quick-exit ()`
- L134: `(defun vertico-quick-insert ()`
- L140: `(provide 'vertico-quick)`

## extensions/vertico-repeat.el

- L37: `;; (keymap-global-set "M-R" #'vertico-repeat)`
- L38: `;; (keymap-set vertico-map "M-P" #'vertico-repeat-previous)`
- L39: `;; (keymap-set vertico-map "M-N" #'vertico-repeat-next)`
- L40: `;; (keymap-set vertico-map "S-<prior>" #'vertico-repeat-previous)`
- L41: `;; (keymap-set vertico-map "S-<next>" #'vertico-repeat-next)`
- L51: `(require 'vertico)`
- L54: `(defcustom vertico-repeat-filter`
- L63: `(defcustom vertico-repeat-transformers`
- L78: `(defun vertico-repeat--filter-commands (session)`
- L82: `(defun vertico-repeat--filter-empty (session)`
- L86: `(defun vertico-repeat--remove-long (session)`
- L93: `(defun vertico-repeat--remember-input ()`
- L97: `(defun vertico-repeat--current ()`
- L110: `(defun vertico-repeat--save-on-exit ()`
- L122: `(defun vertico-repeat--restore (session)`
- L142: `(defun vertico-repeat--run (session)`
- L153: `(defun vertico-repeat-save ()`
- L164: `(defun vertico-repeat-next (n)`
- L172: `(defun vertico-repeat-previous (n)`
- L194: `(defun vertico-repeat-select ()`
- L240: `(defun vertico-repeat (&optional arg)`
- L246: `(provide 'vertico-repeat)`

## extensions/vertico-reverse.el

- L36: `(require 'vertico)`
- L39: `(defcustom vertico-reverse-candidates t`
- L44: `(defcustom vertico-reverse-prompt t`
- L49: `(defvar-keymap vertico-reverse-map`
- L64: `(define-minor-mode vertico-reverse-mode`
- L92: `(provide 'vertico-reverse)`

## extensions/vertico-sort.el

- L35: `(require 'vertico)`
- L41: `(defcustom vertico-sort-history-duplicate 10`
- L50: `(defcustom vertico-sort-history-decay 10`
- L57: `(defun vertico-sort--history ()`
- L89: `(defun vertico-sort--length-string< (x y)`
- L93: `(defun vertico-sort--decorated (list)`
- L99: `(defmacro vertico-sort--define (by bsize bindex bpred pred)`
- L125: `(defun vertico-sort-directories-first (list)`
- L131: `(provide 'vertico-sort)`

## extensions/vertico-suspend.el

- L35: `;; (keymap-global-set "M-S" #'vertico-suspend)`
- L47: `(require 'vertico)`
- L53: `(defun vertico-suspend ()`
- L91: `(defun vertico-suspend--unselect (&rest _)`
- L99: `(defun vertico-suspend--message (&rest app)`
- L105: `(provide 'vertico-suspend)`

## extensions/vertico-unobtrusive.el

- L37: `(require 'vertico-flat)`
- L42: `(define-minor-mode vertico-unobtrusive-mode`
- L64: `(provide 'vertico-unobtrusive)`

## vertico.el

- L37: `(require 'compat)`
- L52: `(defcustom vertico-count-format (cons "%-6s " "%s/%s")`
- L56: `(defcustom vertico-group-format`
- L63: `(defcustom vertico-count 10`
- L67: `(defcustom vertico-preselect 'directory`
- L75: `(defcustom vertico-scroll-margin 2`
- L80: `(defcustom vertico-resize resize-mini-windows`
- L86: `(defcustom vertico-cycle nil`
- L90: `(defcustom vertico-multiline`
- L95: `(defcustom vertico-sort-function`
- L106: `(defcustom vertico-sort-override-function nil`
- L127: `(defvar-keymap vertico-map`
- L195: `(defun vertico--affixate (cands)`
- L209: `(defun vertico--move-to-front (elem list)`
- L216: `(defun vertico--metadata-get (prop)`
- L220: `(defun vertico--sort-function ()`
- L226: `(defun vertico--compute (input)`
- L295: `(defun vertico--hilit (cand)`
- L301: `(defun vertico--cycle (list n)`
- L305: `(defun vertico--group-by (fun elems)`
- L333: `(defun vertico--remote-p (path)`
- L337: `(defun vertico--update (&optional interruptible)`
- L365: `(defun vertico--display-string (str)`
- L388: `(defun vertico--window-width ()`
- L392: `(defun vertico--truncate-multiline (str max)`
- L402: `(defun vertico--compute-scroll ()`
- L410: `(defun vertico--format-group-title (title cand)`
- L420: `(defun vertico--format-count ()`
- L429: `(defun vertico--display-count ()`
- L435: `(defun vertico--prompt-selection ()`
- L442: `(defun vertico--remove-face (beg end face &optional obj)`
- L450: `(defun vertico--debug (&rest _)`
- L462: `(defun vertico--protect (fun)`
- L479: `(defun vertico--exhibit ()`
- L489: `(defun vertico--goto (index)`
- L496: `(defun vertico--candidate (&optional hl)`
- L510: `(defun vertico--match-p (input)`
- L615: `(defun vertico-first ()`
- L620: `(defun vertico-last ()`
- L625: `(defun vertico-scroll-down (&optional n)`
- L630: `(defun vertico-scroll-up (&optional n)`
- L635: `(defun vertico-next (&optional n)`
- L646: `(defun vertico-previous (&optional n)`
- L651: `(defun vertico-exit (&optional arg)`
- L659: `(defun vertico-next-group (&optional n)`
- L672: `(defun vertico-previous-group (&optional n)`
- L678: `(defun vertico-exit-input ()`
- L683: `(defun vertico-save ()`
- L690: `(defun vertico-insert ()`
- L703: `(define-minor-mode vertico-mode`
- L711: `(defun vertico--command-p (_sym buffer)`
- L725: `(provide 'vertico)`
