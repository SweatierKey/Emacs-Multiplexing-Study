# Indice del codice: turnip

Fonte: https://github.com/kljohann/turnip.el.git

Revisione: `2fd32562fc6fc1cda6d91aa939cfb29f9b16e9de`.


## turnip.el

- L30: `(require 'dash)`
- L31: `(require 's)`
- L39: `(defcustom turnip-send-region-before-keys nil`
- L46: `(defcustom turnip-send-region-prepare-hook nil`
- L55: `(defcustom turnip-output-buffer-name "*turnip-output*"`
- L74: `(defun turnip:session (&optional session silent)`
- L84: `(defun turnip:pane-id-p (target)`
- L88: `(defun turnip:format-pane-id (pane &optional fmt)`
- L94: `(defun turnip:panes-displaying-emacs ()`
- L101: `(defun turnip:qualify (target &optional session)`
- L114: `(defun turnip:pane-id (target &optional session)`
- L138: `(defun turnip:normalize-and-check-target-pane (target)`
- L150: `(defun turnip:format-status (status &optional extra)`
- L162: `(defun turnip:call (&rest arguments)`
- L171: `(defun turnip:call->lines (&rest arguments)`
- L178: `(defun turnip:list-sessions ()`
- L182: `(defun turnip:list-windows (&optional session)`
- L191: `(defun turnip:list-panes (&optional session)`
- L201: `(defun turnip:list-clients ()`
- L205: `(defun turnip:list-buffers ()`
- L211: `(defun turnip:parse-command-options (line)`
- L234: `(defun turnip:parse-command (line)`
- L257: `(defun turnip:list-commands ()`
- L261: `(defun turnip:completions-for-argument (arg &optional session)`
- L269: `(defun turnip:normalize-argument-type (arguments current)`
- L284: `(defun turnip:normalize-argument-value (argument value &optional session)`
- L291: `(defun turnip:prompt-for-command (&optional initial-arguments session)`
- L334: `(defun turnip:send-keys (target &rest keys)`
- L338: `(defun turnip:send-text (target &rest strings)`
- L343: `(defun turnip-attach (session)`
- L360: `(defun turnip-choose-pane (target)`
- L378: `(defun turnip-command (&rest initial-arguments)`
- L415: `(defun turnip-yank-from-buffer (&optional buffer)`
- L430: `(defun turnip-send-region-to-buffer (start end &optional tmux-buffer with-buffer)`
- L459: `(defun turnip-send-region (start end target &optional before-keys)`
- L484: `(provide 'turnip)`
