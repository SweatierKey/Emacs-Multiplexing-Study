# Indice del codice: toggle-term

Fonte: https://github.com/justinlime/toggle-term.el.git

Revisione: `ebfce6283e53fda7f69ccda73109a02b646623af`.


## toggle-term.el

- L65: `(defcustom toggle-term-size 40`
- L70: `(defcustom toggle-term-remember-resize t`
- L82: `(defcustom toggle-term-side 'bottom`
- L97: `(defcustom toggle-term-types '(term vterm ghostel eat shell eshell ielm)`
- L117: `(defcustom toggle-term-switch-upon-toggle t`
- L122: `(defcustom toggle-term-use-persp (when (and (boundp 'persp-mode) (eq persp-mode t)) t)`
- L127: `(defcustom toggle-term-spawn-hook nil`
- L132: `(defcustom toggle-term-close-hook nil`
- L154: `(defun toggle-term--get-last-used (&optional side)`
- L175: `(defun toggle-term--set-last-used (wrapped type)`
- L198: `(defun toggle-term--toggle-side (name)`
- L205: `(defun toggle-term--remember-window-size (window)`
- L229: `(defun toggle-term--saved-window-size (name)`
- L241: `(defun toggle-term--display-buffer (buffer &optional size side)`
- L264: `(defun toggle-term--cleanup-active-toggle ()`
- L272: `(defun toggle-term--spawn (wrapped type &optional side)`
- L318: `(defun toggle-term--strip-side-suffix (str)`
- L329: `(defun toggle-term--name-candidates ()`
- L352: `(defun toggle-term-find (&optional name type side)`
- L427: `(defun toggle-term--toggle (side)`
- L452: `(defun toggle-term-toggle ()`
- L471: `(defun toggle-term-toggle-left ()`
- L476: `(defun toggle-term-toggle-right ()`
- L481: `(defun toggle-term-toggle-top ()`
- L486: `(defun toggle-term-toggle-bottom ()`
- L492: `(defun toggle-term-term ()`
- L515: `(defun toggle-term-shell ()`
- L520: `(defun toggle-term-eshell ()`
- L525: `(defun toggle-term-ielm ()`
- L530: `(defun toggle-term--marginalia-annotate (cand)`
- L559: `(provide 'toggle-term)`
