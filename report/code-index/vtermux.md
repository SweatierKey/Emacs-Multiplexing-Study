# Indice del codice: vtermux

Fonte: https://github.com/pcmantz/vtermux.git

Revisione: `98db8bfde835ba2c100e5dd835d5772ab2becf0a`.


## vtermux-test.el

- L3: `(require 'ert)`
- L4: `(require 'cl-lib)`
- L9: `(provide 'vterm)`
- L16: `(require 'vtermux)`
- L36: `(defun vtermux-test--make-buffer (name)`
- L42: `(defun vtermux-test--with-mocks (fn)`
- L71: `(defun vtermux-test--capture-vterm-shell (&rest _)`

## vtermux.el

- L55: `(require 'cl-lib)`
- L61: `(defun vtermux--detect-backend ()`
- L68: `(defcustom vtermux-backend (vtermux--detect-backend)`
- L75: `(defcustom vtermux-kill-buffer-on-exit t`
- L80: `(defcustom vtermux-command-directory :project`
- L100: `(defun vtermux-register-backend (name create-fn)`
- L111: `(defun vtermux--shell-string (prog args)`
- L154: `(defun vtermux--command-directory (&optional method prompt)`
- L175: `(defun vtermux--next-label (buffers)`
- L195: `(defun vtermux--format-buffer-name (bufname directory &optional label)`
- L204: `(defun vtermux--buffers (bufname buf-list &optional directory)`
- L216: `(defun vtermux--create-buffer (prog bufname args buf-list-sym directory &optional label backend)`
- L249: `(defun vtermux--launch (prog bufname args buf-list-sym directory &optional backend)`
- L264: `(defun vtermux--launch-new (prog bufname args buf-list-sym directory &optional backend)`
- L275: `(defun vtermux--select (prog buf-list-sym)`
- L286: `(defun vtermux--cycle (prog bufname args buf-list-sym directory direction offset &optional backend)`
- L309: `(defun vtermux--next-key (name)`
- L329: `(defmacro vtermux-define (name &rest args)`
- L467: `'((define-key global-map (kbd ,bind-key) #',fn)))`
- L471: `(defun vtermux-run (&optional arg)`
- L513: `(provide 'vtermux)`
