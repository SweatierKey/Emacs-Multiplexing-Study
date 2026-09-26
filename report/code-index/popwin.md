# Indice del codice: popwin

Fonte: https://github.com/emacsorphanage/popwin.git

Revisione: `b67254bef763ffa5ab781460bc47d6adf6f87127`.


## misc/popwin-browse-kill-ring.el

- L27: `(require 'popwin)`
- L29: `(defun popwin-bkr:update-window-reference ()`
- L34: `(provide 'popwin-browse-kill-ring)`

## misc/popwin-pp.el

- L27: `(require 'popwin)`
- L28: `(require 'pp)`
- L41: `(provide 'popwin-pp)`

## misc/popwin-term.el

- L27: `(require 'popwin)`
- L29: `(defun popwin-term:term ()`
- L37: `(provide 'popwin-term)`

## misc/popwin-w3m.el

- L27: `(require 'popwin)`
- L28: `(require 'browse-url)`
- L29: `(require 'w3m)`
- L31: `(defcustom popwin-w3m:w3m-special-display-config nil`
- L39: `(defun popwin-w3m:w3m-browse-url (url &optional new-session)`
- L51: `(provide 'popwin-w3m)`

## misc/popwin-yatex.el

- L31: `(require 'popwin)`
- L32: `(require 'yatex)`
- L39: `(provide 'popwin-yatex)`

## popwin.el

- L58: `;;     (global-set-key (kbd "C-z") popwin:keymap)`
- L75: `(defun popwin:listify (object)`
- L79: `(defun popwin:subsitute-in-tree (map tree)`
- L86: `(defun popwin:get-buffer (buffer-or-name &optional if-not-found)`
- L100: `(defun popwin:switch-to-buffer (buffer-or-name &optional norecord)`
- L108: `(defun popwin:select-window (window &optional norecord)`
- L114: `(defun popwin:buried-buffer-p (buffer)`
- L118: `(defun popwin:window-point (window)`
- L126: `(defun popwin:window-deletable-p (window)`
- L133: `(defmacro popwin:save-selected-window (&rest body)`
- L137: `(defun popwin:minibuffer-window-selected-p ()`
- L141: `(defun popwin:last-selected-window ()`
- L157: `(defun popwin:dummy-buffer ()`
- L163: `(defun popwin:kill-dummy-buffer ()`
- L169: `(defun popwin:window-trailing-edge-adjustable-p (window)`
- L176: `(cl-defun popwin:adjust-window-edges (window`
- L194: `(defun popwin:window-config-tree-1 (node)`
- L213: `(defun popwin:window-config-tree ()`
- L220: `(defun popwin:replicate-window-config (window node hfactor vfactor)`
- L246: `(defun popwin:restore-window-outline (node outline)`
- L274: `(defun popwin:position-horizontal-p (position)`
- L278: `(defun popwin:position-vertical-p (position)`
- L282: `(defun popwin:create-popup-window-1 (window size position)`
- L301: `(cl-defun popwin:create-popup-window (&optional (size 15) (position 'bottom) (adjust t))`
- L348: `(defcustom popwin:popup-window-position 'bottom`
- L354: `(defcustom popwin:popup-window-width 30`
- L362: `(defcustom popwin:popup-window-height 15`
- L370: `(defcustom popwin:reuse-window 'current`
- L377: `(defcustom popwin:adjust-other-windows t`
- L413: `(defvar popwin:window-map nil`
- L467: `(defun popwin:popup-window-live-p ()`
- L471: `(cl-defun popwin:update-window-reference (symbol`
- L483: `(defun popwin:start-close-popup-window-timer ()`
- L491: `(defun popwin:stop-close-popup-window-timer ()`
- L497: `(defun popwin:close-popup-window-timer ()`
- L505: `(defun popwin:close-popup-window (&optional keep-selected)`
- L527: `(defun popwin:close-popup-window-if-necessary ()`
- L624: `(cl-defun popwin:popup-buffer (buffer`
- L682: `(defun popwin:popup-last-buffer (&optional noselect)`
- L694: `(defun popwin:select-popup-window ()`
- L701: `(defun popwin:stick-popup-window ()`
- L716: `(defmacro popwin:without-special-displaying (&rest body)`
- L728: `(defcustom popwin:special-display-config`
- L828: `(defun popwin:apply-display-buffer (function buffer &optional not-this-window)`
- L853: `(defun popwin:original-display-buffer (buffer &optional not-this-window)`
- L857: `(defun popwin:original-pop-to-buffer (buffer &optional not-this-window)`
- L861: `(defun popwin:original-display-last-buffer ()`
- L868: `(defun popwin:switch-to-last-buffer ()`
- L877: `(defun popwin:original-pop-to-last-buffer ()`
- L884: `(defun popwin:reuse-window-p (buffer-or-name not-this-window)`
- L894: `(cl-defun popwin:match-config (buffer)`
- L912: `(cl-defun popwin:display-buffer-1 (buffer-or-name`
- L945: `(defun popwin:display-buffer (buffer-or-name &optional not-this-window)`
- L962: `(defun popwin:special-display-popup-window (buffer &rest ignore)`
- L966: `(cl-defun popwin:pop-to-buffer-1 (buffer`
- L978: `(defun popwin:pop-to-buffer (buffer &optional other-window norecord)`
- L993: `(defcustom popwin:universal-display-config '(t)`
- L1000: `(defun popwin:universal-display ()`
- L1015: `(defun popwin:one-window ()`
- L1023: `(defun popwin:popup-buffer-tail (&rest same-as-popwin:popup-buffer)`
- L1031: `(defun popwin:find-file (filename &optional wildcards)`
- L1040: `(defun popwin:find-file-tail (file &optional wildcard)`
- L1049: `(defun popwin:messages ()`
- L1059: `(defun popwin:display-buffer-condition (buffer action)`
- L1063: `(defun popwin:display-buffer-action (buffer alist)`
- L1069: `(define-minor-mode popwin-mode`
- L1089: `(defvar popwin:keymap`
- L1091: `(define-key map "b"    'popwin:popup-buffer)`
- L1092: `(define-key map "l"    'popwin:popup-last-buffer)`
- L1093: `(define-key map "o"    'popwin:display-buffer)`
- L1094: `(define-key map "\C-b" 'popwin:switch-to-last-buffer)`
- L1095: `(define-key map "\C-p" 'popwin:original-pop-to-last-buffer)`
- L1096: `(define-key map "\C-o" 'popwin:original-display-last-buffer)`
- L1097: `(define-key map " "    'popwin:select-popup-window)`
- L1098: `(define-key map "s"    'popwin:stick-popup-window)`
- L1099: `(define-key map "0"    'popwin:close-popup-window)`
- L1100: `(define-key map "f"    'popwin:find-file)`
- L1101: `(define-key map "\C-f" 'popwin:find-file)`
- L1102: `(define-key map "e"    'popwin:messages)`
- L1103: `(define-key map "\C-u" 'popwin:universal-display)`
- L1104: `(define-key map "1"    'popwin:one-window)`
- L1108: `\(global-set-key (kbd \"C-z\") popwin:keymap\)`
- L1128: `(provide 'popwin)`
