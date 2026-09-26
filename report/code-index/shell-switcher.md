# Indice del codice: shell-switcher

Fonte: https://github.com/DamienCassou/shell-switcher.git

Revisione: `4c96dc27afb519bdbf7bbe42d49a51497f078192`.


## features/step-definitions/shell-switcher-steps.el


## features/support/env.el

- L1: `(require 'f)`
- L14: `(require 'cl)`
- L15: `(require 'shell-switcher)`
- L16: `(require 'espuds)`
- L17: `(require 'ert)`

## rswitcher.el

- L40: `(defun rswitcher-make ()`
- L48: `(defun rswitcher--elements (switcher)`
- L55: `(defun rswitcher--last-pos (switcher)`
- L68: `(defun rswitcher--set-last-pos (switcher last-pos)`
- L74: `(defun rswitcher--increment-last-pos (switcher)`
- L81: `(defun rswitcher--reset-last-pos (switcher)`
- L86: `(defun rswitcher-length (switcher)`
- L91: `(defun rswitcher-empty-p (switcher)`
- L95: `(defun rswitcher--most-recent-pos (switcher)`
- L103: `(defun rswitcher-most-recent (switcher)`
- L107: `(defun rswitcher--push (switcher elt)`
- L112: `(defun rswitcher-make-most-recent-elt-the-first (switcher)`
- L119: `(defun rswitcher-add (switcher elt)`
- L125: `(defun rswitcher--pop (switcher)`
- L132: `(defun rswitcher-memq (switcher elt)`
- L137: `(defun rswitcher--delete (switcher pos)`
- L154: `(defun rswitcher-delete-all (switcher)`
- L159: `(defun rswitcher-delete-most-recent (switcher)`
- L163: `(defun rswitcher--swap-first-two-elts (switcher)`
- L170: `(defun rswitcher-switch-full (switcher)`
- L180: `(defun rswitcher-switch-partial (switcher)`
- L194: `(provide 'rswitcher)`

## shell-switcher.el

- L48: `(require 'rswitcher)`
- L58: `(defcustom shell-switcher-new-shell-function 'shell-switcher-make-eshell`
- L68: `(defcustom shell-switcher-ask-before-creating-new nil`
- L76: `(defcustom shell-switcher-ansi-term-shell ""`
- L91: `(defvar shell-switcher-mode-map`
- L93: `(define-key map (kbd "C-'") 'shell-switcher-switch-buffer)`
- L94: `(define-key map (kbd "C-x 4 '") 'shell-switcher-switch-buffer-other-window)`
- L95: `(define-key map (kbd "C-M-'") 'shell-switcher-new-shell)`
- L100: `(define-minor-mode shell-switcher-mode`
- L121: `(defun shell-switcher-make-shell ()`
- L127: `(defun shell-switcher-make-eshell ()`
- L133: `(defun shell-switcher-make-ansi-term ()`
- L155: `(defun sswitcher--most-recent ()`
- L159: `(defun sswitcher--most-recent-shell-valid-p ()`
- L163: `(defun sswitcher--clean-buffers ()`
- L169: `(defun shell-switcher-kill-all-shells ()`
- L175: `(defun sswitcher--shell-exist-p ()`
- L180: `(defun sswitcher--in-shell-buffer-p ()`
- L184: `(defun shell-switcher-manually-register-shell ()`
- L192: `(defun sswitcher--new-shell (&optional other-window)`
- L205: `(defun sswitcher--no-more-shell-buffers (&optional other-window)`
- L256: `(defun sswitcher--prepare-for-fast-key ()`
- L267: `(define-key map (vector repeat-key)`
- L274: `(defun sswitcher--display-shell-buffer (&optional other-window)`
- L284: `(defun sswitcher--switch-buffer (&optional other-window)`
- L311: `(defun shell-switcher-switch-buffer ()`
- L325: `(defun sswitcher--switch-partially ()`
- L338: `(defun shell-switcher-switch-buffer-other-window ()`
- L346: `(defun shell-switcher-new-shell ()`
- L352: `(defun shell-switcher-open-on-directory (directory)`
- L361: `(defun shell-switcher-open-on-bookmark (bookmark)`
- L372: `(defun shell-switcher-open-on-project (&optional project)`
- L380: `(provide 'shell-switcher)`
