# Indice del codice: multi-term

Fonte: https://github.com/manateelazycat/multi-term.git

Revisione: `017c77c550115936860e2ea71b88e585371475d5`.


## multi-term.el

- L279: `(require 'term)`
- L280: `(require 'cl-lib)`
- L281: `(require 'advice)`
- L292: `(defcustom multi-term-program nil`
- L298: `(defcustom multi-term-program-switches nil`
- L303: `(defcustom multi-term-try-create t`
- L311: `(defcustom multi-term-default-dir "~/"`
- L316: `(defcustom multi-term-buffer-name "terminal"`
- L321: `(defcustom multi-term-scroll-show-maximum-output nil`
- L329: `(defcustom multi-term-scroll-to-bottom-on-output nil`
- L341: `(defcustom multi-term-switch-after-close 'NEXT`
- L349: `(defcustom term-unbind-key-list`
- L355: `(defcustom term-bind-key-alist`
- L382: `(defcustom multi-term-dedicated-window-height 14`
- L387: `(defcustom multi-term-dedicated-max-window-height 30`
- L394: `(defcustom multi-term-dedicated-skip-other-window-p nil`
- L414: `(defcustom multi-term-dedicated-select-after-open-p nil`
- L422: `(defcustom multi-term-dedicated-close-back-to-open-buffer-p nil`
- L451: `(defun multi-term ()`
- L465: `(defun multi-term-next (&optional offset)`
- L472: `(defun multi-term-prev (&optional offset)`
- L479: `(defun multi-term-dedicated-open ()`
- L508: `(defun multi-term-dedicated-close ()`
- L529: `(defun multi-term-dedicated-remember-window-height ()`
- L538: `(defun multi-term-dedicated-toggle ()`
- L554: `(defun multi-term-dedicated-select ()`
- L561: `(defun term-send-esc ()`
- L566: `(defun term-send-return ()`
- L573: `(defun term-send-backward-kill-word ()`
- L578: `(defun term-send-forward-kill-word ()`
- L583: `(defun term-send-backward-word ()`
- L588: `(defun term-send-forward-word ()`
- L593: `(defun term-send-reverse-search-history ()`
- L598: `(defun term-send-delete-word ()`
- L603: `(defun term-send-quote ()`
- L609: `(defun term-send-M-x ()`
- L615: `(defun multi-term-internal ()`
- L631: `(defun multi-term-switch-buffer (term-buffer default-dir)`
- L642: `(defun multi-term-get-buffer (&optional special-shell dedicated-window)`
- L672: `(defun multi-term-handle-close ()`
- L680: `(defun multi-term-kill-buffer-hook ()`
- L700: `(defun multi-term-switch (direction offset)`
- L712: `(defun multi-term-switch-internal (direction offset)`
- L728: `(defun multi-term-keystroke-setup ()`
- L741: `(define-key term-raw-map unbind-key nil))`
- L752: `(define-key term-raw-map bind-key bind-command))))`
- L754: `(defun multi-term-dedicated-handle-other-window-advice (activate)`
- L764: `(defun multi-term-current-window-take-height (&optional window)`
- L771: `(defun multi-term-dedicated-get-window ()`
- L778: `(defun multi-term-dedicated-get-buffer-name ()`
- L782: `(defun multi-term-dedicated-exist-p ()`
- L787: `(defun multi-term-window-exist-p (window)`
- L792: `(defun multi-term-buffer-exist-p (buffer)`
- L797: `(defun multi-term-dedicated-window-p ()`
- L802: `(defun multi-term-window-dedicated-only-one-p ()`
- L872: `(provide 'multi-term)`
