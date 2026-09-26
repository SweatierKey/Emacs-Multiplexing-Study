# Indice del codice: multi-buf

Fonte: https://github.com/djr7C4/multi-buf.git

Revisione: `dcd28e9d18b4757431eb99a22b2193efb8f87841`.


## multi-buf.el

- L34: `(require 'cl-lib)`
- L35: `(require 'eieio)`
- L36: `(require 'project)`
- L39: `(defun multi-buf-project-root ()`
- L48: `(defmacro multi-buf-with-displayed-buffer (&rest body)`
- L85: `(defun multi-buf-cleanup-wrapper ()`
- L89: `(defun multi-buf-register (backend buf)`
- L188: `(defun multi-buf-all ()`
- L224: `(defun multi-buf-create (backend)`
- L231: `(cl-defun multi-buf-next (backend &key (offset 1) (use-category (multi-buf-use-category-default backend 'cycle)))`
- L265: `(cl-defun multi-buf-previous (backend &key (offset 1) (use-category (multi-buf-use-category-default backend 'cycle)))`
- L277: `(cl-defun multi-buf-switch (backend &key (use-category (multi-buf-use-category-default backend 'switch)) all)`
- L304: `(cl-defun multi-buf-switch-group (backend)`
- L392: `(cl-defun multi-buf-dwim-docstring`
- L452: `(cl-defun multi-buf-dwim (backend arg &key region-force-new)`
- L667: `(defun multi-buf-indirect-register (buf)`
- L685: `(defun multi-buf-new-indirect ()`
- L690: `(defun multi-buf-indirect-dwim (&optional arg)`
- L696: `(provide 'multi-buf)`
