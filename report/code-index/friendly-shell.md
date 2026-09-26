# Indice del codice: friendly-shell

Fonte: https://github.com/p3r7/friendly-shell.git

Revisione: `5cafa3f6313ce04a47c8996ea1ac6b617d155d46`.


## friendly-remote-shell.el

- L33: `(require 'cl-lib)`
- L35: `(require 'tramp)`
- L36: `(require 'tramp-sh)`
- L38: `(require 'friendly-tramp-path)`
- L39: `(require 'with-shell-interpreter)`
- L40: `(require 'friendly-shell)`
- L54: `(defmacro friendly-remote-shell--make-tramp-file-name (vec)`
- L83: `(cl-defun friendly-remote-shell (&key path`
- L113: `(defun friendly-remote-shell-register-display-same-window ()`
- L124: `(provide 'friendly-remote-shell)`

## friendly-shell-command.el

- L36: `(require 'cl-lib)`
- L37: `(require 'dash)`
- L39: `(require 'tramp)`
- L40: `(require 'tramp-sh)`
- L42: `(require 'with-shell-interpreter)`
- L49: `(cl-defun friendly-shell-command-to-string (command &key path interpreter command-switch)`
- L63: `(cl-defun friendly-shell-command-async (command &key output-buffer error-buffer`
- L116: `(cl-defun friendly-shell-command (command &key output-buffer error-buffer`
- L158: `(defun friendly-shell-command--kill-buffer-sentinel (process _output)`
- L163: `(cl-defun friendly-shell-command--build-process-sentinel (process &key sentinel callback kill-buffer)`
- L187: `(provide 'friendly-shell-command)`

## friendly-shell.el

- L32: `(require 'cl-lib)`
- L33: `(require 'dash)`
- L35: `(require 'tramp)`
- L36: `(require 'tramp-sh)`
- L38: `(require 'with-shell-interpreter)`
- L65: `(cl-defun friendly-shell (&key path`
- L151: `(defun friendly-shell--generate-buffer-name (is-remote interpreter path)`
- L158: `(defun friendly-shell--generate-buffer-name-local (&optional interpreter _path)`
- L164: `(defun friendly-shell--generate-buffer-name-remote (&optional _interpreter path)`
- L169: `(defun friendly-shell--tramp-hop-paths-from-vec (vec)`
- L175: `(defun friendly-shell--tramp-hop-paths (path)`
- L179: `(defun friendly-shell--generate-buffer-name-remote-from-vec (vec)`
- L193: `(defun friendly-shell--stty-echo-p (explicit-interpreter-args)`
- L206: `(defun friendly-shell--maybe-register-buffer-display-same-win (basename)`
- L218: `(provide 'friendly-shell)`
