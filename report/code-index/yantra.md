# Indice del codice: yantra

Fonte: https://github.com/alix559/yantra.git

Revisione: `abd9d94f3cb60abd0200e5427fe9ba715d7c9103`.


## web_editor_api.el

- L3: `(require 'json)`
- L4: `(require 'seq)`
- L5: `(require 'subr-x)`
- L7: `(defcustom web-editor-allowed-roots`
- L15: `(defcustom web-editor-ignored-names`
- L21: `(defun web-editor--json (value)`
- L25: `(defun web-editor--buffer (buffer-name)`
- L30: `(defun web-editor--allowed-path-p (path)`
- L43: `(defun web-editor--validate-path (path)`
- L50: `(defun web-editor--buffer-data (buffer)`
- L65: `(defun web-editor-ping ()`
- L73: `(defun web-editor-create-buffer (buffer-name)`
- L83: `(defun web-editor-open-file (path)`
- L90: `(defun web-editor--file-entry (path &optional root)`
- L98: `(defun web-editor-list-directory (path)`
- L148: `(defun web-editor-get-buffer (buffer-name)`
- L154: `(defun web-editor-replace-buffer`
- L176: `(defun web-editor-save-buffer (buffer-name)`
- L191: `(defun web-editor-indent-buffer (buffer-name)`
- L206: `(defun web-editor-list-buffers ()`
- L233: `(defun web-editor-command-completions (query limit)`
- L253: `(defun web-editor-describe-command (command-name)`
- L297: `(defun web-editor--decode-command-argument (argument)`
- L313: `(defun web-editor-execute-command`
- L348: `(defun web-editor-get-web-frame-state ()`
- L354: `(defun web-editor-set-web-frame-state (state-json)`
- L360: `(provide 'web-editor-api)`
