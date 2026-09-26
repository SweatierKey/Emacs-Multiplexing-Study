# Indice del codice: project-shells

Fonte: https://github.com/hying-caritas/project-shells.git

Revisione: `15f70d99b6d5f078f490ceb64b6f13c000b37e24`.


## project-shells.el

- L52: `(require 'cl-lib)`
- L53: `(require 'shell)`
- L54: `(require 'term)`
- L55: `(require 'eshell)`
- L56: `(require 'seq)`
- L69: `(defcustom project-shells-default-shell-name "sh"`
- L74: `(defcustom project-shells-empty-project "-"`
- L81: `(defcustom project-shells-setup '((,project-shells-empty-project .`
- L103: `(defcustom project-shells-default-init-func 'project-shells-init-sh`
- L106: `(defcustom project-shells-keys '("1" "2" "3" "4" "5" "6" "7" "8" "9" "0" "-" "=")`
- L114: `(defcustom project-shells-vterm-keys nil`
- L122: `(defcustom project-shells-term-keys '("-")`
- L131: `(defcustom project-shells-eshell-keys '("=")`
- L140: `(defcustom project-shells-session-root "~/.sessions"`
- L145: `(defcustom project-shells-project-name-func 'projectile-project-name`
- L150: `(defcustom project-shells-project-root-func 'projectile-project-root`
- L155: `(defcustom project-shells-histfile-env "HISTFILE"`
- L160: `(defcustom project-shells-histfile-name ".shell_history"`
- L165: `(defcustom project-shells-init-file-name ".shellrc"`
- L170: `(defcustom project-shells-term-args nil`
- L175: `(defcustom project-shells-keymap-prefix "C-c s"`
- L230: `(cl-defun project-shells-send-shell-command (cmdline)`
- L236: `(cl-defun project-shells-init-sh (session-dir type)`
- L245: `(cl-defun project-shells--project-name ()`
- L251: `(cl-defun project-shells--project-root (proj-name)`
- L259: `(cl-defun project-shells--histfile-name (session-dir)`
- L263: `(cl-defun project-shells--command-string (args)`
- L271: `(cl-defun project-shells--term-command-string ()`
- L278: `(cl-defun project-shells-activate-for-key (key &optional proj proj-root)`
- L335: `(cl-defun project-shells-activate (p)`
- L345: `(cl-defun project-shells-setup (map &optional setup)`
- L353: `do (define-key map (kbd key) 'project-shells-activate)))`
- L357: `(defvar project-shells-map`
- L360: `(define-key map (kbd "s") 'project-shells-switch-to-last)`
- L365: `(defvar project-shells-mode-map`
- L369: `(define-key map (kbd project-shells-keymap-prefix)`
- L375: `(define-minor-mode project-shells-mode`
- L384: `(provide 'project-shells)`
