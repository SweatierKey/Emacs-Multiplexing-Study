# Indice del codice: multi-run

Fonte: https://github.com/sagarjha/multi-run.git

Revisione: `13d4d923535b5e8482b13ff76185203075fb26a3`.


## multi-run-helpers.el

- L32: `(require 'multi-run-vars)`
- L38: `(defun multi-run-get-buffer-name (term-num)`
- L42: `(defun multi-run-get-working-directory ()`
- L49: `(defun multi-run-get-full-remote-path (file-path term-num root)`
- L56: `(defun multi-run-open-terminal (term-num)`
- L63: `(defun multi-run-display-buffers (master-buffer-name num-buffers window-batch symbol-prefix hint-fun)`
- L78: `(defun multi-run-on-single-terminal (command term-num)`
- L85: `(defun multi-run-on-terminals (command term-nums &optional delay)`
- L100: `(defun multi-run-create-terminals ()`
- L104: `(defun calculate-window-batch (num-terminals)`
- L108: `(defun multi-run-make-vertical-or-horizontal-pane (num-terminals offset sym-vec)`
- L115: `(defun multi-run-make-internal-recipe (num-terminals window-batch sym-vec)`
- L130: `(defun multi-run-make-symbols (hint)`
- L134: `(defun multi-run-make-dict (hint-fun sym-list)`
- L140: `(defun multi-run-copy-one-file-sudo (source-file destination-file-or-directory &optional non-root)`
- L155: `(defun multi-run-copy-one-file (source-file destination-file-or-directory)`
- L159: `(defun multi-run-flatten (list)`
- L162: `(defun multi-run-copy-generic (copy-fun &rest files)`
- L168: `(provide 'multi-run-helpers)`

## multi-run-vars.el

- L51: `(provide 'multi-run-vars)`

## multi-run.el

- L30: `(require 'window-layout)`
- L31: `(require 'multi-run-vars)`
- L32: `(require 'multi-run-helpers)`
- L38: `(defun multi-run-configure-terminals (&optional num-terminals window-batch)`
- L49: `(defun multi-run-with-delay (delay &rest cmd)`
- L57: `(defun multi-run-with-delay2 (delay &rest cmd)`
- L65: `(defun multi-run (&rest cmd)`
- L69: `(defun multi-run-loop (cmd &optional times delay)`
- L82: `(defun multi-run-ssh ()`
- L88: `(defun multi-run-find-remote-files-sudo (file-path &optional window-batch non-root)`
- L101: `(defun multi-run-find-remote-files (file-path &optional window-batch)`
- L105: `(defun multi-run-execute-on-single-buffer (buffer)`
- L111: `(defun multi-run-execute-command ()`
- L120: `(defun multi-run-edit-files (&optional window-batch)`
- L133: `(defun multi-run-edit-files-quit ()`
- L138: `(defun multi-run-execute-function-on-single-buffer (buffer fun)`
- L144: `(defun multi-run-execute-function-on-files (fun)`
- L148: `(defun multi-run-copy-sudo (file1 file-or-directory1 &rest files)`
- L152: `(defun multi-run-copy (file1 file-or-directory1 &rest files)`
- L156: `(defun multi-run-kill-terminals ()`
- L161: `(defun multi-run-kill-all-timers ()`
- L166: `(provide 'multi-run)`
