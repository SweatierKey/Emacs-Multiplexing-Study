# Indice del codice: emux-shcv

Fonte: https://github.com/shcv/emux.git

Revisione: `156829a9ee823b24a94108c95c34dbca8ca5a4d1`.


## emux.el

- L27: `(require 'vterm nil t)`
- L28: `(require 'tab-bar)`
- L29: `(require 'json)`
- L36: `(defcustom emux-terminal-backend 'vterm`
- L43: `(defcustom emux-buffer-prefix "emux"`
- L48: `(defcustom emux-workspace-name nil`
- L58: `(defcustom emux-use-workspaces 'auto`
- L87: `(defun emux-init-env (tmux-val state-dir log-file emux-dir)`
- L109: `(defun emux--has-workspaces-p ()`
- L116: `(defun emux--workspace-exists-p (name)`
- L121: `(defun emux--workspace-switch (name)`
- L126: `(defun emux--workspace-create (name)`
- L131: `(defun emux--workspace-kill (name)`
- L136: `(defun emux--workspace-current-name ()`
- L142: `(defun emux--ensure-workspace ()`
- L168: `(defun emux--destroy-workspace ()`
- L179: `(defun emux-create-session-workspace (name)`
- L196: `(defun emux-create-terminal (name &optional mode direction)`
- L209: `(defun emux-send-keys (buffer-name keys)`
- L222: `(defun emux--parse-tmux-key (key)`
- L241: `(defun emux--vterm-send-key (key)`
- L266: `(defun emux--eat-send-key (key)`
- L302: `(defun emux-kill-terminal (buffer-name)`
- L328: `(defun emux-set-pane-title (buffer-name title)`
- L333: `(defun emux-all-pane-info (output-file)`
- L363: `(defun emux-capture-pane-to-file (buffer-name output-file)`
- L373: `(defun emux-tab-info (output-file)`
- L388: `(defun emux--make-terminal-buffer (buf-name)`
- L413: `(defun emux--augmented-env ()`
- L425: `(defun emux--display-buffer (buf name mode direction)`
- L436: `(defun emux--split-window (buf direction)`
- L446: `(defun emux--create-tab (buf name)`
- L464: `(defun emux--close-pane (buf)`
- L483: `(defun emux--close-tab-for-buffer (buf frame)`
- L493: `(defun emux--find-tab-for-buffer (buf frame)`
- L512: `(defun emux-hide-pane (buffer-name)`
- L527: `(defun emux-show-pane (buffer-name &optional direction)`
- L536: `(defun emux-select-tab (name)`
- L550: `(defun emux-select-tab-for-buffer (buffer-name)`
- L558: `(defun emux-rename-tab-for-buffer (buffer-name new-name)`
- L566: `(defun emux-balance-windows ()`
- L576: `(defun emux-resize-pane (buffer-name delta horizontal)`
- L587: `(defun emux-resize-pane-absolute (buffer-name width height)`
- L603: `(defun emux-zoom-pane (buffer-name)`
- L623: `(defun emux-list-buffers ()`
- L638: `(defun emux-cleanup ()`
- L649: `(defun emux-kill-all ()`
- L665: `(provide 'emux)`
