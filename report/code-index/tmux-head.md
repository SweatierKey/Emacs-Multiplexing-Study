# Indice del codice: tmux-head

Fonte: https://github.com/jeffyql/tmux-head.git

Revisione: `12c6fa6fa1fef1c6af738086dceea53344483ef6`.


## tmux-commands.el

- L1: `(require 'general)`
- L2: `(require 'hydra)`

## tmux-head-ipython.el

- L22: `(defun tmux-ipython-send-buffer (&optional arg)`
- L29: `(defun tmux-python-console-p ()`
- L35: `(defun tmux-ipython-send-region (&optional arg)`
- L59: `(defun tmux-ipython-send-defun ()`
- L80: `(defun tmux-ipython-send-from-beginning ()`
- L88: `(defun tmux-ipython-send-to-end ()`
- L100: `(defun tmux-ipython-print (&optional arg)`
- L104: `(defun tmux-ipython-help (&optional arg)`
- L108: `(defun tmux-ipython-send-special (type &optional arg)`
- L125: `(defun tmux-python-run-this-file ()`
- L133: `(defun tmux-ipython-start ()`
- L137: `(defun tmux-ipython-start-existing ()`
- L148: `(provide 'tmux-head-ipython)`

## tmux-head.el

- L22: `(require 'comint)`
- L29: `(defun tmux-run-command (cmd &rest args)`
- L36: `(defun tmux-pane-0-run-command (cmd &rest args)`
- L39: `(defun tmux-send-key (&rest args)`
- L42: `(defun tmux-run-key (&rest args)`
- L45: `(defun tmux-copy (str)`
- L48: `(defun tmux-paste ()`
- L52: `(defun tmux-shell-send-string (str &optional arg)`
- L60: `(defun tmux-send-region (&optional arg)`
- L98: `(defun tmux-dired-run-file ()`
- L104: `(defun tmux-send-selection (cmd-str)`
- L109: `(defun tmux-minibuffer-run-shell-cmd ()`
- L113: `(define-key map (kbd "TAB") 'my-complete-file-name)`
- L114: `(define-key map (kbd "M-y") 'insert-current-file-name-at-point)`
- L118: `(defun tmux-edit-and-send (cmd-string)`
- L122: `(defun tmux-edit-and-send-action ()`
- L128: `(defun tmux-edit-and-send-prompt-action ()`
- L138: `(defvar ivy-minibuffer-tmux-shell-command-map`
- L140: `(define-key map (kbd "TAB") #'my-complete-file-name)`
- L141: `(define-key map (kbd "C-c C-c") #'tmux-ctrl-c)`
- L142: `(define-key map (kbd "C-d") #'tmux-ctrl-d)`
- L143: `(define-key map (kbd "M-RET") 'tmux-edit-and-send-prompt-action)`
- L144: `(define-key map (kbd "M-h") 'tmux-swap-pane)`
- L145: `(define-key map (kbd "M-i") #'ivy-immediate-done)   ;; CMD-m : run prompt text`
- L146: `(define-key map (kbd "M-l") 'ivy-insert-current)    ;; CMD-h : insert selected`
- L147: `(define-key map (kbd "M-m") 'tmux-edit-and-send-action)`
- L148: `(define-key map (kbd "M-u") 'tmux-sync-location-with-emacs)`
- L152: `(defun tmux-ivy-run-shell (&optional arg)`
- L168: `(defun tmux-insert-state ()`
- L206: `(defun tmux-set-emacs-frame-name (frame-name)`
- L213: `(defun tmux-display-pane-numbers ()`
- L222: `(defun my/tmux-select-number (num-list prompt)`
- L236: `(defun tmux-get-list-entry (num &rest cmd)`
- L245: `(defun tmux-get-window-name (window-num)`
- L251: `(defun tmux-get-pane-or-window-number-list (&optional panes)`
- L266: `(defun tmux-display-message (message &optional pane-id)`
- L272: `(defun tmux-pane-height (pane-id)`
- L275: `(defun tmux-window-height ()`
- L278: `(defun tmux-window-id ()`
- L281: `(defun tmux-zoomed ()`
- L285: `(defun tmux-zoom-pane-0 ()`
- L290: `(defun tmux-unzoom-pane-0 ()`
- L295: `(defun tmux-toggle-zoom ()`
- L299: `(defun tmux-window-exist (window-num)`
- L304: `(defun tmux-capture-pane (&optional arg)`
- L327: `(defun tmux-ctrl-c ()`
- L332: `(defun tmux-ctrl-d ()`
- L337: `(defun tmux-ctrl-m ()`
- L342: `(defun tmux-q ()`
- L347: `(defun tmux-ctrl-z ()`
- L352: `(defun tmux-space ()`
- L356: `(defun tmux-n ()`
- L360: `(defun tmux-y ()`
- L364: `(defun tmux-clear-pane ()`
- L370: `(defun tmux-login-type ()`
- L373: `(defun tmux-cd-default-directory ()`
- L399: `(defun tmux-down ()`
- L403: `(defun tmux-up ()`
- L407: `(defun tmux-command-history-prev ()`
- L411: `(defun tmux-command-history-next ()`
- L416: `(defun  tmux-ls ()`
- L420: `(defun tmux-pwd ()`
- L425: `(defun tmux-home-dir ()`
- L430: `(defun tmux-last-dir ()`
- L435: `(defun tmux-up-dir ()`
- L439: `(defun tmux-begin-cmd-history ()`
- L443: `(defun tmux-run-a-history-cmd ()`
- L451: `(defun tmux-begin-copy-mode ()`
- L457: `(defun tmux-quit-copy-mode ()`
- L464: `(defun tmux-page-up ()`
- L468: `(defun tmux-page-down ()`
- L472: `(defun tmux-halfpage-up ()`
- L476: `(defun tmux-halfpage-down ()`
- L480: `(defun tmux-copy-mode-down ()`
- L484: `(defun tmux-copy-mode-up ()`
- L488: `(defun tmux-kill-pane ()`
- L494: `(defun tmux-resize-pane (directory)`
- L497: `(defun tmux-resize-pane-up ()`
- L501: `(defun tmux-resize-pane-down ()`
- L505: `(defun tmux-resize-pane-left ()`
- L509: `(defun tmux-resize-pane-right ()`
- L513: `(defun tmux-new-window ()`
- L518: `(defun tmux-kill-window ()`
- L523: `(defun tmux-split-window (direction)`
- L528: `(defun tmux-split-window-horizontal ()`
- L533: `(defun tmux-split-window-vertical ()`
- L538: `(defun tmux-last-window (&optional keep-display)`
- L542: `(defun tmux-next-window (&optional keep-display)`
- L548: `(defun tmux-select-window (window-id &optional keep-display)`
- L553: `(defun tmux-select-window-0 (&optional arg)`
- L558: `(defun tmux-select-window-1 (&optional arg)`
- L563: `(defun tmux-select-window-2 (&optional arg)`
- L568: `(defun tmux-select-window-3 (&optional arg)`
- L573: `(defun tmux-select-window-4 (&optional arg)`
- L578: `(defun tmux-select-window-5 (&optional arg)`
- L583: `(defun tmux-select-window-6 (&optional arg)`
- L588: `(defun tmux-select-window-7 (&optional arg)`
- L593: `(defun tmux-select-window-8 (&optional arg)`
- L598: `(defun tmux-select-window-9 (&optional arg)`
- L603: `(defun tmux-rename-window ()`
- L609: `(defun tmux-select-pane-num ()`
- L614: `(defun tmux-select-pane ()`
- L619: `(defun tmux-select-pane-0 ()`
- L623: `(defun tmux-swap-pane ()`
- L637: `(defun tmux-tail-this-file ()`
- L646: `(provide 'tmux-head)`
