# Indice del codice: abysl-term

Fonte: https://github.com/abysl/abysl-term.git

Revisione: `7a5de7fb1bd50a56c0ccf6c808fb817a84c49247`.


## abysl-term.el

- L81: `(defcustom abysl-term-terminal "wezterm"`
- L86: `(defcustom abysl-term-terminal-args '("--always-new-process")`
- L91: `(defcustom abysl-term-shell "bash"`
- L96: `(defcustom abysl-term-hide 'onSuccess`
- L103: `(defcustom abysl-term-args-alist`
- L125: `(defcustom abysl-term-user-exit-hooks nil`
- L135: `(defun abysl-term-open-shell (&optional terminal terminal-args shell)`
- L151: `(defun abysl-term-run (command &optional current-exit-hook terminal terminal-args shell)`
- L184: `(defun abysl-term-run-selected ()`
- L193: `(defun abysl-term-run-previous ()`
- L202: `(defun abysl-term--get-terminal-flags (term action)`
- L212: `(defun abysl-term--use-argument-separator (term)`
- L223: `(defun abysl-term--format-command (term &optional term-args shell shell-args command)`
- L249: `(defun abysl-term--run-terminal (full-command tmp-files exit-hooks)`
- L262: `(defun abysl-term--process-sentinel (proc event tmp-files exit-hooks)`
- L272: `(defun abysl-term--default-exit-hook (tmp-files exit-hooks)`
- L295: `(defun abysl-term--show-buffer (exit-codes output)`
- L311: `(defun abysl-term--handle-output (exit-codes output)`
- L327: `(defun abysl-term--merge-exit-hooks (user-hooks current-exit-hook)`
- L333: `(defun abysl-term--generate-command (shell command-str)`
- L354: `(defun abysl-term--find-shell-path (shell)`
- L365: `(defun abysl-term--get-command-str (command)`
- L371: `(defun abysl-term--message-tmp-files (tmp-files prefix)`
- L381: `(defun abysl-term--strip-carriage-returns (string)`
- L385: `(defun apply-all (str replacements)`
- L395: `(defun abysl-term--convert-to-unix-path (path)`
- L410: `(defun abysl-term--get-project-root-or-default ()`
- L425: `(provide 'abysl-term)`
