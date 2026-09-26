# Indice del codice: lazy-emacs-terminal

Fonte: https://github.com/lizqwerscott/lazy-emacs-terminal.git

Revisione: `75eee8341b0c2e64376f482577e76b19c0c4a530`.


## early-init.el

- L23: `(provide 'early-init)`

## init.el

- L7: `(require 'cl-lib)`
- L9: `(defun directory-dirs (path)`
- L38: `(require 'init-package)`
- L39: `(require 'init-startup)`
- L41: `(require 'server)`
- L46: `(require 'keybinding)`
- L47: `(require 'init-edit)`
- L48: `(require 'init-ui)`
- L50: `(require 'init-program)`
- L51: `(require 'init-common-lisp)`
- L52: `(require 'init-input)`

## lisp/init-common-lisp.el

- L31: `(provide 'init-common-lisp)`

## lisp/init-corfu.el

- L2: `(defun +complete ()`
- L54: `(provide 'init-corfu)`

## lisp/init-edit.el

- L16: `(require 'awesome-pair)`
- L43: `(define-key awesome-pair-mode-map (kbd "(") 'awesome-pair-open-round)`
- L44: `(define-key awesome-pair-mode-map (kbd "[") 'awesome-pair-open-bracket)`
- L45: `(define-key awesome-pair-mode-map (kbd "{") 'awesome-pair-open-curly)`
- L46: `(define-key awesome-pair-mode-map (kbd ")") 'awesome-pair-close-round)`
- L47: `(define-key awesome-pair-mode-map (kbd "]") 'awesome-pair-close-bracket)`
- L48: `(define-key awesome-pair-mode-map (kbd "}") 'awesome-pair-close-curly)`
- L49: `(define-key awesome-pair-mode-map (kbd "=") 'awesome-pair-equal)`
- L51: `(define-key awesome-pair-mode-map (kbd "%") 'awesome-pair-match-paren)`
- L52: `(define-key awesome-pair-mode-map (kbd "\"") 'awesome-pair-double-quote)`
- L54: `(define-key awesome-pair-mode-map (kbd "SPC") 'awesome-pair-space)`
- L55: `(define-key awesome-pair-mode-map (kbd "RET") 'awesome-pair-newline)`
- L57: `(define-key awesome-pair-mode-map (kbd "C-k") 'awesome-pair-kill)`
- L58: `(define-key awesome-pair-mode-map (kbd "M-o") 'awesome-pair-backward-delete)`
- L59: `(define-key awesome-pair-mode-map (kbd "C-d") 'awesome-pair-forward-delete)`
- L60: `(define-key awesome-pair-mode-map (kbd "C-k") 'awesome-pair-kill)`
- L71: `(provide 'init-edit)`

## lisp/init-input.el

- L12: `(require 'cl-lib)`
- L13: `(require 'posframe)`
- L14: `(defun pyim-probe-meow-normal-mode ()`
- L24: `(global-set-key (kbd "C-\\") 'toggle-input-method)`
- L36: `(provide 'init-input)`

## lisp/init-package.el

- L14: `(require 'package)`
- L35: `(defun site-lisp-update ()`
- L51: `(defun require-package (package &optional min-version no-refresh)`
- L66: `(defun maybe-require-package (package &optional min-version no-refresh)`
- L77: `(provide 'init-package)`

## lisp/init-program.el

- L58: `(require-package 'dumb-jump)`
- L60: `(require 'xref)`
- L61: `(require 'lsp-bridge)`
- L62: `(defun find-definition-with-lsp-bridge ()`
- L76: `(defun return-find-def ()`
- L120: `(require-package 'format-all)`
- L128: `(defun format-this-buffer ()`
- L163: `(require-package 'helpful)`
- L170: `(require-package 'quickrun)`
- L175: `(require-package 'eacl)`
- L180: `(provide 'init-program)`

## lisp/init-startup.el

- L55: `(defun max-gc-limit ()`
- L58: `(defun reset-gc-limit ()`
- L73: `(require-package 'no-littering)`
- L78: `(require 'no-littering)`
- L82: `(require 'recentf)`
- L194: `(require-package 'consult-project-extra)`
- L202: `(require-package 'affe)`
- L204: `(require 'init-corfu)`
- L252: `(provide 'init-startup)`

## lisp/init-ui.el

- L125: `(require-package 'avy)`
- L157: `(provide 'init-ui)`

## lisp/keybinding.el

- L2: `(define-key project-prefix-map`
- L7: `(defun my/meow-quit ()`
- L12: `(defun help-helfup-lsp-bridge-sly ()`
- L22: `(defun meow-setup ()`
- L217: `(global-set-key (kbd "RET") 'newline-and-indent)`
- L218: `(global-set-key (kbd "S-<return>") 'comment-indent-new-line)`
- L220: `(global-set-key (kbd "C-h f") #'helpful-callable)`
- L221: `(global-set-key (kbd "C-h v") #'helpful-variable)`
- L222: `(global-set-key (kbd "C-h k") #'helpful-key)`
- L228: `(global-set-key (kbd "C-h F") #'helpful-function)`
- L235: `(global-set-key (kbd "C-h C") #'helpful-command)`
- L237: `(global-set-key (kbd "s-x") #'execute-extended-command)`
- L239: `(provide 'keybinding)`
