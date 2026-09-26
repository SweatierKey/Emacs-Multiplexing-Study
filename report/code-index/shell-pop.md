# Indice del codice: shell-pop

Fonte: https://github.com/kyagi/shell-pop-el.git

Revisione: `446b1691454e65be648dcb7e316639aa7dd73be2`.


## shell-pop.el

- L94: `(defcustom shell-pop-window-size 30`
- L103: `(defcustom shell-pop-full-span nil`
- L108: `(defcustom shell-pop-window-position "bottom"`
- L118: `(defcustom shell-pop-default-directory nil`
- L123: `(defun shell-pop--set-shell-type (symbol value)`
- L132: `(define-key term-raw-map (read-kbd-macro shell-pop-universal-key) 'shell-pop)))`
- L134: `(defcustom shell-pop-shell-type '("shell" "*shell*" (lambda () (shell)))`
- L178: `(defcustom shell-pop-term-shell (or (bound-and-true-p explicit-shell-file-name)`
- L185: `(defcustom shell-pop-autocd-to-working-dir t`
- L190: `(defcustom shell-pop-restore-window-configuration 'buffer-view`
- L209: `(defcustom shell-pop-cleanup-buffer-at-process-exit t`
- L214: `(defcustom shell-pop-prevent-scroll t`
- L222: `(defcustom shell-pop-per-window nil`
- L233: `(defcustom shell-pop-pop-under-shell nil`
- L243: `(defun shell-pop--set-universal-key (symbol value)`
- L246: `(when value (global-set-key (read-kbd-macro value) 'shell-pop))`
- L250: `(define-key term-raw-map (read-kbd-macro value) 'shell-pop)))`
- L253: `(defcustom shell-pop-universal-key nil`
- L261: `(defcustom shell-pop-in-hook nil`
- L266: `(defcustom shell-pop-in-after-hook nil`
- L271: `(defcustom shell-pop-out-hook nil`
- L276: `(defcustom shell-pop-process-exit-hook nil`
- L283: `(defun shell-pop--shell-buffer-name (index)`
- L290: `(defun shell-pop-check-internal-mode-buffer (index)`
- L305: `(defun shell-pop-get-internal-mode-buffer-window (index)`
- L310: `(defun shell-pop (arg)`
- L346: `(defun shell-pop--cd-to-cwd-eshell (cwd)`
- L353: `(defun shell-pop--cd-to-cwd-shell (cwd)`
- L363: `(defun shell-pop--cd-to-cwd-term (cwd)`
- L371: `(defun shell-pop--cd-to-cwd-vterm (cwd)`
- L376: `(defun shell-pop--cd-to-cwd-eat (cwd)`
- L383: `(defun shell-pop--cd-to-cwd-ghostel (cwd)`
- L388: `(defun shell-pop--cd-to-cwd (cwd)`
- L409: `(defun shell-pop--per-window-p ()`
- L415: `(defun shell-pop--pop-under-shell-p ()`
- L420: `(defun shell-pop--popup-window-for-source-window (source-window &optional index)`
- L433: `(defun shell-pop--target-index (arg)`
- L441: `(defun shell-pop--toggle-target-from-shell (index)`
- L462: `(defun shell-pop--calculate-window-size ()`
- L470: `(defun shell-pop--eshell-exit-hook-delete-window ()`
- L499: `(defun shell-pop--set-exit-action ()`
- L549: `(defun shell-pop--switch-to-shell-buffer (index)`
- L560: `(defun shell-pop--translate-position (pos)`
- L568: `(defun shell-pop-get-unused-internal-mode-buffer-window ()`
- L580: `(defun shell-pop-up (index)`
- L657: `(defun shell-pop-out ()`
- L740: `(defun shell-pop-split-window ()`
- L753: `(provide 'shell-pop)`
