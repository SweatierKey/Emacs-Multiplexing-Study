# Indice del codice: shackle

Fonte: https://github.com/wasamasa/shackle.git

Revisione: `32a397770be30a518f5123b81a6d667d02308bfb`.


## shackle.el

- L38: `(require 'cl-lib)`
- L45: `(defcustom shackle-select-reused-windows nil`
- L53: `(defcustom shackle-inhibit-window-quit-on-same-windows nil`
- L62: `(defcustom shackle-default-alignment 'below`
- L85: `(defcustom shackle-default-size 0.5`
- L96: `(defcustom shackle-rules nil`
- L207: `(defcustom shackle-default-rule nil`
- L231: `(defun shackle--match (buffer-or-name condition plist)`
- L252: `(defun shackle-match (buffer-or-name)`
- L263: `(defun shackle-display-buffer-condition (buffer action)`
- L269: `(defun shackle-display-buffer-action (buffer alist)`
- L275: `(defun shackle--frame-splittable-p (frame)`
- L281: `(defun shackle--splittable-frame ()`
- L290: `(defun shackle--split-some-window (frame alist)`
- L300: `(defun shackle--inhibit-window-quit (window)`
- L304: `(defun shackle--window-display-buffer (buffer window type alist)`
- L317: `(defun shackle--display-buffer-reuse (buffer alist)`
- L328: `(defun shackle--display-buffer-same (buffer alist)`
- L337: `(defun shackle--display-buffer-frame (buffer alist plist)`
- L362: `(defun shackle--display-buffer-popup-window (buffer alist plist)`
- L380: `(defun shackle--display-buffer-aligned-window (buffer alist plist)`
- L422: `(defun shackle--display-buffer (buffer alist plist)`
- L446: `(defun shackle-display-buffer (buffer alist plist)`
- L465: `(define-minor-mode shackle-mode`
- L484: `(require 'trace)`
- L486: `(defcustom shackle-trace-buffer "*shackle trace*"`
- L491: `(defcustom shackle-traced-functions`
- L500: `(defun shackle-trace-functions ()`
- L506: `(defun shackle-untrace-functions ()`
- L512: `(provide 'shackle)`
