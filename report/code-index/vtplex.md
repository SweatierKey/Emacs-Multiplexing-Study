# Indice del codice: vtplex

Fonte: https://github.com/mitch-kyle/vtplex.git

Revisione: `f853c0f6f32499b24300a0519d348356645c1a33`.


## vtplex-spaceline.el

- L30: `(require 'vtplex)`
- L31: `(require 'spaceline)`
- L41: `(defcustom vtplex-spaceline-max-title-length 30`
- L47: `(defcustom vtplex-spaceline-title-overflow-suffix "..."`
- L76: `(defun vtplex-spaceline--indicator-text (index buffer)`
- L93: `(defun vtplex-spaceline-buffer-indicator (n`
- L127: `(define-key map`
- L146: `(defun vtplex-spaceline--set (&rest _)`
- L157: `(defun vtplex-spaceline-compile (&rest additional-segments)`
- L194: `(defun vtplex-spaceline-enable (&rest additional-segments)`
- L204: `(defun vtplex-spaceline-disable ()`
- L212: `(provide 'vtplex-spaceline)`

## vtplex.el

- L43: `(require 'vterm)`
- L44: `(require 'seq)`
- L68: `(defun vtplex--exit ()`
- L76: `(defun vtplex-switch (&optional title)`
- L92: `(defun vtplex-switch-index (index)`
- L98: `(defun vtplex--current-index ()`
- L105: `(defun vtplex-next ()`
- L115: `(defun vtplex-prev ()`
- L125: `(defun vtplex-bury ()`
- L131: `(defun vtplex-hide ()`
- L139: `(defun vtplex-last ()`
- L150: `(defun vtplex-create ()`
- L157: `(defun vtplex-execute (command)`
- L164: `(defun vtplex ()`
- L176: `(defvar vtplex-mode-map`
- L178: `(define-key map (kbd "C-a C-a") 'vterm-send-C-a)`
- L179: `(define-key map (kbd "C-a [")   'vterm-copy-mode)`
- L180: `(define-key map (kbd "C-a c")   'vtplex-create)`
- L181: `(define-key map (kbd "C-a r")   'vtplex-execute)`
- L182: `(define-key map (kbd "C-a b")   'vtplex-switch)`
- L183: `(define-key map (kbd "C-a n")   'vtplex-next)`
- L184: `(define-key map (kbd "C-a p")   'vtplex-prev)`
- L185: `(define-key map (kbd "C-a d")   'vtplex-bury)`
- L188: `(define-key map (kbd (format "C-a %s" i))`
- L195: `(define-minor-mode vtplex-mode`
- L213: `(provide 'vtplex)`
