# Indice del codice: tmux-runner

Fonte: https://github.com/joaofnds/emacs-tmux-runner.git

Revisione: `1dfdefd2569848024c581a933e3ebc09b93b41e3`.


## emacs-tmux-runner-test.el

- L1: `(require 'buttercup)`
- L2: `(require 'emacs-tmux-runner)`

## emacs-tmux-runner.el

- L25: `(defun etr:list-sessions ()`
- L30: `(defun etr:select-session ()`
- L38: `(defun etr:set-session ()`
- L46: `(defun etr:list-windows ()`
- L52: `(defun etr:select-window ()`
- L62: `(defun etr:set-window ()`
- L70: `(defun etr:list-panes ()`
- L75: `(defun etr:other-panes ()`
- L84: `(defun etr:select-pane ()`
- L93: `(defun etr:set-pane ()`
- L98: `(defun etr:display-panes ()`
- L105: `(defun etr:set-user-command ()`
- L108: `(defun etr:forget-user-command ()`
- L113: `(defun etr:assert-user-command-presence ()`
- L116: `(defun etr:run-user-command ()`
- L124: `(defun etr:prompt (prompt &rest args)`
- L128: `(cl-defun etr:target-pane ()`
- L132: `(defun etr:reset-target-pane ()`
- L139: `(defun etr:ensure-target-pane ()`
- L144: `(defun etr:tmux (command)`
- L150: `(cl-defun etr:send-keys (input &optional (target (etr:target-pane)))`
- L154: `(cl-defun etr:send-enter (&optional (target (etr:target-pane)))`
- L157: `(cl-defun etr:send-command (input &optional (target (etr:target-pane)))`
- L162: `(defun etr:vslipt ()`
- L167: `(defun etr:hsplit ()`
- L172: `(cl-defun etr:clear-pane (&optional (pane (etr:target-pane)))`
- L178: `(cl-defun etr:focus-pane (&optional (pane (etr:target-pane)))`
- L184: `(cl-defun etr:zoom-pane (&optional (pane (etr:target-pane)))`
- L191: `(cl-defun etr:current-line ()`
- L196: `(cl-defun etr:current-selection ()`
- L203: `(cl-defun etr:sanitize-buffer-string (str)`
- L209: `(cl-defun etr:send-lines ()`
- L214: `(provide 'emacs-tmux-runner)`

## test-helper.el

- L3: `(defun stub-shell ()`
- L6: `(defun expect-shell-cmd (cmd)`
- L9: `(defun expect-cmd-to-target (session window pane)`
- L14: `(defun expect-cmd-to-default-target ()`
- L17: `(defun nth-sent-cmd (n)`
- L20: `(defun first-sent-cmd ()`
- L23: `(defun last-sent-cmd ()`
- L28: `(defun cmds-sent-count ()`
- L31: `(defmacro with-default-target (&rest body)`
