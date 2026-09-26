# Indice del codice: vterm-toggle

Fonte: https://github.com/jixiuf/vterm-toggle.git

Revisione: `a0051a8b8eaa85f8df54ddb032f5710c1f62779d`.


## vterm-toggle.el

- L40: `(require 'cl-lib)`
- L41: `(require 'tramp)`
- L42: `(require 'tramp-sh)`
- L51: `(defcustom vterm-toggle-show-hook nil`
- L56: `(defcustom vterm-toggle-hide-hook nil`
- L61: `(defcustom vterm-toggle-fullscreen-p nil`
- L66: `(defcustom vterm-toggle-scope nil`
- L77: `(defcustom vterm-toggle-project-root t`
- L83: `(defcustom vterm-toggle-cd-auto-create-buffer nil`
- L89: `(defcustom vterm-toggle-reset-window-configration-after-exit 'kill-window-only`
- L97: `(defcustom vterm-toggle-hide-method 'delete-window`
- L114: `(defcustom vterm-toggle-togglable-buffer-functions nil`
- L123: `(defun vterm-toggle-togglable-buffer-p (buffer)`
- L130: `(defun vterm-toggle(&optional args)`
- L149: `(defun vterm-toggle-cd(&optional args)`
- L167: `(defun vterm-toggle-hide (&optional _args)`
- L194: `(defun vterm-toggle--get-window()`
- L199: `(defun vterm-toggle--bury-all-vterm ()`
- L205: `(defun vterm-toggle-tramp-get-method-parameter (method param)`
- L223: `(defun vterm-toggle-cd-show(&optional  args)`
- L230: `(defun vterm-toggle-show(&optional make-cd)`
- L286: `(defun vterm-toggle--wait-prompt()`
- L297: `(defun vterm-toggle-insert-cd()`
- L307: `(defun vterm-toggle--new(&optional buffer-name)`
- L325: `(defun vterm-toggle--get-buffer(&optional make-cd ignore-prompt-p)`
- L340: `(defun vterm-toggle--get-dedicated-buffer()`
- L351: `(defun vterm-toggle--not-in-other-frame(frame buf)`
- L357: `(defun vterm-toggle--recent-vterm-buffer(&optional make-cd ignore-prompt-p dir)`
- L396: `(defun vterm-toggle--in-cmd-buffer-p()`
- L402: `(defun vterm-toggle--project-root()`
- L408: `(defun vterm-toggle--recent-other-buffer(&optional _args)`
- L419: `(defun vterm-toggle--exit-hook()`
- L439: `(defun vterm-toggle--mode-hook()`
- L449: `(defun vterm-toggle--switch (direction offset)`
- L466: `(defun vterm-toggle-forward (&optional offset)`
- L473: `(defun vterm-toggle-backward (&optional offset)`
- L479: `(provide 'vterm-toggle)`
