# Indice del codice: elscreen

Fonte: https://github.com/knu/elscreen.git

Revisione: `cc58337faf5ba1eae7e87f75f6ff3758675688f2`.


## elscreen-buffer-list.el

- L16: `(provide 'elscreen-buffer-list)`
- L17: `(require 'elscreen)`
- L20: `(defun buffer-dead-p (buffer)`
- L28: `(defun reorder-buffer-list (new-list)`
- L47: `(defun elscreen-get-buffer-list (screen)`
- L52: `(defun elscreen-set-buffer-list (screen buflist)`
- L58: `(defun elscreen-save-buffer-list (&optional screen)`
- L64: `(defun elscreen-load-buffer-list (&optional screen)`
- L79: `(defcustom elscreen-buffer-list-enabled nil`
- L84: `(defun toggle-elscreen-buffer-list (&optional arg)`

## elscreen-color-theme.el

- L24: `(provide 'elscreen-color-theme)`
- L25: `(require 'elscreen)`
- L27: `(defcustom elscreen-color-theme-override-theme nil`
- L32: `(defcustom elscreen-color-theme-tab-background-face-function`
- L38: `(defcustom elscreen-color-theme-tab-control-face-function`
- L44: `(defcustom elscreen-color-theme-tab-current-screen-face-function`
- L50: `(defcustom elscreen-color-theme-tab-other-screen-face-function`
- L68: `(defun elscreen-color-theme-tab-background-face-default-function (theme)`
- L77: `(defun elscreen-color-theme-tab-control-face-default-function (theme)`
- L89: `(defun elscreen-color-theme-tab-other-screen-face-default-function (theme)`

## elscreen-dired.el

- L25: `(provide 'elscreen-dired)`
- L26: `(require 'elscreen)`

## elscreen-dnd.el

- L25: `(provide 'elscreen-dnd)`
- L26: `(require 'elscreen)`
- L28: `(defcustom elscreen-dnd-open-file-new-screen t`
- L36: `(defmacro elscreen-dnd-drag-n-drop (ad-do-it)`

## elscreen-gf.el

- L27: `(provide 'elscreen-gf)`
- L28: `(require 'elscreen)`
- L29: `(require 'ring)`
- L38: `(defcustom elscreen-gf-grep-program-name "grep"`
- L43: `(defcustom elscreen-gf-idutils-gid-program-name "gid"`
- L48: `(defcustom elscreen-gf-idutils-mkid-program-name "mkid"`
- L53: `(defcustom elscreen-gf-cscope-program-name "cscope"`
- L58: `(defcustom elscreen-gf-global-program-name "global"`
- L63: `(defcustom elscreen-gf-global-gtags-program-name "gtags"`
- L68: `(defcustom elscreen-gf-mode-truncate-lines t`
- L76: `(defcustom elscreen-gf-invoke-point-history-length 8`
- L139: `(defvar elscreen-gf-map (make-sparse-keymap)`
- L141: `(define-key elscreen-gf-map "G" 'elscreen-gf-grep)`
- L142: `(define-key elscreen-gf-map "m" 'elscreen-gf-idutils-mkid)`
- L143: `(define-key elscreen-gf-map "g" 'elscreen-gf-idutils-gid)`
- L144: `(define-key elscreen-gf-map "c" 'elscreen-gf-cscope)`
- L145: `(define-key elscreen-gf-map "t" 'elscreen-gf-global-gtags)`
- L146: `(define-key elscreen-gf-map "l" 'elscreen-gf-global)`
- L147: `(define-key elscreen-gf-map "u" 'elscreen-gf-go-back-to-latest-invoke-point)`
- L148: `(define-key elscreen-gf-map "v" 'elscreen-gf-display-version)`
- L150: `(define-key elscreen-map "\C-g" elscreen-gf-map)`
- L152: `(defvar elscreen-gf-mode-map (make-sparse-keymap)`
- L154: `(define-key elscreen-gf-mode-map "n"    'elscreen-gf-mode-next-line)`
- L155: `(define-key elscreen-gf-mode-map "p"    'elscreen-gf-mode-previous-line)`
- L156: `(define-key elscreen-gf-mode-map " "    'elscreen-gf-mode-scroll-up)`
- L157: `(define-key elscreen-gf-mode-map "\177" 'elscreen-gf-mode-scroll-down)`
- L158: `(define-key elscreen-gf-mode-map "<"    'elscreen-gf-mode-beginning-of-buffer)`
- L159: `(define-key elscreen-gf-mode-map ">"    'elscreen-gf-mode-end-of-buffer)`
- L160: `(define-key elscreen-gf-mode-map "N"    'elscreen-gf-mode-next-file)`
- L161: `(define-key elscreen-gf-mode-map "P"    'elscreen-gf-mode-previous-file)`
- L162: `(define-key elscreen-gf-mode-map "t"    'elscreen-gf-mode-truncate-lines-toggle)`
- L163: `(define-key elscreen-gf-mode-map "o"    'elscreen-gf-mode-jump-to-entry)`
- L164: `(define-key elscreen-gf-mode-map "O"    'elscreen-gf-mode-jump-to-entry-read-only)`
- L165: `(define-key elscreen-gf-mode-map "\C-g" 'elscreen-gf-mode-search-quit)`
- L166: `(define-key elscreen-gf-mode-map "q"    'elscreen-gf-mode-exit)`
- L167: `(define-key elscreen-gf-mode-map "v"    'elscreen-gf-display-version)`
- L191: `(defun elscreen-gf-define-major-mode-token (major-mode token-chars)`
- L244: `(defun elscreen-gf-goto-screen-create (target-directory)`
- L256: `(defun elscreen-gf-mode (target-directory)`
- L275: `(defun elscreen-gf-mode-selected-entry-overlay ()`
- L281: `(defun elscreen-gf-mode-next-line ()`
- L293: `(defun elscreen-gf-mode-previous-line ()`
- L305: `(defun elscreen-gf-mode-scroll-up ()`
- L311: `(defun elscreen-gf-mode-scroll-down ()`
- L317: `(defun elscreen-gf-mode-beginning-of-buffer ()`
- L324: `(defun elscreen-gf-mode-end-of-buffer ()`
- L331: `(defun elscreen-gf-mode-next-file ()`
- L346: `(defun elscreen-gf-mode-previous-file ()`
- L366: `(defun elscreen-gf-mode-truncate-lines-toggle ()`
- L380: `(defun elscreen-gf-mode-jump-to-entry ()`
- L415: `(defun elscreen-gf-mode-jump-to-entry-read-only ()`
- L422: `(defun elscreen-gf-mode-search-quit (&optional force)`
- L432: `(defun elscreen-gf-mode-exit ()`
- L456: `(defun elscreen-gf-process-exclusive-p (process &optional noerror)`
- L478: `(defun elscreen-gf-search-regexp-dot-to-token (regexp token)`
- L492: `(defun elscreen-gf-read-selection (title prompt option-defs)`
- L535: `(define-key minibuffer-map "\C-m" 'undefined)`
- L536: `(define-key minibuffer-map "\C-g" 'abort-recursive-edit)`
- L539: `(define-key minibuffer-map (car option-def) 'self-insert-and-exit))`
- L567: `(defun elscreen-gf-search-filter (process string)`
- L619: `(defun elscreen-gf-search-sentinel (process event)`
- L628: `(defun elscreen-gf-grep (&optional pattern file-name-re)`
- L666: `(defun elscreen-gf-grep-line-parser (line)`
- L680: `(defun elscreen-gf-idutils-mkid (&optional directory)`
- L700: `(defun elscreen-gf-idutils-mkid-sentinel (process event)`
- L706: `(defun elscreen-gf-idutils-mkid-after-save ()`
- L714: `(defun elscreen-gf-idutils-mkid-setup-after-save-hook ()`
- L718: `(defun elscreen-gf-idutils-gid (&optional pattern)`
- L757: `(defun elscreen-gf-cscope (&optional pattern directory)`
- L796: `(defun elscreen-gf-cscope-line-parser-common (line)`
- L809: `(defun elscreen-gf-cscope-line-parser-query-type-1 (line)`
- L826: `(defun elscreen-gf-global-gtags (&optional directory)`
- L846: `(defun elscreen-gf-global-gtags-sentinel (process event)`
- L852: `(defun elscreen-gf-global-gtags-after-save ()`
- L860: `(defun elscreen-gf-global-gtags-setup-after-save-hook ()`
- L876: `(defun elscreen-gf-global (&optional pattern directory)`
- L922: `(defun elscreen-gf-global-line-parser (line)`
- L931: `(defun elscreen-gf-go-back-to-latest-invoke-point ()`
- L1014: `(defun elscreen-gf-display-version ()`

## elscreen-goby.el

- L25: `(provide 'elscreen-goby)`
- L26: `(require 'elscreen)`

## elscreen-howm.el

- L25: `(provide 'elscreen-howm)`
- L26: `(require 'elscreen)`
- L30: `(defcustom elscreen-howm-mode-to-nickname-alist`
- L41: `(defcustom elscreen-howm-buffer-to-nickname-alist`
- L81: `(defun elscreen-howm-mode-buffer-to-nickname ()`
- L87: `(defun elscreen-howm-mode-update-title ()`
- L93: `(defun elscreen-howm-mode-initialize ()`
- L101: `(defun howm-save-and-kill-buffer/screen ()`
- L118: `(define-key howm-mode-map`

## elscreen-server.el

- L28: `(require 'elscreen)`
- L29: `(require 'dframe)`
- L31: `(defcustom elscreen-server-dont-use-dedicated-frame t`
- L36: `(defun elscreen-server-visit-files-new-screen (buffer-list)`
- L58: `(provide 'elscreen-server)`

## elscreen-speedbar.el

- L24: `(provide 'elscreen-speedbar)`
- L25: `(require 'elscreen)`
- L27: `(defcustom elscreen-speedbar-find-file-in-screen t`

## elscreen-w3m.el

- L25: `(provide 'elscreen-w3m)`
- L26: `(require 'elscreen)`
- L49: `(defun elscreen-w3m-mailto-url-popup-function (buffer)`
- L66: `(defun elscreen-w3m-initialize ()`

## elscreen-wl.el

- L25: `(provide 'elscreen-wl)`
- L26: `(require 'elscreen)`
- L27: `(require 'wl)`
- L32: `(defcustom elscreen-wl-draft-use-elscreen t`
- L38: `(defcustom elscreen-wl-display-biff-on-tab t`
- L51: `(defcustom elscreen-wl-mode-to-nickname-alist`
- L78: `(defmacro elscreen-wl-draft-create-buffer (ad-do-it)`
- L116: `(defmacro elscreen-wl-compensate-summary-window (ad-do-it)`

## elscreen.el

- L45: `(require 'dired)`
- L56: `(defcustom elscreen-prefix-key "\C-z"`
- L66: `(defcustom elscreen-default-buffer-name "*scratch*"`
- L72: `(defcustom elscreen-default-buffer-initial-major-mode initial-major-mode`
- L78: `(defcustom elscreen-default-buffer-initial-message initial-scratch-message`
- L86: `(defcustom elscreen-mode-to-nickname-alist`
- L109: `(defcustom elscreen-buffer-to-nickname-alist`
- L125: `(defcustom elscreen-display-screen-number t`
- L131: `(defcustom elscreen-display-tab t`
- L151: `(defcustom elscreen-tab-display-control t`
- L161: `(defcustom elscreen-tab-display-kill-screen 'left`
- L208: `(defvar elscreen-map (make-sparse-keymap)`
- L210: `(define-key elscreen-map "\C-c" 'elscreen-create)`
- L211: `(define-key elscreen-map "c"    'elscreen-create)`
- L212: `(define-key elscreen-map "C"    'elscreen-clone)`
- L213: `(define-key elscreen-map "\C-k" 'elscreen-kill)`
- L214: `(define-key elscreen-map "k"    'elscreen-kill)`
- L215: `(define-key elscreen-map "\M-k" 'elscreen-kill-screen-and-buffers)`
- L216: `(define-key elscreen-map "K"    'elscreen-kill-others)`
- L217: `(define-key elscreen-map "\C-p" 'elscreen-previous)`
- L218: `(define-key elscreen-map "p"    'elscreen-previous)`
- L219: `(define-key elscreen-map "\C-n" 'elscreen-next)`
- L220: `(define-key elscreen-map "n"    'elscreen-next)`
- L221: `(define-key elscreen-map "\C-a" 'elscreen-toggle)`
- L222: `(define-key elscreen-map "a"    'elscreen-toggle)`
- L223: `(define-key elscreen-map "'"    'elscreen-goto)`
- L224: `(define-key elscreen-map "\""   'elscreen-select-and-goto)`
- L225: `(define-key elscreen-map "0"    'elscreen-jump-0)`
- L226: `(define-key elscreen-map "1"    'elscreen-jump)`
- L227: `(define-key elscreen-map "2"    'elscreen-jump)`
- L228: `(define-key elscreen-map "3"    'elscreen-jump)`
- L229: `(define-key elscreen-map "4"    'elscreen-jump)`
- L230: `(define-key elscreen-map "5"    'elscreen-jump)`
- L231: `(define-key elscreen-map "6"    'elscreen-jump)`
- L232: `(define-key elscreen-map "7"    'elscreen-jump)`
- L233: `(define-key elscreen-map "8"    'elscreen-jump)`
- L234: `(define-key elscreen-map "9"    'elscreen-jump-9)`
- L235: `(define-key elscreen-map "\C-s" 'elscreen-swap)`
- L236: `(define-key elscreen-map "\C-w" 'elscreen-display-screen-name-list)`
- L237: `(define-key elscreen-map "w"    'elscreen-display-screen-name-list)`
- L238: `(define-key elscreen-map "\C-m" 'elscreen-display-last-message)`
- L239: `(define-key elscreen-map "m"    'elscreen-display-last-message)`
- L240: `(define-key elscreen-map "\C-t" 'elscreen-display-time)`
- L241: `(define-key elscreen-map "t"    'elscreen-display-time)`
- L242: `(define-key elscreen-map "A"    'elscreen-screen-nickname)`
- L243: `(define-key elscreen-map "b"    'elscreen-find-and-goto-by-buffer)`
- L244: `(define-key elscreen-map "\C-f" 'elscreen-find-file)`
- L245: `(define-key elscreen-map "\C-r" 'elscreen-find-file-read-only)`
- L246: `(define-key elscreen-map "d"    'elscreen-dired)`
- L247: `(define-key elscreen-map "\M-x" 'elscreen-execute-extended-command)`
- L248: `(define-key elscreen-map "i"    'elscreen-toggle-display-screen-number)`
- L249: `(define-key elscreen-map "T"    'elscreen-toggle-display-tab)`
- L250: `(define-key elscreen-map "?"    'elscreen-help)`
- L251: `(define-key elscreen-map "v"    'elscreen-display-version)`
- L252: `(define-key elscreen-map "j"    'elscreen-link)`
- L253: `(define-key elscreen-map "s"    'elscreen-split)`
- L255: `(defun elscreen-set-prefix-key (prefix-key)`
- L258: `(global-set-key elscreen-prefix-key`
- L261: `(define-key minibuffer-local-map elscreen-prefix-key`
- L267: `(global-set-key prefix-key elscreen-map)`
- L268: `(define-key minibuffer-local-map prefix-key 'undefined)`
- L302: `(defun elscreen--put-alist (key value alist)`
- L313: `(defun elscreen--set-alist (symbol key value)`
- L319: `(defun elscreen--del-alist (key alist)`
- L327: `(defun elscreen-window-history-supported-p ()`
- L333: `(defun elscreen-get-all-window-history-alist ()`
- L341: `(defun elscreen-restore-all-window-history-alist (history-alist)`
- L353: `(defun elscreen--remove-alist (symbol key)`
- L363: `(defun elscreen-current-window-configuration ()`
- L366: `(defun elscreen-default-window-configuration ()`
- L379: `(defun elscreen-apply-window-configuration (elscreen-window-configuration)`
- L391: `(defun elscreen-copy-tree-1 (tree)`
- L401: `(defmacro elscreen-save-screen-excursion (&rest body)`
- L429: `(defun elscreen-make-frame-confs (frame &optional keep-window-configuration)`
- L453: `(defun elscreen-delete-frame-confs (frame)`
- L466: `(defun elscreen-get-screen-property (screen)`
- L470: `(defun elscreen-set-screen-property (screen property)`
- L475: `(defun elscreen-delete-screen-property (screen)`
- L480: `(defun elscreen-get-number-of-screens ()`
- L484: `(defun elscreen-one-screen-p ()`
- L488: `(defun elscreen-get-screen-list ()`
- L492: `(defun elscreen-screen-live-p (screen)`
- L496: `(defun elscreen-get-window-configuration (screen)`
- L502: `(defun elscreen-set-window-configuration (screen winconf)`
- L508: `(defun elscreen-get-screen-nickname (screen)`
- L513: `(defun elscreen-set-screen-nickname (screen nickname)`
- L519: `(defun elscreen-delete-screen-nickname (screen)`
- L525: `(defun elscreen-append-screen-to-history (screen)`
- L529: `(defun elscreen-delete-screen-from-history (screen)`
- L534: `(defun elscreen-set-current-screen (screen)`
- L539: `(defun elscreen-get-current-screen ()`
- L542: `(defun elscreen-get-previous-screen ()`
- L545: `(defun elscreen-status-label (screen &optional default)`
- L555: `(defmacro elscreen-notify-screen-modification-suppress (&rest body)`
- L560: `(defun elscreen-run-screen-update-hook ()`
- L566: `(defun elscreen-screen-modified-p (inquirer)`
- L573: `(defun elscreen-set-screen-modified ()`
- L578: `(defun elscreen-notify-screen-modification (&optional mode)`
- L594: `(defmacro elscreen-screen-modified-hook-setup (&rest hooks-and-functions)`
- L625: `(defun elscreen-get-screen-to-name-alist-cache ()`
- L628: `(defun elscreen-set-screen-to-name-alist-cache (alist)`
- L633: `(defun elscreen-rebuild-mode-to-nickname-alist ()`
- L639: `(defun elscreen-set-mode-to-nickname-alist (mode-to-nickname-alist-symbol)`
- L647: `(defun elscreen-rebuild-buffer-to-nickname-alist ()`
- L653: `(defun elscreen-set-buffer-to-nickname-alist (buffer-to-nickname-alist-symbol)`
- L681: `(defun elscreen-get-screen-to-name-alist (&optional truncate-length padding)`
- L742: `(defun elscreen-truncate-screen-name (screen-name truncate-length &optional padding)`
- L754: `(defun elscreen-goto-internal (screen)`
- L762: `(defun elscreen-create-internal (&optional noerror)`
- L786: `(defun elscreen-kill-internal (screen)`
- L791: `(defun elscreen-find-screens (condition)`
- L807: `(defun elscreen-find-screen (condition)`
- L813: `(defun elscreen-find-screen-by-buffer (buffer &optional create)`
- L836: `(defun elscreen-find-screen-by-major-mode (major-mode-or-re)`
- L860: `(defun elscreen-message (message &optional sec)`
- L872: `(defun elscreen-create ()`
- L879: `(defun elscreen-clone (&optional screen)`
- L897: `(defun elscreen-kill (&optional screen)`
- L917: `(defun elscreen-kill-screen-and-buffers (&optional screen)`
- L934: `(defun elscreen-kill-others (&optional screen)`
- L964: `(defun elscreen-goto (screen)`
- L982: `(defun elscreen-next ()`
- L997: `(defun elscreen-previous ()`
- L1012: `(defun elscreen-toggle ()`
- L1023: `(defun elscreen-jump ()`
- L1032: `(defun elscreen-swap ()`
- L1049: `(defun elscreen-screen-nickname (nickname)`
- L1059: `(defun elscreen-display-screen-name-list ()`
- L1077: `(defun elscreen-set-help (help-symbol)`
- L1081: `(defun elscreen-help ()`
- L1093: `(defun elscreen-display-version ()`
- L1098: `(defun elscreen-toggle-display-screen-number ()`
- L1104: `(defun elscreen-toggle-display-tab ()`
- L1110: `(defun elscreen-display-last-message ()`
- L1115: `(defun elscreen-display-time ()`
- L1127: `(defun elscreen-select-and-goto ()`
- L1189: `(define-key minibuffer-map "\C-g" 'abort-recursive-edit)`
- L1190: `(define-key minibuffer-map "\C-m" 'exit-recursive-edit)`
- L1191: `(define-key minibuffer-map "q" 'exit-recursive-edit)`
- L1192: `(define-key minibuffer-map " " 'exit-recursive-edit)`
- L1195: `(define-key minibuffer-map (car command) 'self-insert-and-exit))`
- L1199: `(define-key minibuffer-map (number-to-string screen)`
- L1215: `(defun elscreen-find-and-goto-by-buffer (&optional buffer create noselect)`
- L1234: `(defun elscreen-find-file (filename)`
- L1241: `(defun elscreen-find-file-read-only (filename)`
- L1249: `(defun elscreen-dired (dirname &optional switches)`
- L1255: `(defun elscreen-execute-extended-command (prefix-arg)`
- L1293: `(defun elscreen-mode-line-update ()`
- L1372: `(defun elscreen-menu-bar-update (&optional force)`
- L1397: `(define-key (current-global-map) [menu-bar elscreen]`
- L1424: `(define-key keymap (vector 'header-line key) function)))`
- L1439: `(defun elscreen-tab-escape-% (string)`
- L1453: `(defun elscreen-tab-update (&optional force)`
- L1557: `(defun elscreen-link ()`
- L1574: `(defun elscreen-split ()`
- L1588: `(defun elscreen-start ()`
- L1598: `(provide 'elscreen)`
