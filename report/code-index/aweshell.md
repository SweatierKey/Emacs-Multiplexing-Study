# Indice del codice: aweshell

Fonte: https://github.com/manateelazycat/aweshell.git

Revisione: `db495f29eef9013cf6b3796c3797e0ec76352e3f`.


## aweshell.el

- L214: `(require 'eshell)`
- L215: `(require 'cl-lib)`
- L216: `(require 'subr-x)`
- L217: `(require 'seq)`
- L235: `(defcustom aweshell-complete-selection-key "M-h"`
- L240: `(defcustom aweshell-clear-buffer-key "C-l"`
- L245: `(defcustom aweshell-sudo-toggle-key "C-S-l"`
- L250: `(defcustom aweshell-search-history-key "M-'"`
- L255: `(defcustom aweshell-valid-command-color "#98C379"`
- L260: `(defcustom aweshell-invalid-command-color "#FF0000"`
- L275: `(defcustom aweshell-dedicated-window-height 14`
- L280: `(defcustom aweshell-auto-suggestion-p t`
- L288: `(defcustom aweshell-search-history-completing-read-fn 'ido-completing-read`
- L302: `(defun aweshell-kill-buffer-hook ()`
- L309: `(defun aweshell-get-buffer-index ()`
- L321: `(defun aweshell-get-buffer-names ()`
- L330: `(defun aweshell-get-buffer-index-list ()`
- L350: `(defun aweshell-toggle (&optional arg)`
- L378: `(defun aweshell-new ()`
- L383: `(defun aweshell-next ()`
- L398: `(defun aweshell-prev ()`
- L413: `(defun aweshell-clear-buffer ()`
- L420: `(defun aweshell-sudo-toggle ()`
- L436: `(defun aweshell-search-history ()`
- L450: `(defun aweshell-switch-buffer ()`
- L476: `(defun aweshell-switch-buffer--annotate (candidate)`
- L491: `(defun aweshell-current-window-take-height (&optional window)`
- L498: `(defun aweshell-dedicated-exist-p ()`
- L503: `(defun aweshell-window-exist-p (window)`
- L508: `(defun aweshell-buffer-exist-p (buffer)`
- L513: `(defun aweshell-dedicated-open ()`
- L522: `(defun aweshell-dedicated-close ()`
- L534: `(defun aweshell-dedicated-toggle ()`
- L541: `(defun aweshell-dedicated-select-window ()`
- L546: `(defun aweshell-dedicated-pop-window ()`
- L553: `(defun aweshell-dedicated-create-window ()`
- L560: `(defun aweshell-dedicated-split-window ()`
- L571: `(defun aweshell-dedicated-create-buffer ()`
- L610: `(define-key eshell-mode-map (kbd aweshell-clear-buffer-key) 'aweshell-clear-buffer)`
- L611: `(define-key eshell-mode-map (kbd aweshell-sudo-toggle-key) 'aweshell-sudo-toggle)`
- L612: `(define-key eshell-mode-map (kbd aweshell-search-history-key) 'aweshell-search-history)`
- L619: `(require 'eshell-up)`
- L625: `(require 'eshell-prompt-extras)`
- L631: `(defun aweshell-validate-command ()`
- L667: `(defun aweshell-emacs (&rest args)`
- L681: `(defun aweshell-unpack (file &rest args)`
- L705: `(defun aweshell-sync-dir-buffer-name ()`
- L780: `(defun aweshell-cat-with-syntax-highlight (filename)`
- L800: `(defun eshell-command-alert (process status)`
- L925: `(provide 'aweshell)`

## eshell-did-you-mean.el

- L31: `(require 'cl-lib)`
- L32: `(require 'eshell)`
- L33: `(require 'pcomplete)`
- L35: `(defun eshell-did-you-mean--edit-distance (s1 s2)`
- L58: `(defun eshell-did-you-mean--edit-distances (string strings &optional threshold)`
- L76: `(defun eshell-did-you-mean--get-all-commands ()`
- L83: `(defun eshell-did-you-mean-output-filter (output)`
- L108: `(defun eshell-did-you-mean-setup ()`
- L115: `(provide 'eshell-did-you-mean)`

## eshell-prompt-extras.el

- L80: `(require 'em-ls)`
- L81: `(require 'em-dirs)`
- L82: `(require 'esh-ext)`
- L83: `(require 'tramp)`
- L84: `(require 'subr-x)`
- L85: `(require 'seq)`
- L94: `(defcustom epe-show-python-info t`
- L99: `(defcustom epe-git-dirty-char "*"`
- L104: `(defcustom epe-git-untracked-char "?"`
- L109: `(defcustom epe-git-modified-char "!"`
- L114: `(defcustom epe-git-renamed-char "»"`
- L119: `(defcustom epe-git-deleted-char "x"`
- L124: `(defcustom epe-git-added-char "+"`
- L129: `(defcustom epe-git-unmerged-char "≠"`
- L134: `(defcustom epe-git-ahead-char "↑"`
- L139: `(defcustom epe-git-behind-char "↓"`
- L144: `(defcustom epe-git-diverged-char "↕"`
- L149: `(defcustom epe-git-detached-HEAD-char "D:"`
- L154: `(defcustom epe-show-local-working-directory nil`
- L159: `(defcustom epe-path-style 'fish`
- L166: `(defcustom epe-fish-path-max-len 30`
- L171: `(defcustom epe-pipeline-show-time t`
- L176: `(defcustom epe-show-git-status-extended nil`
- L259: `(defmacro epe-colorize-with-face (str face)`
- L263: `(defun epe-pwd ()`
- L269: `(defun epe-abbrev-dir-name (dir)`
- L276: `(defun epe-trim-newline (string)`
- L281: `(defun epe-fish-path (path &optional max-len)`
- L307: `(defun epe-extract-git-component (path)`
- L331: `(defun epe-user-name ()`
- L337: `(defun epe-date-time (&optional format)`
- L341: `(defun epe-status-formatter (timestamp duration)`
- L349: `(defcustom epe-status-min-duration 1`
- L357: `(defun epe-status--record ()`
- L361: `(defun epe-status (&optional formatter min-duration)`
- L383: `(defun epe-remote-p ()`
- L387: `(defun epe-remote-user ()`
- L391: `(defun epe-remote-host ()`
- L407: `(defun epe-git-p ()`
- L413: `(defun epe-git-short-sha1 ()`
- L424: `(defun epe-git-branch ()`
- L433: `(defun epe-git-tag (&optional rev with-distance)`
- L456: `(defun epe-git-dirty ()`
- L462: `(defun epe-git-unpushed-number ()`
- L467: `(defun epe-git-untracked ()`
- L477: `(defun epe-git-modified ()`
- L481: `(defun epe-git-renamed ()`
- L485: `(defun epe-git-deleted ()`
- L489: `(defun epe-git-added ()`
- L493: `(defun epe-git-unmerged ()`
- L497: `(defun epe-git-ahead ()`
- L501: `(defun epe-git-behind ()`
- L505: `(defun epe-git-diverged ()`
- L509: `(defun epe-git-p-helper (command)`
- L513: `(defun epe-git-untracked-p ()`
- L517: `(defun epe-git-added-p ()`
- L522: `(defun epe-git-modified-p ()`
- L528: `(defun epe-git-renamed-p ()`
- L532: `(defun epe-git-deleted-p ()`
- L538: `(defun epe-git-unmerged-p ()`
- L542: `(defun epe-git-ahead-p ()`
- L546: `(defun epe-git-behind-p ()`
- L550: `(defun epe-git-diverged-p ()`
- L561: `(defun epe-theme-lambda ()`
- L589: `(defun epe-theme-dakrone ()`
- L639: `(defun epe-theme-pipeline ()`
- L678: `(defun epe-theme-multiline-with-status ()`
- L714: `(defun epe-git-prompt-info ()`
- L719: `(defun epe-git-default-info ()`
- L729: `(defun epe-git-extended-info ()`
- L736: `(defun epe-git-description ()`
- L744: `(defun epe-git-full-status ()`
- L759: `(provide 'eshell-prompt-extras)`

## eshell-up.el

- L70: `(defun eshell-up-closest-parent-dir (file)`
- L77: `(defun eshell-up-find-parent-dir (path &optional match)`
- L95: `(defun eshell-up (&optional match)`
- L111: `(defun eshell-up-peek (&optional match)`
- L121: `(provide 'eshell-up)`

## exec-path-from-shell.el

- L83: `(defcustom exec-path-from-shell-variables`
- L89: `(defcustom exec-path-from-shell-check-startup-files t`
- L96: `(defcustom exec-path-from-shell-shell-name nil`
- L108: `(defun exec-path-from-shell--double-quote (s)`
- L112: `(defun exec-path-from-shell--shell ()`
- L121: `(defcustom exec-path-from-shell-arguments`
- L131: `(defun exec-path-from-shell--debug (msg &rest args)`
- L136: `(defun exec-path-from-shell--standard-shell-p (shell)`
- L140: `(defun exec-path-from-shell-printf (str &optional args)`
- L175: `(defun exec-path-from-shell-getenvs (names)`
- L197: `(defun exec-path-from-shell-getenv (name)`
- L204: `(defun exec-path-from-shell-setenv (name value)`
- L214: `(defun exec-path-from-shell-copy-envs (names)`
- L227: `(defun exec-path-from-shell--maybe-warn-about-startup-files (pairs)`
- L242: `(defun exec-path-from-shell-copy-env (name)`
- L252: `(defun exec-path-from-shell-initialize ()`
- L262: `(provide 'exec-path-from-shell)`
