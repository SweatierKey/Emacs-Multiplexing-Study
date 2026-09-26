# Indice del codice: yaxception

Fonte: https://github.com/aki2o/yaxception.git

Revisione: `5941de88b19752c14e0dce0d2bf562b1288055a0`.


## yaxception.el

- L37: `(require 'cl-lib)`
- L38: `(require 'backtrace)`
- L39: `(require 'dash)`
- L53: `(defun yaxception:toggle-debug-enable ()`
- L58: `(defun yaxception:clear-debug-log ()`
- L71: `(defun yaxception-signal-hook-function (error-symbol data)`
- L146: `(defun yaxception:get-raw (err)`
- L151: `(defun yaxception:get-text (err)`
- L155: `(defun yaxception:get-data (err)`
- L159: `(defun yaxception:get-prop (err name)`
- L164: `(cl-defun yaxception:get-stack-trace-string (err &key (filter nil) (limit nil))`
- L180: `(defun yaxception-expose-stack-traces (err)`
- L197: `(provide 'yaxception)`
