# Indice del codice: term-manager

Fonte: https://github.com/colonelpanic8/term-manager.git

Revisione: `1581a90ff9b359449e056da55259b9f42e749f0c`.


## term-manager-eat.el

- L30: `(require 'term-manager)`
- L31: `(require 'eat)`
- L33: `(defun term-manager-eat-build-term (directory-symbol)`
- L45: `(provide 'term-manager-eat)`

## term-manager-indexed-mapping.el

- L25: `(require 'dash)`
- L26: `(require 'eieio)`
- L28: `(defun term-manager-plist-delete (plist property)`
- L88: `(provide 'term-manager-indexed-mapping)`

## term-manager.el

- L30: `(require 'cl-lib)`
- L31: `(require 'dash)`
- L32: `(require 'eieio)`
- L33: `(require 'term)`
- L34: `(require 'term-manager-indexed-mapping)`
- L41: `(defcustom term-manager-display-buffer-alist nil`
- L46: `(defun term-manager-display-buffer (buffer)`
- L111: `(defun term-manager-default-build-term (directory-symbol)`
- L138: `(defun term-manager-replace-home-with-tilde (path)`
- L145: `(defun term-manager-default-name-buffer (_buffer symbol)`
- L190: `(provide 'term-manager)`

## term-project.el

- L32: `(require 'project)`
- L33: `(require 'term-manager)`
- L37: `(defun term-project (&rest args)`
- L47: `(defun term-project-maybe-intern (value)`
- L51: `(defun term-project-get-symbol-for-buffer (buffer)`
- L64: `(defun term-project-switch (&rest args)`
- L69: `(defun term-project-global-switch (&rest args)`
- L76: `(defun term-project-get-all-buffers ()`
- L81: `(defun term-project-select-existing ()`
- L88: `(defun term-project-switch-to ()`
- L94: `(defun term-project-forward ()`
- L101: `(defun term-project-backward ()`
- L108: `(cl-defun term-project-create-new (&optional (directory (project-root (project-current))))`
- L117: `(defun term-project-default-directory-forward ()`
- L123: `(defun term-project-default-directory-backward ()`
- L129: `(defun term-project-default-directory-create-new ()`
- L136: `(defun term-project-global-forward ()`
- L143: `(defun term-project-global-backward ()`
- L150: `(defun term-project-global-create-new ()`
- L155: `(provide 'term-project)`

## term-projectile.el

- L30: `(require 'projectile)`
- L31: `(require 'term-manager)`
- L35: `(defun term-projectile (&rest args)`
- L46: `(defun maybe-intern (value)`
- L49: `(defun term-projectile-get-symbol-for-buffer (buffer)`
- L62: `(defun term-projectile-switch (&rest args)`
- L65: `(defun term-projectile-global-switch (&rest args)`
- L70: `(defun term-projectile-get-all-buffers ()`
- L74: `(defun term-projectile-select-existing ()`
- L80: `(defun term-projectile-switch-to ()`
- L86: `(defun term-projectile-forward ()`
- L93: `(defun term-projectile-backward ()`
- L100: `(cl-defun term-projectile-create-new (&optional (directory (projectile-project-root)))`
- L110: `(defun term-projectile-default-directory-forward ()`
- L116: `(defun term-projectile-default-directory-backward ()`
- L122: `(defun term-projectile-default-directory-create-new ()`
- L129: `(defun term-projectile-global-forward ()`
- L136: `(defun term-projectile-global-backward ()`
- L143: `(defun term-projectile-global-create-new ()`
- L148: `(provide 'term-projectile)`
