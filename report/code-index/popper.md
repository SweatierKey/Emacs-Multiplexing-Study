# Indice del codice: popper

Fonte: https://github.com/karthink/popper.git

Revisione: `d83b894ee7a9daf7c8e9b864c23d08f1b23d78f6`.


## popper-echo.el

- L55: `(require 'popper)`
- L57: `(defcustom popper-echo-transform-function nil`
- L75: `(defcustom popper-echo-dispatch-persist t`
- L80: `(defcustom popper-echo-dispatch-actions nil`
- L93: `(defcustom popper-echo-dispatch-keys '("M-0" "M-1" "M-2" "M-3" "M-4"`
- L131: `(defun popper-echo--dispatch-toggle (i buf-list repeat)`
- L145: `(defun popper-echo--dispatch-kill (i buf-list repeat)`
- L159: `(defun popper-echo--dispatch-raise (i buf-list repeat)`
- L173: `(defun popper-echo--popup-info ()`
- L183: `(defun popper-echo--activate-keymap (buffers repeat)`
- L194: `(define-key map (kbd rawkey) (popper-echo--dispatch-toggle i buffers repeat))`
- L196: `(define-key map (kbd (concat "k " rawkey))`
- L198: `(define-key map (kbd (concat "^ " rawkey))`
- L203: `(defun popper-echo ()`
- L255: `(define-minor-mode popper-echo-mode`
- L283: `(defun popper-tab-line--format (tab tabs)`
- L295: `(defun popper-tab-line--ensure ()`
- L315: `(define-minor-mode popper-tab-line-mode`
- L348: `(provide 'popper-echo)`

## popper.el

- L77: `(require 'cl-lib)`
- L78: `(require 'seq)`
- L93: `(defcustom popper-reference-buffers '("\\*Messages\\*$")`
- L132: `(defcustom popper-mode-line '(:eval (propertize " POP" 'face 'mode-line-emphasis))`
- L141: `(defcustom popper-mode-line-position 0`
- L145: `(defcustom popper-display-control t`
- L155: `(defcustom popper-display-function #'popper-select-popup-at-bottom`
- L166: `(defcustom popper-group-function nil`
- L191: `(defcustom popper-window-height #'popper--fit-window-height`
- L213: `(defcustom popper-open-popup-hook nil`
- L258: `(defun popper--fit-window-height (win)`
- L265: `(defun popper-select-popup-at-bottom (buffer &optional alist)`
- L273: `(defun popper-display-popup-at-bottom (buffer &optional alist)`
- L285: `(defun popper-popup-p (buf)`
- L294: `(defun popper-display-control-p (buf &optional _act)`
- L308: `(defun popper-group-by-directory ()`
- L318: `(defun popper-group-by-project ()`
- L327: `(defun popper-group-by-projectile ()`
- L337: `(defun popper-group-by-perspective ()`
- L347: `(defun popper--find-popups (test-buffer-list)`
- L371: `(defun popper--update-popups ()`
- L407: `(defun popper--find-buried-popups ()`
- L427: `(defun popper-close-latest ()`
- L449: `(defun popper-open-latest (&optional group)`
- L473: `(defun popper--delete-popup (win)`
- L486: `(defun popper--modified-mode-line ()`
- L498: `(defun popper--restore-mode-lines (win-buf-alist)`
- L508: `(defun popper--bury-all ()`
- L513: `(defun popper--open-all ()`
- L523: `(defun popper-toggle (&optional arg)`
- L549: `(defun popper-cycle (&optional num)`
- L573: `(defun popper-cycle-backwards (&optional num)`
- L580: `(defun popper-raise-popup (&optional buffer)`
- L592: `(defun popper-lower-to-popup (&optional buffer)`
- L606: `(defun popper-toggle-type (&optional buffer)`
- L617: `(defun popper-kill-latest-popup ()`
- L627: `(defun popper--suppress-p (buf)`
- L635: `(defun popper--suppress-popups ()`
- L657: `(defun popper--set-reference-vars ()`
- L684: `(define-minor-mode popper-mode`
- L730: `(provide 'popper)`
