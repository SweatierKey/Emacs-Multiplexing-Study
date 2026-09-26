# Indice del codice: ob-tmux

Fonte: https://github.com/ahendriksen/ob-tmux.git

Revisione: `cb4f151554a653f8f6b22ab8edbe3420d7f5e377`.


## ob-tmux.el

- L42: `(require 'ob)`
- L43: `(require 'seq)`
- L44: `(require 's)`
- L47: `(defcustom org-babel-tmux-location "tmux"`
- L53: `(defcustom org-babel-tmux-session-prefix "org-babel-session-"`
- L58: `(defcustom org-babel-tmux-default-window-name "ob1"`
- L63: `(defcustom org-babel-tmux-terminal "gnome-terminal"`
- L68: `(defcustom org-babel-tmux-terminal-opts '("--")`
- L86: `(defun org-babel-execute:tmux (body params)`
- L131: `(defun ob-tmux--tmux-session (org-session)`
- L136: `(defun ob-tmux--tmux-window (org-session)`
- L141: `(defun ob-tmux--from-org-session (org-session &optional socket)`
- L150: `(defun ob-tmux--window-default (ob-session)`
- L159: `(defun ob-tmux--target (ob-session)`
- L175: `(defun ob-tmux--execute (ob-session &rest args)`
- L188: `(defun ob-tmux--execute-string (ob-session &rest args)`
- L201: `(defun ob-tmux--start-terminal-window (ob-session terminal)`
- L220: `(defun ob-tmux--create-session (ob-session)`
- L232: `(defun ob-tmux--create-window (ob-session)`
- L243: `(defun ob-tmux--set-window-option (ob-session option value)`
- L253: `(defun ob-tmux--disable-renaming (ob-session)`
- L265: `(defun ob-tmux--format-keys (string)`
- L270: `(defun ob-tmux--send-keys (ob-session line)`
- L282: `(defun ob-tmux--send-body (ob-session body)`
- L296: `(defun ob-tmux--session-alive-p (ob-session)`
- L306: `(defun ob-tmux--window-alive-p (ob-session)`
- L325: `(defun ob-tmux--deprecation-warning (org-header-terminal)`
- L362: `(defun ob-tmux--open-file (path)`
- L370: `(defun ob-tmux--test ()`
- L390: `(provide 'ob-tmux)`
