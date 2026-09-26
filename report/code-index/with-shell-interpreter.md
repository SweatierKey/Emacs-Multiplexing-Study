# Indice del codice: with-shell-interpreter

Fonte: https://github.com/p3r7/with-shell-interpreter.git

Revisione: `8191d0b745dda30c7f6d225eb86598d8337c6b82`.


## with-shell-interpreter.el

- L26: `(require 'cl-lib)`
- L28: `(require 'files-x)`
- L29: `(require 'shell)`
- L92: `(defmacro with-shell-interpreter (&rest args)`
- L150: `(cl-defun with-shell-interpreter-eval (&key form path`
- L195: `(defun with-shell-interpreter--normalize-path (path)`
- L202: `(defun with-shell-interpreter--interpreter-name (interpreter)`
- L211: `(defun with-shell-interpreter--plist-get (plist prop)`
- L228: `(defun with-shell-interpreter--some (fn list)`
- L241: `(defun with-shell-interpreter--symbol-value (sym &optional allow-buffer-local)`
- L251: `(defun with-shell-interpreter--boundp-buffer-local (symbol)`
- L261: `(defun with-shell-interpreter--cnnx-local-vars (path)`
- L267: `(defun with-shell-interpreter--cnnx-local-vars-custom (path)`
- L278: `(defun with-shell-interpreter--cnnx-local-vars-native (path)`
- L299: `(defun with-shell-interpreter--resolve-shell-var (syms is-remote`
- L343: `(defun with-shell-interpreter--interpreter-value (is-remote`
- L360: `(defun with-shell-interpreter--generate-props (path interpreter allow-local-vars)`
- L389: `(provide 'with-shell-interpreter)`
