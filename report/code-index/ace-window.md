# Indice del codice: ace-window

Fonte: https://github.com/abo-abo/ace-window.git

Revisione: `77115afc1b0b9f633084cf7479c767988106c196`.


## ace-window-posframe.el

- L5: `(require 'ace-window)`
- L17: `(defun aw--lead-overlay-posframe (path leaf)`
- L37: `(defun aw--remove-leading-chars-posframe ()`
- L42: `(defun ace-window-posframe-enable ()`
- L49: `(defun ace-window-posframe-disable ()`
- L54: `(define-minor-mode ace-window-posframe-mode`
- L64: `(provide 'ace-window-posframe)`

## ace-window.el

- L38: `;;    (global-set-key (kbd "M-o") 'ace-window)`
- L65: `(require 'avy)`
- L66: `(require 'ring)`
- L67: `(require 'subr-x)`
- L75: `(defcustom aw-keys '(?1 ?2 ?3 ?4 ?5 ?6 ?7 ?8 ?9)`
- L79: `(defcustom aw-scope 'global`
- L86: `(defcustom aw-translate-char-function #'identity`
- L95: `(defcustom aw-minibuffer-flag nil`
- L99: `(defcustom aw-ignored-buffers '("*Calc Trail*" " *LV*")`
- L104: `(defcustom aw-ignore-on t`
- L109: `(defcustom aw-ignore-current nil`
- L113: `(defcustom aw-background t`
- L117: `(defcustom aw-leading-char-style 'char`
- L123: `(defcustom aw-dispatch-always nil`
- L129: `(defcustom aw-dispatch-when-more-than 2`
- L133: `(defcustom aw-reverse-frame-list nil`
- L138: `(defcustom aw-frame-offset '(13 . 23)`
- L143: `(defcustom aw-frame-size nil`
- L149: `(defcustom aw-char-position 'top-left`
- L179: `(defun aw-set-make-frame-char (option value)`
- L191: `(defcustom aw-make-frame-char ?z`
- L220: `(defun aw-ignored-p (window)`
- L241: `(defun aw-window-list ()`
- L285: `(defun aw--done ()`
- L305: `(defun aw--restore-windows-hscroll ()`
- L316: `(defun aw--overlay-str (wnd pos path)`
- L345: `(defun aw--point-visible-p ()`
- L352: `(defun aw--lead-overlay (path leaf)`
- L413: `(defun aw--remove-leading-chars ()`
- L419: `(defun aw--make-backgrounds (wnd-list)`
- L438: `(defun aw-set-mode-line (str)`
- L445: `(defun aw--dispatch-action (char)`
- L449: `(defun aw-make-frame ()`
- L476: `(defun aw-use-frame (window)`
- L484: `(defun aw-clean-up-avy-current-path ()`
- L494: `(defun aw-dispatch-default (char)`
- L528: `(defcustom aw-display-mode-overlay t`
- L534: `(defun aw-select (mode-line &optional action)`
- L596: `(defun ace-select-window ()`
- L603: `(defun ace-delete-window ()`
- L610: `(defun ace-swap-window ()`
- L617: `(defun ace-delete-other-windows ()`
- L624: `(defun ace-display-buffer (buffer alist)`
- L640: `(defun aw-transpose-frame (w)`
- L645: `(defun ace-window (arg)`
- L680: `(defun aw-window< (wnd1 wnd2)`
- L705: `(defun aw--push-window (window)`
- L713: `(defun aw--pop-window ()`
- L728: `(defun aw-switch-to-window (window)`
- L739: `(defun aw-flip-window ()`
- L744: `(defun aw-show-dispatch-help ()`
- L763: `(defun aw-delete-window (window &optional kill-buffer)`
- L779: `(defun aw-switch-buffer-in-window (window)`
- L786: `(defun aw--switch-buffer ()`
- L794: `(defcustom aw-swap-invert nil`
- L798: `(defun aw-swap-window (window)`
- L819: `(defun aw-move-window (window)`
- L827: `(defun aw-copy-window (window)`
- L837: `(defun aw-split-window-vert (window)`
- L842: `(defun aw-split-window-horz (window)`
- L847: `(defcustom aw-fair-aspect-ratio 2`
- L853: `(defun aw-split-window-fair (window)`
- L862: `(defun aw-switch-buffer-other-window (window)`
- L869: `(defun aw-execute-command-other-window (window)`
- L879: `(defun aw--face-rel-height ()`
- L891: `(defun aw-offset (window)`
- L914: `(defun aw--after-make-frame (f)`
- L920: `(define-minor-mode ace-window-display-mode`
- L945: `(defun aw-update ()`
- L963: `(provide 'ace-window)`
