# Indice del codice: multi-term-roman

Fonte: https://github.com/roman/multi-term.git

Revisione: `06f6b49ef53a5f2ea779b1608eb5a7b38660e6bb`.


## multi-term.el

- L236: `(require 'term)`
- L237: `(require 'cl)`
- L238: `(require 'advice)`
- L249: `(defcustom multi-term-program nil`
- L255: `(defcustom multi-term-program-switches nil`
- L263: `(defcustom multi-term-try-create t`
- L271: `(defcustom multi-term-default-dir "~/"`
- L276: `(defcustom multi-term-buffer-name "terminal"`
- L281: `(defcustom multi-term-scroll-show-maximum-output nil`
- L289: `(defcustom multi-term-scroll-to-bottom-on-output nil`
- L301: `(defcustom multi-term-switch-after-close 'NEXT`
- L309: `(defcustom term-unbind-key-list`
- L315: `(defcustom term-bind-key-alist`
- L338: `(defcustom multi-term-dedicated-window-height 14`
- L343: `(defcustom multi-term-dedicated-max-window-height 30`
- L350: `(defcustom multi-term-dedicated-skip-other-window-p nil`
- L365: `(defcustom multi-term-dedicated-select-after-open-p nil`
- L387: `(defun multi-term ()`
- L404: `(defun multi-term-persistent (&optional session-name screen-shell)`
- L422: `(defun multi-term-next (&optional offset)`
- L428: `(defun multi-term-prev (&optional offset)`
- L434: `(defun multi-term-dedicated-open ()`
- L463: `(defun multi-term-dedicated-close ()`
- L484: `(defun multi-term-dedicated-remember-window-height ()`
- L492: `(defun multi-term-dedicated-toggle ()`
- L499: `(defun multi-term-dedicated-select ()`
- L506: `(defun term-send-backward-kill-word ()`
- L511: `(defun term-send-forward-kill-word ()`
- L516: `(defun term-send-backward-word ()`
- L521: `(defun term-send-forward-word ()`
- L526: `(defun term-send-reverse-search-history ()`
- L533: `(defun multi-term-internal ()`
- L549: `(defun multi-term-get-buffer (&optional special-shell dedicated-window)`
- L582: `(defun multi-term-handle-close ()`
- L590: `(defun multi-term-kill-buffer-hook ()`
- L606: `(defun multi-term-list ()`
- L623: `(defun multi-term-switch (direction offset)`
- L635: `(defun multi-term-switch-internal (direction offset)`
- L655: `(defun multi-term-keystroke-setup ()`
- L668: `(define-key term-raw-map unbind-key nil))`
- L679: `(define-key term-raw-map bind-key bind-command))))`
- L681: `(defun multi-term-dedicated-handle-other-window-advice (activate)`
- L691: `(defun multi-term-current-window-take-height (&optional window)`
- L698: `(defun multi-term-dedicated-get-window ()`
- L705: `(defun multi-term-dedicated-get-buffer-name ()`
- L709: `(defun multi-term-dedicated-exist-p ()`
- L714: `(defun multi-term-window-exist-p (window)`
- L719: `(defun multi-term-buffer-exist-p (buffer)`
- L724: `(defun multi-term-dedicated-window-p ()`
- L729: `(defun multi-term-window-dedicated-only-one-p ()`
- L800: `(provide 'multi-term)`
