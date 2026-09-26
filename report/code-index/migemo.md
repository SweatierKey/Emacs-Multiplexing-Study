# Indice del codice: migemo

Fonte: https://github.com/emacs-jp/migemo.git

Revisione: `c0d84b4092ddade01110ba875559bfd454862ac2`.


## migemo.el

- L33: `(require 'cl-lib)`
- L39: `(defcustom migemo-command "cmigemo"`
- L47: `(defcustom migemo-options '("-q" "--emacs")`
- L52: `(defcustom migemo-white-space-regexp "[ 　\t\r\n]*"`
- L64: `(defcustom migemo-directory nil`
- L69: `(defcustom migemo-isearch-enable-p t`
- L74: `(defcustom migemo-use-default-isearch-keybinding t`
- L79: `(defcustom migemo-dictionary (expand-file-name "migemo-dict" migemo-directory)`
- L84: `(defcustom migemo-user-dictionary (expand-file-name "user-dict" migemo-directory)`
- L91: `(defcustom migemo-regex-dictionary (expand-file-name "regex-dict" migemo-directory)`
- L98: `(defcustom migemo-pre-conv-function nil`
- L105: `(defcustom migemo-after-conv-function nil`
- L112: `(defcustom migemo-coding-system 'utf-8-unix`
- L117: `(defcustom migemo-use-pattern-alist nil`
- L122: `(defcustom migemo-use-frequent-pattern-alist nil`
- L127: `(defcustom migemo-pattern-alist-length 512`
- L132: `(defcustom migemo-pattern-alist-file`
- L138: `(defcustom migemo-frequent-pattern-alist-file`
- L144: `(defcustom migemo-accept-process-output-timeout-msec 5`
- L149: `(defcustom migemo-isearch-min-length 1`
- L176: `(defun migemo-toggle-isearch-enable ()`
- L183: `(defun migemo-start-process (name buffer program args)`
- L191: `(defun migemo-init ()`
- L223: `(defun migemo-replace-in-string (string from to)`
- L232: `(defun migemo-get-pattern (word)`
- L279: `(defun migemo-pattern-alist-load (file)`
- L296: `(defun migemo-pattern-alist-save (&optional clear)`
- L317: `(defun migemo-kill ()`
- L326: `(defun migemo-pattern-alist-clear ()`
- L333: `(defun migemo-frequent-pattern-make (fcfile)`
- L370: `(defun migemo-expand-pattern () "\`
- L384: `(defun migemo-forward (word &optional bound noerror count)`
- L391: `(defun migemo-backward (word &optional bound noerror count)`
- L409: `;; (define-key global-map "\M-;" 'migemo-dabbrev-expand)`
- L410: `(defcustom migemo-dabbrev-display-message nil`
- L415: `(defcustom migemo-dabbrev-ol-face 'highlight`
- L425: `(defun migemo-dabbrev-expand-done ()`
- L433: `(defun migemo-dabbrev-expand ()`
- L509: `(defun migemo--isearch-search (orig-fun &rest args)`
- L518: `(defun migemo--isearch-search-and-update (orig-fun &rest args)`
- L527: `(defun migemo--search-forward (orig-fun &rest args)`
- L533: `(defun migemo--search-backward (orig-fun &rest args)`
- L541: `(defun migemo--multi-isearch-search-fun (orig-val)`
- L548: `(defun isearch-search-fun-migemo ()`
- L584: `(defun migemo--isearch-mode-before (_forward &optional _regexp _op-fun _recursive-edit _regexp-function)`
- L602: `(defun migemo--isearch-done (&optional _nopush _edit)`
- L619: `(defcustom migemo-message-prefix-face 'highlight`
- L624: `(defun migemo--isearch-message-prefix (orig-val)`
- L632: `(defun migemo--isearch-lazy-highlight-new-loop (orig-fun &rest args)`
- L642: `(defun migemo--replace-highlight (orig-fun &rest args)`
- L648: `(defun migemo-register-isearch-keybinding ()`
- L649: `(define-key isearch-mode-map "\C-d" 'migemo-isearch-yank-char)`
- L650: `(define-key isearch-mode-map "\C-w" 'migemo-isearch-yank-word)`
- L651: `(define-key isearch-mode-map "\C-y" 'migemo-isearch-yank-line)`
- L652: `(define-key isearch-mode-map "\M-m" 'migemo-isearch-toggle-migemo))`
- L656: `(defun migemo-isearch-toggle-migemo ()`
- L669: `(defun migemo-isearch-yank-char ()`
- L686: `(defun migemo-isearch-yank-word ()`
- L703: `(defun migemo-isearch-yank-line ()`
- L723: `(provide 'migemo)`
