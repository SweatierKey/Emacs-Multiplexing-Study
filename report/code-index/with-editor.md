# Indice del codice: with-editor

Fonte: https://github.com/magit/with-editor.git

Revisione: `7bec41144ea197961c76c769cfc0acaf689ebac0`.


## .dir-locals.el


## lisp/with-editor.el

- L48: `;;   (keymap-global-set "<remap> <async-shell-command>"`
- L50: `;;   (keymap-global-set "<remap> <shell-command>"`
- L85: `(require 'cl-lib)`
- L86: `(require 'compat)`
- L87: `(require 'cond-let)`
- L88: `(require 'llama)`
- L89: `(require 'server)`
- L90: `(require 'shell)`
- L109: `(defun with-editor-locate-emacsclient ()`
- L125: `(defun with-editor-locate-emacsclient-1 (path depth)`
- L151: `(defun with-editor-emacsclient-version (exec)`
- L156: `(defun with-editor-emacsclient-path ()`
- L179: `(defcustom with-editor-emacsclient-executable (with-editor-locate-emacsclient)`
- L185: `(defcustom with-editor-sleeping-editor "\`
- L235: `(defcustom with-editor-finish-query-functions nil`
- L249: `(defcustom with-editor-cancel-query-functions nil`
- L263: `(defcustom with-editor-mode-lighter " WE"`
- L285: `(defcustom with-editor-shell-command-use-emacsclient t`
- L340: `(defun with-editor-finish (force)`
- L358: `(defun with-editor-cancel (force)`
- L378: `(defun with-editor-return (cancel)`
- L419: `(defvar-keymap with-editor-mode-map`
- L430: `(define-minor-mode with-editor-mode`
- L448: `(defun with-editor-kill-buffer-noop ()`
- L470: `(defun with-editor-usage-message ()`
- L484: `(defmacro with-editor (&rest body)`
- L499: `(defmacro with-editor* (envvar &rest body)`
- L512: `(defun with-editor--setup ()`
- L557: `(defun with-editor-server-window ()`
- L602: `(cl-defun make-process@with-editor-process-filter`
- L642: `(defun with-editor-set-process-filter (process filter)`
- L669: `(defun with-editor-sleeping-editor-filter (process string)`
- L725: `(defun with-editor-process-filter`
- L748: `(cl-defun with-editor-export-editor`
- L831: `(defun with-editor-export-git-editor (&optional process interactive)`
- L841: `(defun with-editor-export-hg-editor (&optional process interactive)`
- L850: `(defun with-editor-output-filter (string)`
- L854: `(defun with-editor-emulate-terminal (process string)`
- L863: `(cl-defun with-editor-read-envvar`
- L873: `(define-minor-mode shell-command-with-editor-mode`
- L892: `(defun with-editor-async-shell-command`
- L915: `(defun with-editor-shell-command`
- L926: `(defun with-editor-shell-command-read-args (prompt &optional async)`
- L976: `(defun with-editor-debug ()`
- L1039: `(provide 'with-editor)`
