# Indice del codice: quick-shell-keybind

Fonte: https://github.com/eyeinsky/quick-shell-keybind.git

Revisione: `eae4ef3673794a202f097b1619ba7cfb79424dfc`.


## quick-shell-keybind.el

- L31: `;;     (global-set-key (kbd "C-c C-t") #'quick-shell-keybind)`
- L41: `(require 'comint)`
- L47: `(defcustom quick-shell-keybind-default-buffer-name "*shell*"`
- L52: `(defun quick-shell-keybind--ask-until (n)`
- L60: `(defun quick-shell-keybind--send (command)`
- L66: `(defun quick-shell-keybind (key buffer commands)`
- L73: `(global-set-key (kbd key)`
- L80: `(provide 'quick-shell-keybind)`
