# Indice del codice: coterm

Fonte: https://github.com/emacsmirror/coterm.git

Revisione: `ce3206fbd7156685e2d2f3fbc39b3eea3334754b`.


## coterm.el

- L68: `;;     (define-key comint-mode-map (kbd "C-;") #'coterm-char-mode-cycle))`
- L131: `(require 'term)`
- L132: `(require 'compat)`
- L139: `(defcustom coterm-term-name term-term-name`
- L183: `(define-minor-mode coterm-mode`
- L227: `(defvar coterm-char-mode-map`
- L230: `(define-key map [remap term-char-mode] #'coterm-char-mode-cycle)`
- L231: `(define-key map [remap term-line-mode] #'coterm-char-mode-cycle)`
- L234: `(define-minor-mode coterm-char-mode`
- L245: `(define-minor-mode coterm-scroll-snap-mode`
- L268: `(defun coterm--scroll-snap ()`
- L303: `(defun coterm-char-mode-cycle ()`
- L326: `(define-minor-mode coterm-auto-char-mode`
- L347: `(define-minor-mode coterm-auto-char-lighter-mode`
- L365: `(defun coterm--auto-char ()`
- L381: `(defun coterm--auto-char-alternative-sub-buffer ()`
- L388: `(defun coterm--auto-char-less-prompt ()`
- L429: `(defun coterm--auto-char-less-prompt-1 ()`
- L447: `(defun coterm--auto-char-mpv-prompt ()`
- L476: `(defun coterm--auto-char-mpv-prompt-1 ()`
- L495: `(defun coterm--auto-char-not-eob ()`
- L520: `(defun coterm--auto-char-leave-both ()`
- L525: `(defun coterm--narrow-to-process-output (pmark)`
- L643: `(defun coterm--t-row ()`
- L656: `(defun coterm--t-col ()`
- L673: `(defun coterm--init ()`
- L697: `(defun coterm--t-reset-size (height width)`
- L721: `(defun coterm--t-goto (row col)`
- L732: `(defun coterm--t-apply-proc-filt (proc-filt process str)`
- L752: `(defun coterm--t-switch-to-alternate-sub-buffer (proc-filt process set)`
- L799: `(defun coterm--t-down-line (proc-filt process)`
- L845: `(defun coterm--t-up-line (proc-filt process)`
- L894: `(defun coterm--t-clear-screen ()`
- L911: `(defun coterm--t-insert (proc-filt process str newlines)`
- L959: `(defun coterm--t-emulate-terminal (proc-filt process string)`
- L1347: `(provide 'coterm)`
