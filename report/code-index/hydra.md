# Indice del codice: hydra

Fonte: https://github.com/abo-abo/hydra.git

Revisione: `59a2a45a35027948476d1d7751b0f0215b1e61aa`.


## .dir-locals.el


## hydra-examples.el

- L32: `(require 'hydra)`
- L50: `;;     (global-set-key (kbd "<f2> g") 'hydra-zoom/text-scale-increase)`
- L51: `;;     (global-set-key (kbd "<f2> l") 'hydra-zoom/text-scale-decrease)`
- L56: `;;     (define-key emacs-lisp-mode-map [f2 103]`
- L58: `;;     (define-key emacs-lisp-mode-map [f2 108]`
- L110: `;;     (global-set-key (kbd "C-c C-v a") 'abbrev-mode)`
- L111: `;;     (global-set-key (kbd "C-c C-v d") 'toggle-debug-on-error)`
- L121: `(defun hydra-vi/pre ()`
- L124: `(defun hydra-vi/post ()`
- L184: `;; (global-set-key (kbd "C-c C-v") 'hydra-toggle/body)`
- L224: `;; (define-key Buffer-menu-mode-map "." 'hydra-buffer-menu/body)`
- L228: `(defvar dired-mode-map)`
- L261: `;; (global-set-key (kbd "C-c h") 'hydra-apropos/body)`
- L264: `(require 'rect)`
- L292: `;; (global-set-key (kbd "C-x SPC") 'hydra-rectangle/body)`
- L295: `(defun org-agenda-cts ()`
- L334: `;; (define-key org-agenda-mode-map "v" 'hydra-org-agenda-view/body)`
- L344: `(require 'windmove)`
- L346: `(defun hydra-move-splitter-left (arg)`
- L354: `(defun hydra-move-splitter-right (arg)`
- L362: `(defun hydra-move-splitter-up (arg)`
- L370: `(defun hydra-move-splitter-down (arg)`
- L379: `(defun hydra-ex-point-mark ()`
- L388: `(provide 'hydra-examples)`

## hydra-ox.el

- L28: `(require 'hydra)`
- L29: `(require 'org)`
- L123: `(define-key org-mode-map (kbd "C-c C-,") 'hydra-ox/body)`
- L125: `(provide 'hydra-ox)`

## hydra-test.el

- L27: `(require 'ert)`
- L28: `(require 'hydra)`
- L225: `(define-key global-map (kbd "M-g")`
- L227: `(define-key global-map [134217831 104]`
- L229: `(define-key global-map [134217831 106]`
- L231: `(define-key global-map [134217831 107]`
- L1379: `(defun remapable-print ()`
- L1382: `(defun remaped-print ()`
- L1385: `(define-key global-map (kbd "C-=") 'remapable-print)`
- L1386: `(define-key global-map [remap remapable-print] 'remaped-print)`
- L1392: `(defmacro hydra-with (in &rest body)`
- L1719: `(provide 'hydra-test)`

## hydra.el

- L64: `;;     (global-set-key (kbd "C-c C-v") 'hydra-toggle/body)`
- L83: `(require 'cl-lib)`
- L84: `(require 'lv)`
- L85: `(require 'ring)`
- L87: `(defvar hydra-curr-map nil`
- L107: `(defun hydra-set-transient-map (keymap on-exit &optional foreign-keys)`
- L126: `(defun hydra--clearfun ()`
- L149: `(defun hydra-disable ()`
- L190: `(defun hydra-amaranth-warn ()`
- L201: `(defcustom hydra-is-helpful t`
- L206: `(defcustom hydra-default-hint ""`
- L225: `(defun hydra-posframe-show (str)`
- L235: `(defun hydra-posframe-hide ()`
- L250: `(defcustom hydra-hint-display-type 'lv`
- L258: `(defcustom hydra-verbose nil`
- L262: `(defcustom hydra-key-format-spec "%s"`
- L267: `(defcustom hydra-doc-format-spec "%s"`
- L271: `(defcustom hydra-look-for-remap nil`
- L313: `(defun hydra-add-font-lock ()`
- L325: `(defun hydra-add-imenu ()`
- L334: `(defvar hydra-base-map`
- L336: `(define-key map (kbd "<f1> k") 'hydra--describe-key)`
- L337: `(define-key map [?\C-u] 'hydra--universal-argument)`
- L338: `(define-key map [?-] 'hydra--negative-argument)`
- L339: `(define-key map [?0] 'hydra--digit-argument)`
- L340: `(define-key map [?1] 'hydra--digit-argument)`
- L341: `(define-key map [?2] 'hydra--digit-argument)`
- L342: `(define-key map [?3] 'hydra--digit-argument)`
- L343: `(define-key map [?4] 'hydra--digit-argument)`
- L344: `(define-key map [?5] 'hydra--digit-argument)`
- L345: `(define-key map [?6] 'hydra--digit-argument)`
- L346: `(define-key map [?7] 'hydra--digit-argument)`
- L347: `(define-key map [?8] 'hydra--digit-argument)`
- L348: `(define-key map [?9] 'hydra--digit-argument)`
- L349: `(define-key map [kp-0] 'hydra--digit-argument)`
- L350: `(define-key map [kp-1] 'hydra--digit-argument)`
- L351: `(define-key map [kp-2] 'hydra--digit-argument)`
- L352: `(define-key map [kp-3] 'hydra--digit-argument)`
- L353: `(define-key map [kp-4] 'hydra--digit-argument)`
- L354: `(define-key map [kp-5] 'hydra--digit-argument)`
- L355: `(define-key map [kp-6] 'hydra--digit-argument)`
- L356: `(define-key map [kp-7] 'hydra--digit-argument)`
- L357: `(define-key map [kp-8] 'hydra--digit-argument)`
- L358: `(define-key map [kp-9] 'hydra--digit-argument)`
- L359: `(define-key map [kp-subtract] 'hydra--negative-argument)`
- L363: `(defun hydra--universal-argument (arg)`
- L372: `(defun hydra--digit-argument (arg)`
- L391: `(defun hydra--negative-argument (arg)`
- L398: `(defun hydra--describe-key ()`
- L414: `(defun hydra-repeat (&optional arg)`
- L427: `(defun hydra--callablep (x)`
- L433: `(defun hydra--make-callable (x)`
- L446: `(defun hydra-plist-get-default (plist prop default)`
- L457: `(defun hydra--head-property (h prop &optional default)`
- L462: `(defun hydra--head-set-property (h prop value)`
- L466: `(defun hydra--head-has-property (h prop)`
- L470: `(defun hydra--body-foreign-keys (body)`
- L479: `(defun hydra--body-exit (body)`
- L488: `(defun hydra--normalize-body (body)`
- L505: `(defun hydra-default-pre ()`
- L524: `(defun hydra-keyboard-quit ()`
- L542: `(defun hydra-key-doc-function-default (key key-width doc doc-width)`
- L549: `(defun hydra--to-string (x)`
- L554: `(defun hydra--eval-and-format (x)`
- L562: `(defun hydra--hint-heads-wocol (body heads)`
- L614: `(defun hydra--hint (body heads)`
- L633: `(defun hydra-fontify-head-default (head body)`
- L662: `(defun hydra-fontify-head-greyscale (head _body)`
- L670: `(defun hydra-fontify-head (head body)`
- L675: `(defun hydra--strip-align-markers (str)`
- L701: `(defun hydra--format (_name body docstring heads)`
- L787: `(defun hydra--format-1 (docstring rest varlist)`
- L817: `(defun hydra--complain (format-string &rest args)`
- L823: `(defun hydra--doc (body-key body-name heads)`
- L841: `(defun hydra--call-interactively-remap-maybe (cmd)`
- L851: `(defun hydra--call-interactively (cmd name)`
- L861: `(defun hydra--make-defun (name body doc head`
- L936: `(defun hydra-set-property (name key val)`
- L948: `(defun hydra-get-property (name key)`
- L956: `(defun hydra-show-hint (hint caller)`
- L968: `(defmacro hydra--make-funcall (sym)`
- L973: `(defun hydra--head-name (h name)`
- L988: `(defun hydra--delete-duplicates (heads)`
- L1005: `(defun hydra--pad (lst n)`
- L1012: `(defmacro hydra-multipop (lst n)`
- L1022: `(defun hydra--matrix (lst rows cols)`
- L1031: `(defun hydra--cell (fstr names)`
- L1052: `(defun hydra--vconcat (strs &optional joiner)`
- L1070: `(defun hydra--table (names rows cols &optional cell-formats)`
- L1091: `(defun hydra-reset-radios (names)`
- L1098: `(defun hydra--normalize-heads (heads)`
- L1109: `(defun hydra--sort-heads (normalized-heads)`
- L1131: `(defun hydra--pad-heads (heads-groups padding-head)`
- L1142: `(defun hydra--generate-matrix (heads-groups)`
- L1166: `(defun hydra-interpose (x lst)`
- L1174: `(defun hydra--hint-row (heads body)`
- L1193: `(defun hydra--hint-from-matrix (body heads-matrix)`
- L1203: `(defun hydra--hint-from-matrix-1 (body heads-matrix)`
- L1215: `(defun hydra-idle-message (secs hint name)`
- L1228: `(defun hydra-timeout (secs &optional function)`
- L1245: `(defmacro defhydra (name body &optional docstring &rest heads)`
- L1374: `(define-key keymap (kbd (car x))`
- L1429: `(define-key ,body-map (kbd ,body-key) nil))))`
- L1449: `'(define-key ,bind ,final-key (quote ,name)))`
- L1462: `(defmacro defhydra+ (name body &optional docstring &rest heads)`
- L1477: `(defun hydra--prop (name prop-name)`
- L1480: `(defmacro defhydradio (name _body &rest heads)`
- L1503: `(defun hydra--radio (parent head)`
- L1514: `(defun hydra--quote-maybe (x)`
- L1523: `(defun hydra--cycle-radio (sym)`
- L1544: `(defun hydra-pause-resume ()`
- L1562: `(provide 'hydra)`

## lv.el

- L36: `(require 'cl-lib)`
- L43: `(defcustom lv-use-separator nil`
- L48: `(defcustom lv-use-padding nil`
- L71: `(defun lv-window ()`
- L105: `(defun lv--pad-to-center (str width)`
- L113: `(defun lv-message (format-string &rest args)`
- L139: `(defun lv-delete-window ()`
- L146: `(provide 'lv)`

## targets/hydra-init.el

- L23: `(require 'hydra)`
- L25: `(require 'hydra-examples)`
- L26: `(require 'hydra-test)`
