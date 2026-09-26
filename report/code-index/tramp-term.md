# Indice del codice: tramp-term

Fonte: https://github.com/cuspymd/tramp-term.el.git

Revisione: `276c4d1cb79cc2685df89a02209e2082f74167ea`.


## tramp-term.el

- L43: `(require 'term)`
- L44: `(require 'tramp)`
- L50: `(defcustom tramp-term-default-shell 'bash`
- L60: `(defcustom tramp-term-host-shells '()`
- L72: `(defun tramp-term (&optional host-arg)`
- L91: `(defun tramp-term--do-ssh-login (host)`
- L113: `(defun tramp-term--find-shell-prompt (bound)`
- L117: `(defun tramp-term--find-yesno-prompt (bound)`
- L121: `(defun tramp-term--find-passwd-prompt (bound)`
- L125: `(defun tramp-term--find-service-unknown (bound)`
- L129: `(defun tramp-term--handle-passwd-prompt ()`
- L134: `(defun tramp-term--confirm ()`
- L141: `(defun tramp-term--initialize (hostname)`
- L157: `(defun tramp-term--detect-shell (hostname)`
- L177: `(defun tramp-term--parse-shell-output (detection-marker)`
- L189: `(defun tramp-term--classify-shell (shell-path)`
- L206: `(defun tramp-term--prompt-for-shell (hostname)`
- L215: `(defun tramp-term--initialize-bash (hostname)`
- L228: `(defun tramp-term--initialize-zsh (hostname)`
- L240: `(defun tramp-term--initialize-tcsh (hostname)`
- L251: `(defun tramp-term--select-host ()`
- L265: `(defun tramp-term-prompt (default-host)`
- L271: `(defun tramp-term-default-host ()`
- L278: `(defun tramp-term--parse-hosts (ssh-config)`
- L282: `(defun tramp-term--create-term (new-buffer-name cmd &rest switches)`
- L294: `(provide 'tramp-term)`
