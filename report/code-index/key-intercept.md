# Indice del codice: key-intercept

Fonte: https://github.com/tarao/key-intercept-el.git

Revisione: `d9a60edb4ce893f2d3d94f242164fdcc62d43cf2`.


## key-intercept.el

- L32: `(defcustom key-intercept-delay 0.5`
- L37: `(defcustom key-intercept-echo-keystrokes 0`
- L46: `(defcustom key-intercept-fake-keystrokes t`
- L53: `(defvar key-intercept-map (make-sparse-keymap))`
- L55: `(defvar key-intercept-prefix-map (make-keymap))`
- L57: `(defvar key-intercept-global-map (make-sparse-keymap))`
- L59: `(defvar key-intercept-pass-map (make-keymap))`
- L61: `(defvar key-intercept-emulation-map-alist`
- L65: `(defvar key-intercept-intercept-map-alist`
- L70: `(defun key-intercept-make-local ()`
- L109: `(defun key-intercept-make-local-maybe ()`
- L114: `(define-minor-mode key-intercept-mode`
- L129: `(defun key-intercept-on ()`
- L134: `(defun key-intercept-make-key-str (key)`
- L137: `(defun key-intercept-make-prefix-event (key)`
- L140: `(defun key-intercept-make-intercept-event (key)`
- L143: `(defun key-intercept-raw-key (key)`
- L154: `(defun key-intercept-raw-keys (keys)`
- L157: `(defun key-intercept-echo-keys (&optional keys)`
- L164: `(defun key-intercept-read-event (delay)`
- L172: `(defun key-intercept-this-command-keys ()`
- L177: `(defun key-intercept-command-end ()`
- L188: `(defun key-intercept-replace-kbd-macro (&optional events)`
- L207: `(defun key-intercept-initial-command (arg)`
- L215: `(defun key-intercept-prefix-command (key delay)`
- L238: `(defun key-intercept-make-prefix-command (key delay)`
- L243: `(defun key-intercept-run-original-command (keys)`
- L248: `(defun key-intercept-pass-through (arg)`
- L253: `(defun define-modal-intercept-key (key mode def &optional delay)`
- L269: `(define-key map key def)`
- L271: `(define-key key-intercept-map (vector initial)`
- L279: `(define-key key-intercept-prefix-map (vector pevent)`
- L281: `(define-key key-intercept-pass-map (vector ievent)`
- L285: `(define-key map (vector ievent) def)))`
- L288: `(defun define-intercept-key (key def &optional delay)`
- L294: `(provide 'key-intercept)`
