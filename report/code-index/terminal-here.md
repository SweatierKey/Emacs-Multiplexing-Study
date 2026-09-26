# Indice del codice: terminal-here

Fonte: https://github.com/davidshepherd7/terminal-here.git

Revisione: `d90bc3e1c8c660e11dba002a1ce1d82940b260b1`.


## terminal-here.el

- L20: `(require 'cl-lib)`
- L21: `(require 'subr-x)`
- L28: `(defun terminal-here--pick-linux-default ()`
- L63: `(defcustom terminal-here-linux-terminal-command`
- L104: `(defcustom terminal-here-mac-terminal-command`
- L131: `(defcustom terminal-here-windows-terminal-command`
- L156: `(defcustom terminal-here-terminal-command`
- L186: `(defcustom terminal-here-command-flag`
- L199: `(defcustom terminal-here-project-root-function`
- L213: `(defcustom terminal-here-terminal-command-table`
- L264: `(defcustom terminal-here-command-flag-table`
- L300: `(defcustom terminal-here-verbose nil`
- L310: `(defun terminal-here--non-function-symbol-p (x)`
- L313: `(defun terminal-here--os-terminal-command ()`
- L324: `(defun terminal-here--maybe-lookup-in-terminal-command-table (term-spec)`
- L332: `(defun terminal-here--maybe-funcall (dir x)`
- L337: `(defun terminal-here--maybe-add-mac-os-open (terminal-command)`
- L344: `(defun terminal-here--get-terminal-command (dir)`
- L350: `(defun terminal-here--get-command-flag ()`
- L366: `(defun terminal-here--find-and-run-st (_)`
- L376: `(defun terminal-here--parse-ssh-dir (dir)`
- L383: `(defun terminal-here--ssh-command (ssh-data)`
- L398: `(defun terminal-here--tramp-path-to-directory (dir)`
- L417: `(defun terminal-here-launch-in-directory (dir &optional inner-command)`
- L435: `(defun terminal-here--run-command (command dir)`
- L454: `(defun terminal-here-launch (&optional inner-command)`
- L466: `(defun terminal-here-project-launch (&optional inner-command)`
- L484: `(provide 'terminal-here)`
