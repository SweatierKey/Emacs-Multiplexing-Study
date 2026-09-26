# Indice del codice: dropdown-remote

Fonte: https://github.com/SleepyBag/dropdown-remote.git

Revisione: `0445c065373f809a6cca31dde3217d9aee970f07`.


## dropdown-remote.el

- L32: `(require 'emacs-guake)`
- L33: `(require 'emacs-yakuake)`
- L38: `(defun dropdown-toggle-window ()`
- L47: `(defun dropdown-close-current-tab ()`
- L53: `(defun dropdown-run-command-in-current-tab (command)`
- L59: `(defun dropdown-current-tab ()`
- L67: `(defun dropdown-add-tab ()`
- L76: `(defun dropdown-close-tab (tab)`
- L84: `(defun dropdown-run-command-in-tab (tab command)`
- L92: `(defun dropdown-set-tab-title (tab title)`
- L101: `(defun dropdown-terminal-here ()`
- L113: `(provide 'dropdown-remote)`

## emacs-guake.el

- L12: `(defun guake-call-method (method &rest args)`
- L21: `(defun guake-show-hide ()`
- L28: `(defun guake-add-tab (&optional directory)`
- L35: `(defun guake-get-selected-uuid-tab ()`
- L41: `(defun guake-close-tab (tab)`
- L45: `(defun guake-run-command-in-tab (tab command)`
- L50: `(defun guake-rename-tab-uuid (tab title)`
- L58: `(defun guake-split-current-terminal-horizontally ()`
- L63: `(defun guake-split-current-terminal-vertically ()`
- L68: `(provide 'emacs-guake)`

## emacs-yakuake.el

- L14: `(defun yakuake-call-session-method (method &rest args)`
- L22: `(defun yakuake-call-tab-method (method &rest args)`
- L29: `(defun yakuake-call-window-method (method &rest args)`
- L38: `(defun yakuake-toggle-window ()`
- L45: `(defun yakuake-add-session ()`
- L50: `(defun yakuake-remove-session (session)`
- L55: `(defun yakuake-run-command-in-session (session command)`
- L61: `(defun yakuake-split-session-horizontally (session)`
- L66: `(defun yakuake-split-session-vertically (session)`
- L71: `(defun yakuake-set-tab-title (session title)`
- L77: `(defun yakuake-active-session-id ()`
- L83: `(defun yakuake-get-terminal-ids-in-session (session)`
- L91: `(defun yakuake-run-command-in-terminal (terminal command)`
- L96: `(defun yakuake-split-terminal-horizontally (session)`
- L101: `(defun yakuake-split-terminal-vertically (session)`
- L106: `(defun yakuake-active-terminal-id ()`
- L111: `(provide 'emacs-yakuake)`
