# Indice del codice: term-toggle

Fonte: https://github.com/amno1/emacs-term-toggle.git

Revisione: `8d3258bc8d03bbb4c735afc681a3c415bb0bbcc6`.


## helm-term-toggle.el

- L41: `(require 'helm)`
- L42: `(require 'seq)`
- L43: `(require 'term-toggle)`
- L59: `(defun tt--helm-candidates ()`
- L79: `(defun tt--helm-at-current-window (fn buf)`
- L89: `(defun tt--helm-toggle (buf)`
- L93: `(defun tt--helm-replace (buf)`
- L110: `(defun helm-term-toggle ()`
- L124: `(defun helm-term-toggle-replace ()`
- L133: `(global-set-key (kbd "C-z t") #'helm-term-toggle-replace)`
- L134: `(define-key term-toggle-minor-mode-map (kbd "C-z t") #'helm-term-toggle-replace)`
- L136: `(provide 'helm-term-toggle)`

## term-toggle-animate.el

- L40: `(require 'term-toggle)`
- L44: `(defcustom term-toggle-side-max-fraction 0.5`
- L49: `(defcustom term-toggle-animation-delay 0.008`
- L60: `(defun tt--animate-window-size (window horizontal)`
- L66: `(defun tt--animate-target (horizontal)`
- L88: `(defun tt--animate-shrink-to-min (window horizontal)`
- L107: `(defun tt--animate-settle (window horizontal target)`
- L121: `(defun tt--animate-stepwise (window horizontal target)`
- L148: `(defun tt--animate-sync-process-size (window)`
- L168: `(defun tt-animate--suppress-adjuster (buffer)`
- L181: `(defun tt-animate--restore-adjuster (buffer saved)`
- L192: `(defun tt-animate--toggle (buffer)`
- L236: `(defun tt-animate--install ()`
- L240: `(defun tt-animate--uninstall ()`
- L244: `(define-minor-mode term-toggle-animate-mode`
- L263: `(provide 'term-toggle-animate)`

## term-toggle.el

- L51: `(require 'seq)`
- L60: `(defcustom term-toggle-default-shell 'ansi-term`
- L74: `(defcustom term-toggle-scope 'directory`
- L98: `(defcustom term-toggle-confirm-exit nil`
- L103: `(defcustom term-toggle-kill-buffer-on-process-exit t`
- L108: `(defcustom term-toggle-minimum-split-height 10`
- L113: `(defcustom term-toggle-default-height 15`
- L119: `(defcustom term-toggle-default-width 80`
- L124: `(defcustom term-toggle-split-side 'below`
- L145: `(defun tt--vterm-available-p ()`
- L150: `(defun tt--ghostel-available-p ()`
- L162: `(defun tt--directory ()`
- L170: `(defun tt--project-root ()`
- L178: `(defun tt--key ()`
- L190: `(defun tt--shell-dir (key)`
- L199: `(defun tt--setup-process (buffer)`
- L211: `(defun tt--make-buffer-name (shell dir)`
- L217: `(defun tt--start (shell key)`
- L261: `(defun tt--find-buffer (shell key)`
- L270: `(defun tt--get-buffer (shell key)`
- L283: `(defun tt--toggle (buffer)`
- L316: `(defun tt--replace (buffer)`
- L335: `(defvar term-toggle-minor-mode-map`
- L337: `(define-key map (kbd "<f1>")    #'term-toggle-close)`
- L338: `(define-key map (kbd "<f10>")   #'term-toggle-cycle)`
- L339: `(define-key map (kbd "<S-f10>") #'term-toggle-cycle-backward)`
- L343: `(define-minor-mode term-toggle-minor-mode`
- L354: `(defun term-toggle-close (&optional replace)`
- L372: `(defun term-toggle-cycle (&optional backward)`
- L407: `(defun term-toggle-cycle-backward ()`
- L412: `(defun term-toggle (&optional shell)`
- L424: `(defun term-toggle-ansi ()`
- L430: `(defun term-toggle-term ()`
- L436: `(defun term-toggle-shell ()`
- L442: `(defun term-toggle-eshell ()`
- L448: `(defun term-toggle-ielm ()`
- L454: `(defun term-toggle-vterm ()`
- L462: `(defun term-toggle-ghostel ()`
- L477: `(provide 'term-toggle)`
