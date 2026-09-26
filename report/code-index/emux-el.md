# Indice del codice: emux-el

Fonte: https://github.com/luozengbin/emux-el.git

Revisione: `acc8db2b25d394364165ddeee13019a28eff4fba`.


## emux.el

- L28: `(require 'cl)`
- L29: `(require 'term)`
- L36: `(defun emux:window-total-width (&optional window)`
- L51: `(defcustom emux:shell-program nil`
- L58: `(defcustom emux:terminal-name "emux"`
- L78: `(defun emux:shell-program ()`
- L97: `(defun emux:terminal-live-p (term)`
- L103: `(defun emux:terminal-kill (term)`
- L110: `(defun emux:current-live-terminal ()`
- L117: `(defun emux:current-live-terminal! ()`
- L121: `(defun* emux:next-live-terminal (term &key cycle)`
- L127: `(defun* emux:previous-live-terminal (term &key cycle)`
- L133: `(defun emux:first-terminal ()`
- L139: `(defun emux:last-terminal ()`
- L145: `(defun emux:list-terminals ()`
- L149: `(defun emux:live-terminals ()`
- L154: `(defun emux:dead-terminals ()`
- L159: `(defun emux:add-terminal (term)`
- L167: `(defun emux:clean-dead-terminals ()`
- L183: `(defun emux:make-terminal-buffer (name program)`
- L190: `(defun emux:new-terminal-1 (name program)`
- L195: `(defun emux:new-terminal ()`
- L199: `(defun emux:make-terminal-header (term &optional window)`
- L224: `(defun emux:update-terminal-header (term &optional window)`
- L228: `(defun emux:update-terminal (term &optional window)`
- L231: `(defun emux:switch-to-terminal (term)`
- L237: `(defun emux:switch-to-terminal-other-window (term)`
- L246: `(defvar emux:term-raw-escape-map`
- L249: `(define-key map (kbd "C-n") 'emux:term-next)`
- L250: `(define-key map (kbd "SPC") 'emux:term-next)`
- L251: `(define-key map (kbd "C-p") 'emux:term-previous)`
- L252: `(define-key map (kbd "C-t") 'emux:term-new)`
- L253: `(define-key map (kbd "A")   'emux:term-rename)`
- L254: `(define-key map (kbd "k")   'emux:term-kill)`
- L255: `(define-key map (kbd "d")   'emux:term-cd)`
- L256: `(define-key map (kbd "~")   'emux:term-sync)`
- L259: `(defvar emux:term-raw-map`
- L262: `(define-key map (kbd "C-c") emux:term-raw-escape-map)`
- L265: `(defun emux:term-mode ()`
- L273: `(defun emux:term-kill-input ()`
- L280: `(defun emux:term-send-input ()`
- L287: `(defun emux:term-command (command &optional record-flag)`
- L296: `(defun emux:term-noselect ()`
- L302: `(defun emux:term ()`
- L308: `(defun emux:term-other-window ()`
- L313: `(defun emux:term-new ()`
- L318: `(defun emux:term-previous ()`
- L323: `(defun emux:term-next ()`
- L328: `(defun emux:term-rename ()`
- L336: `(defun emux:term-kill ()`
- L346: `(defun emux:term-cd (directory)`
- L351: `(defun emux:term-sync (&optional buffer)`
- L358: `(provide 'emux)`
