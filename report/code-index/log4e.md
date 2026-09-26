# Indice del codice: log4e

Fonte: https://github.com/aki2o/log4e.git

Revisione: `6d71462df9bf595d3861bfb328377346aceed422`.


## log4e.el

- L33: `(require 'cl-lib)`
- L34: `(require 'rx)`
- L54: `(defmacro log4e--def-symmaker (symnm)`
- L70: `(defmacro log4e--def-level-logger (prefix suffix level)`
- L181: `(defun log4e--logging (buffnm codsys logtmpl timetmpl minlevel maxlevel logging-p level msg &rest msgargs)`
- L204: `(defun log4e--get-current-log-line-level ()`
- L210: `(defun log4e--clear-log (buffnm)`
- L216: `(defun log4e--open-log (buffnm)`
- L225: `(defun log4e--open-log-if-debug (buffnm dbg)`
- L237: `(defmacro log4e:deflogger (prefix msgtmpl timetmpl &optional log-function-name-custom-alist)`
- L484: `(define-derived-mode log4e-mode view-mode "Log4E"`
- L489: `(define-key log4e-mode-map (kbd "J") 'log4e:next-log)`
- L490: `(define-key log4e-mode-map (kbd "K") 'log4e:previous-log))`
- L492: `(defun log4e:next-log ()`
- L502: `(defun log4e:previous-log ()`
- L513: `(defun log4e:insert-start-log-quickly ()`
- L556: `(provide 'log4e)`
