# Indice del codice: eshell

Fonte: https://git.savannah.gnu.org/cgit/emacs.git

Revisione: `30.1`.


## em-alias.el

- L93: `(require 'esh-mode)`
- L103: `(defcustom eshell-aliases-file (expand-file-name "alias" eshell-directory-name)`
- L115: `(defcustom eshell-bad-command-tolerance 3`
- L121: `(defcustom eshell-alias-load-hook nil`
- L146: `(defun eshell-alias-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L155: `(defun eshell-command-aliased-p (name)`
- L158: `(defun eshell/alias (&optional alias &rest definition)`
- L183: `(defun pcomplete/eshell-mode/alias ()`
- L187: `(defun eshell-read-aliases-list ()`
- L207: `(defun eshell-write-aliases-list ()`
- L222: `(defun eshell-maybe-replace-by-alias--which (command)`
- L228: `(defun eshell-maybe-replace-by-alias (command _args)`
- L243: `(defun eshell-alias-completions (name)`
- L252: `(defun eshell-fix-bad-commands (name)`
- L281: `(provide 'em-alias)`

## em-banner.el

- L44: `(require 'esh-util)`
- L45: `(require 'esh-mode)`
- L59: `(defcustom eshell-banner-message "Welcome to the Emacs shell\n\n"`
- L66: `(defcustom eshell-banner-load-hook nil`
- L72: `(defun eshell-banner-initialize ()  ;Called from 'eshell-mode' via intern-soft!`
- L84: `(provide 'em-banner)`

## em-basic.el

- L56: `(require 'esh-cmd)`
- L57: `(require 'esh-io)`
- L58: `(require 'esh-opt)`
- L59: `(require 'esh-util)`
- L72: `(defcustom eshell-plain-echo-behavior nil`
- L81: `(defun eshell-echo (args &optional output-newline)`
- L113: `(defun eshell/echo (&rest args)`
- L140: `(defun eshell/printnl (&rest args)`
- L146: `(defun eshell/listify (&rest args)`
- L154: `(defun eshell/umask (&rest args)`
- L195: `(defun eshell/eshell-debug (&rest args)`
- L223: `(defun pcomplete/eshell-mode/eshell-debug ()`
- L227: `(provide 'em-basic)`

## em-cmpl.el

- L71: `(require 'pcomplete)`
- L73: `(require 'esh-mode)`
- L74: `(require 'esh-util)`
- L75: `(require 'em-dirs)`
- L90: `(defcustom eshell-cmpl-load-hook nil`
- L95: `(defcustom eshell-show-lisp-completions nil`
- L101: `(defcustom eshell-show-lisp-alternatives t`
- L107: `(defcustom eshell-no-completion-during-jobs t`
- L111: `(defcustom eshell-command-completions-alist`
- L136: `(defun eshell-cmpl--custom-variable-docstring (pcomplete-var)`
- L143: `(defcustom eshell-cmpl-file-ignore "~\\'"`
- L147: `(defcustom eshell-cmpl-dir-ignore "\\'\\(\\.\\.?\\|CVS\\)/\\'"`
- L151: `(defcustom eshell-cmpl-remote-file-ignore nil`
- L156: `(defcustom eshell-cmpl-ignore-case (eshell-under-windows-p)`
- L160: `(defcustom eshell-cmpl-autolist nil`
- L164: `(defcustom eshell-cmpl-recexact nil`
- L168: `(defcustom eshell-cmpl-man-function #'man`
- L172: `(defcustom eshell-cmpl-compare-entry-function #'file-newer-than-file-p`
- L176: `(defcustom eshell-cmpl-expand-before-complete nil`
- L180: `(defcustom eshell-cmpl-cycle-completions t`
- L184: `(defcustom eshell-cmpl-cycle-cutoff-length 5`
- L188: `(defcustom eshell-cmpl-restore-window-delay 1`
- L192: `(defcustom eshell-command-completion-function`
- L198: `(defcustom eshell-cmpl-command-name-function`
- L203: `(defcustom eshell-default-completion-function`
- L212: `(defcustom eshell-cmpl-use-paring t`
- L218: `(defun eshell-complete-lisp-symbol ()`
- L224: `(defvar-keymap eshell-cmpl-mode-map`
- L236: `(define-minor-mode eshell-cmpl-mode`
- L242: `(defun eshell-cmpl-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L291: `(defun eshell-completion-command-name ()`
- L302: `(defun eshell-completion-help ()`
- L308: `(defun eshell--pcomplete-insert-tab ()`
- L314: `(defun eshell-complete--eval-argument-form (arg)`
- L336: `(defun eshell-external-command-p (command)`
- L344: `(defun eshell-complete-parse-arguments ()`
- L453: `(defun eshell--complete-commands-list ()`
- L521: `(provide 'em-cmpl)`

## em-dirs.el

- L45: `(require 'esh-mode)                     ;For eshell-directory-name`
- L46: `(require 'esh-var)                      ;For eshell-variable-aliases-list`
- L47: `(require 'ring)`
- L48: `(require 'esh-opt)`
- L63: `(defcustom eshell-dirs-load-hook nil`
- L68: `(defcustom eshell-pwd-convert-function (if (eshell-under-windows-p)`
- L80: `(defcustom eshell-ask-to-save-last-dir 'always`
- L92: `(defcustom eshell-cd-shows-directory nil`
- L96: `(defcustom eshell-cd-on-directory t`
- L100: `(defcustom eshell-directory-change-hook nil`
- L104: `(defcustom eshell-list-files-after-cd nil`
- L111: `(defcustom eshell-pushd-tohome nil`
- L116: `(defcustom eshell-pushd-dextract nil`
- L121: `(defcustom eshell-pushd-dunique nil`
- L126: `(defcustom eshell-dirtrack-verbose t`
- L131: `(defcustom eshell-last-dir-ring-file-name`
- L138: `(defcustom eshell-last-dir-ring-size 32`
- L158: `(defcustom eshell-last-dir-unique t`
- L173: `(defun eshell-dirs-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L228: `(defun eshell-save-some-last-dir ()`
- L243: `(defun eshell-lone-directory-p (file)`
- L249: `(defun eshell-dirs-substitute-cd (&rest args)`
- L256: `(defun eshell-expand-user-reference (file)`
- L262: `(defun eshell-parse-user-reference ()`
- L273: `(defun eshell-parse-drive-letter ()`
- L288: `(defun eshell-complete-user-reference ()`
- L320: `(defun eshell/pwd ()`
- L331: `(defun eshell-expand-multiple-dots (filename)`
- L356: `(defun eshell-find-previous-directory (regexp)`
- L370: `(defun eshell/cd (&rest args)           ; all but first ignored`
- L437: `(defun eshell-add-to-dir-ring (path)`
- L451: `(defun eshell/pushd (&rest args)        ; all but first ignored`
- L502: `(defun eshell/popd (&rest args)`
- L532: `(defun eshell/dirs (&optional if-verbose)`
- L548: `(defun eshell-read-last-dir-ring ()`
- L576: `(defun eshell-write-last-dir-ring ()`
- L600: `(provide 'em-dirs)`

## em-elecslash.el

- L28: `(require 'tramp)`
- L29: `(require 'thingatpt)`
- L30: `(require 'esh-cmd)`
- L31: `(require 'esh-ext)`
- L32: `(require 'esh-mode)`
- L57: `(defun eshell-elecslash-initialize () ;Called from 'eshell-mode' via intern-soft!`
- L62: `(defun eshell-electric-forward-slash ()`
- L103: `(define-key map "/" (lambda ()`
- L110: `(provide 'em-elecslash)`

## em-extpipe.el

- L31: `(require 'cl-lib)`
- L32: `(require 'esh-arg)`
- L33: `(require 'esh-cmd)`
- L34: `(require 'esh-io)`
- L35: `(require 'esh-util)`
- L56: `(defun eshell-extpipe-initialize () ;Called from 'eshell-mode' via intern-soft!`
- L67: `(defmacro eshell-extpipe--or-with-catch (&rest disjuncts)`
- L80: `(defun eshell-parse-external-pipeline ()`
- L203: `(defun eshell-rewrite-external-pipeline (terms)`
- L219: `(provide 'em-extpipe)`

## em-glob.el

- L52: `(require 'esh-arg)`
- L53: `(require 'esh-module)`
- L54: `(require 'esh-util)`
- L66: `(defcustom eshell-glob-load-hook nil`
- L72: `(defcustom eshell-glob-splice-results nil`
- L81: `(defcustom eshell-glob-include-dot-files nil`
- L86: `(defcustom eshell-glob-include-dot-dot t`
- L91: `(defcustom eshell-glob-case-insensitive (not (not (eshell-under-windows-p)))`
- L96: `(defcustom eshell-glob-show-progress nil`
- L102: `(defcustom eshell-error-if-no-glob nil`
- L108: `(defcustom eshell-glob-chars-list '(?\] ?\[ ?* ?? ?~ ?\( ?\) ?| ?# ?^)`
- L113: `(defcustom eshell-glob-translate-alist`
- L138: `(defun eshell-glob-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L148: `(defun eshell-no-command-globbing (terms)`
- L156: `(defun eshell-add-glob-modifier ()`
- L162: `(defun eshell-parse-glob-chars ()`
- L199: `(defun eshell-glob-regexp (pattern)`
- L245: `(defun eshell-glob-p (pattern)`
- L249: `(defun eshell-glob-convert-1 (glob &optional last)`
- L284: `(defun eshell-glob-convert (glob)`
- L327: `(defun eshell-extended-glob (glob)`
- L364: `(defun eshell-glob-entries (path globs only-dirs)`
- L419: `(provide 'em-glob)`

## em-hist.el

- L59: `(require 'ring)`
- L60: `(require 'esh-opt)`
- L61: `(require 'esh-mode)`
- L72: `(defcustom eshell-hist-load-hook nil`
- L77: `(defcustom eshell-hist-unload-hook`
- L85: `(defcustom eshell-history-file-name`
- L93: `(defcustom eshell-history-size 128`
- L98: `(defcustom eshell-hist-ignoredups nil`
- L107: `(defcustom eshell-save-history-on-exit t`
- L119: `(defcustom eshell-history-append nil`
- L125: `(defcustom eshell-input-filter 'eshell-input-filter-default`
- L135: `(defun eshell-hist--update-keymap (symbol value)`
- L150: `(keymap-set eshell-hist-mode-map (car keyb) (cdr keyb))))`
- L153: `(defcustom eshell-hist-match-partial t`
- L161: `(defcustom eshell-hist-move-to-end t`
- L165: `(defcustom eshell-hist-event-designator`
- L170: `(defcustom eshell-hist-word-designator`
- L175: `(defcustom eshell-hist-modifier`
- L180: `(defcustom eshell-hist-rebind-keys-alist`
- L208: `(defvar-keymap eshell-isearch-map`
- L219: `(defvar-keymap eshell-hist-mode-map`
- L238: `(defun eshell-input-filter-default (input)`
- L243: `(defun eshell-input-filter-initial-space (input)`
- L248: `(define-minor-mode eshell-hist-mode`
- L254: `(defun eshell-hist-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L310: `(defun eshell--save-history ()`
- L314: `(defun eshell-save-some-history ()`
- L330: `(defun eshell/history (&rest args)`
- L376: `(defun eshell-put-history (input &optional ring at-beginning)`
- L383: `(defun eshell-get-history (index &optional ring)`
- L387: `(defun eshell-add-input-to-history (input)`
- L410: `(defun eshell-add-to-history ()`
- L420: `(defun eshell-read-history (&optional filename silent)`
- L470: `(defun eshell-write-history (&optional filename append)`
- L513: `(defun eshell-list-history ()`
- L552: `(defun eshell-hist-word-reference (ref)`
- L562: `(defun eshell-hist-parse-arguments (&optional b e)`
- L600: `(defun eshell-expand-history-references (beg end)`
- L631: `(defun eshell-complete-history-reference ()`
- L660: `(defun eshell-history-substitution (line)`
- L680: `(defun eshell-history-reference (reference)`
- L712: `(defun eshell-hist-parse-event-designator (reference)`
- L739: `(defun eshell-hist-parse-word-designator (hist reference)`
- L777: `(defun eshell-hist-parse-modifier (hist reference)`
- L793: `(defun eshell-get-next-from-history ()`
- L804: `(defun eshell-search-arg (arg)`
- L821: `(defun eshell-search-start (arg)`
- L833: `(defun eshell-previous-input-string (arg)`
- L841: `(defun eshell-previous-input (arg)`
- L846: `(defun eshell-next-input (arg)`
- L851: `(defun eshell-previous-matching-input-string (regexp arg)`
- L857: `(defun eshell-previous-matching-input-string-position`
- L887: `(defun eshell-previous-matching-input (regexp arg)`
- L907: `(defun eshell-next-matching-input (regexp arg)`
- L915: `(defun eshell-previous-matching-input-from-input (arg)`
- L932: `(defun eshell-next-matching-input-from-input (arg)`
- L940: `(defun eshell-test-imatch ()`
- L956: `(defun eshell-return-to-prompt ()`
- L984: `(defun eshell-prepare-for-search ()`
- L994: `(defun eshell-isearch-backward (&optional invert)`
- L1004: `(defun eshell-isearch-repeat-backward (&optional invert)`
- L1017: `(defun eshell-isearch-forward ()`
- L1022: `(defun eshell-isearch-repeat-forward ()`
- L1027: `(defun eshell-isearch-cancel ()`
- L1033: `(defun eshell-isearch-abort ()`
- L1039: `(defun eshell-isearch-delete-char ()`
- L1044: `(defun eshell-isearch-return ()`
- L1049: `(defun em-hist-unload-function ()`
- L1052: `(provide 'em-hist)`

## em-ls.el

- L29: `(require 'cl-lib)`
- L30: `(require 'esh-util)`
- L31: `(require 'esh-opt)`
- L32: `(require 'esh-proc)`
- L33: `(require 'esh-cmd)`
- L48: `(defcustom eshell-ls-date-format "%Y-%m-%d"`
- L55: `(defcustom eshell-ls-initial-args nil`
- L60: `(defcustom eshell-ls-dired-initial-args nil`
- L65: `(defun eshell-ls-enable-in-dired ()`
- L71: `(defun eshell-ls-disable-in-dired ()`
- L76: `(defcustom eshell-ls-use-in-dired nil`
- L87: `(defcustom eshell-ls-default-blocksize 1024`
- L91: `(defcustom eshell-ls-exclude-regexp nil`
- L95: `(defcustom eshell-ls-exclude-hidden t`
- L101: `(defcustom eshell-ls-use-colors t`
- L140: `(defcustom eshell-ls-archive-regexp`
- L154: `(defcustom eshell-ls-backup-regexp`
- L164: `(defcustom eshell-ls-product-regexp`
- L176: `(defcustom eshell-ls-clutter-regexp`
- L193: `(defmacro eshell-ls-applicable (attrs index func file)`
- L217: `(defcustom eshell-ls-highlight-alist nil`
- L250: `(defun eshell-ls--insert-directory`
- L297: `(defun eshell-ls--dired (orig-fun dir-or-list &optional switches)`
- L335: `(defun eshell-do-ls (&rest args)`
- L438: `(defun eshell-ls-annotate (fileinfo)`
- L471: `(defun eshell-ls-file (fileinfo &optional size-width copy-fileinfo)`
- L534: `(defun eshell-ls-dir (dirinfo &optional insert-name root-dir size-width)`
- L620: `(defun eshell-ls-sort-entries (entries)`
- L658: `(defun eshell-ls-files (files &optional size-width copy-fileinfo)`
- L738: `(defun eshell-ls-entries (entries &optional separate root-dir)`
- L784: `(defun eshell-ls-find-column-widths (files)`
- L830: `(defun eshell-ls-find-column-lengths (files)`
- L896: `(defun eshell-ls-decorated-name (file)`
- L951: `(defun em-ls-unload-function ()`
- L954: `(provide 'em-ls)`

## em-pred.el

- L49: `(require 'esh-mode)`
- L63: `(defcustom eshell-pred-load-hook nil`
- L68: `(defcustom eshell-predicate-alist`
- L113: `(defcustom eshell-modifier-alist`
- L238: `(defvar-keymap eshell-pred-mode-map`
- L244: `(defun eshell-display-predicate-help ()`
- L250: `(defun eshell-display-modifier-help ()`
- L256: `(define-minor-mode eshell-pred-mode`
- L262: `(defun eshell-pred-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L268: `(defun eshell-apply-modifiers (lst predicates modifiers string-desc)`
- L289: `(defun eshell-parse-arg-modifier ()`
- L316: `(defun eshell-parse-modifiers ()`
- L378: `(defun eshell-add-pred-func (pred funcs negate follow)`
- L388: `(defun eshell-get-comparison-modifier-argument (&optional functions)`
- L402: `(defun eshell-get-numeric-modifier-argument ()`
- L410: `(defun eshell-get-delimited-modifier-argument (&optional chained-p)`
- L433: `(defun eshell-pred-user-or-group (mod-char mod-type attr-index get-id-func)`
- L448: `(defun eshell-pred-file-time (mod-char mod-type attr-index)`
- L482: `(defun eshell-pred-file-type (type)`
- L504: `(defun eshell-pred-file-links ()`
- L513: `(defun eshell-pred-file-size ()`
- L534: `(defun eshell-pred-substitute (&optional repeat)`
- L549: `(defun eshell-include-members (mod-char &optional invert-p)`
- L562: `(defun eshell-join-members ()`
- L569: `(defun eshell-split-members ()`
- L578: `(provide 'em-pred)`

## em-prompt.el

- L29: `(require 'esh-mode)`
- L30: `(require 'text-property-search)`
- L42: `(defcustom eshell-prompt-load-hook nil`
- L50: `(defcustom eshell-prompt-function`
- L60: `(defcustom eshell-prompt-regexp "^[^#$\n]* [#$] "`
- L66: `(defcustom eshell-highlight-prompt t`
- L80: `(defcustom eshell-before-prompt-hook nil`
- L86: `(defcustom eshell-after-prompt-hook nil`
- L96: `(defvar-keymap eshell-prompt-mode-map`
- L102: `(defvar-keymap eshell-prompt-repeat-map`
- L110: `(define-minor-mode eshell-prompt-mode`
- L116: `(defun eshell-prompt-initialize ()  ;Called from 'eshell-mode' via intern-soft!`
- L122: `(defun eshell-emit-prompt ()`
- L145: `(defun eshell-forward-matching-input (regexp arg)`
- L161: `(defun eshell-backward-matching-input (regexp arg)`
- L168: `(defun eshell-forward-paragraph (&optional n)`
- L198: `(defun eshell-backward-paragraph (&optional n)`
- L204: `(defun eshell-next-prompt (&optional n)`
- L233: `(defun eshell-previous-prompt (&optional n)`
- L238: `(defun eshell-skip-prompt ()`
- L247: `(defun eshell-bol-ignoring-prompt (arg)`
- L255: `(provide 'em-prompt)`

## em-rebind.el

- L26: `(require 'esh-mode)`
- L48: `(defcustom eshell-rebind-load-hook nil`
- L54: `(defcustom eshell-rebind-keys-alist`
- L66: `(defcustom eshell-confine-point-to-input t`
- L81: `(defcustom eshell-error-if-move-away t`
- L87: `(defcustom eshell-remap-previous-input t`
- L92: `(defcustom eshell-cannot-leave-input-list`
- L139: `(defvar-keymap eshell-rebind-mode-map`
- L144: `(defvar eshell-input-keymap)`
- L146: `(defvar eshell-lock-keymap)`
- L150: `(define-minor-mode eshell-rebind-mode`
- L156: `(defun eshell-rebind-initialize ()  ;Called from 'eshell-mode' via intern-soft!`
- L167: `(defun eshell-lock-local-map (&optional arg)`
- L181: `(defun eshell-save-previous-point ()`
- L199: `(defun eshell-rebind-input-map ()`
- L218: `(defun eshell-setup-input-keymap ()`
- L224: `(define-key eshell-input-keymap (caar bindings)`
- L228: `(defun eshell-delete-backward-char (n)`
- L236: `(defun eshell-delchar-or-maybe-eof (arg)`
- L252: `(provide 'em-rebind)`

## em-script.el

- L26: `(require 'esh-mode)`
- L27: `(require 'esh-io)`
- L39: `(defcustom eshell-script-load-hook nil`
- L45: `(defcustom eshell-login-script (expand-file-name "login" eshell-directory-name)`
- L52: `(defcustom eshell-rc-script (expand-file-name "profile" eshell-directory-name)`
- L60: `(defun eshell-script-initialize ()  ;Called from 'eshell-mode' via intern-soft!`
- L87: `(defun eshell--source-file (file &optional args subcommand-p)`
- L101: `(defun eshell-source-file (file &optional args subcommand-p)`
- L109: `(defun eshell-execute-file (file &optional args destination)`
- L149: `(defun eshell-batch-file ()`
- L176: `(defun eshell/source (file &rest args)`
- L183: `(defun eshell/. (file &rest args)`
- L190: `(provide 'em-script)`

## em-smart.el

- L71: `(require 'esh-mode)`
- L88: `(defcustom eshell-smart-load-hook nil`
- L94: `(defcustom eshell-smart-unload-hook`
- L104: `(defcustom eshell-review-quick-commands nil`
- L121: `(defcustom eshell-smart-display-navigate-list`
- L133: `(defcustom eshell-smart-space-goes-to-end t`
- L152: `(defcustom eshell-where-to-jump 'begin`
- L166: `(defun eshell-smart-initialize ()   ;Called from 'eshell-mode' via intern-soft!`
- L193: `(defun eshell-smart-scroll-windows ()`
- L203: `(defun eshell-smart-display-setup ()`
- L221: `(defun eshell-disable-after-change (_b _e _l)`
- L227: `(defun eshell-smart-maybe-jump-to-end ()`
- L240: `(defun eshell-smart-scroll ()`
- L257: `(defun eshell-smart-goto-end ()`
- L262: `(defun eshell-smart-display-move ()`
- L302: `(defun em-smart-unload-hook ()`
- L305: `(provide 'em-smart)`

## em-term.el

- L34: `(require 'cl-lib)`
- L35: `(require 'esh-util)`
- L36: `(require 'esh-ext)`
- L37: `(require 'term)`
- L52: `(defcustom eshell-term-load-hook nil`
- L57: `(defcustom eshell-visual-commands`
- L72: `(defcustom eshell-visual-subcommands`
- L93: `(defcustom eshell-visual-options`
- L116: `(defcustom eshell-term-name term-term-name`
- L123: `(defcustom eshell-escape-control-x t`
- L131: `(defcustom eshell-destroy-buffer-when-process-dies nil`
- L144: `(defun eshell-term-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L151: `(defun eshell-visual-command-p (command args)`
- L164: `(defun eshell-exec-visual (&rest args)`
- L196: `(defun eshell-term-sentinel (proc msg)`
- L286: `;       (define-key eshell-term-raw-map eshell-term-escape-char 'eshell-term-send-raw))`
- L288: `;   (define-key eshell-term-raw-map c eshell-term-raw-escape-map)`
- L290: `;   (define-key eshell-term-raw-escape-map "\C-x"`
- L292: `;   (define-key eshell-term-raw-escape-map "\C-v"`
- L294: `;   (define-key eshell-term-raw-escape-map "\C-u"`
- L296: `;   (define-key eshell-term-raw-escape-map c 'eshell-term-send-raw))`
- L308: `;	  (define-key map (make-string 1 i) 'eshell-term-send-raw)`
- L309: `;	  (define-key esc-map (make-string 1 i) 'eshell-term-send-raw-meta)`
- L311: `;	(define-key map "\e" esc-map)`
- L315: `;	(define-key eshell-term-raw-map [mouse-2] 'eshell-term-mouse-paste)`
- L316: `;	(define-key eshell-term-raw-map [up] 'eshell-term-send-up)`
- L317: `;	(define-key eshell-term-raw-map [down] 'eshell-term-send-down)`
- L318: `;	(define-key eshell-term-raw-map [right] 'eshell-term-send-right)`
- L319: `;	(define-key eshell-term-raw-map [left] 'eshell-term-send-left)`
- L320: `;	(define-key eshell-term-raw-map [delete] 'eshell-term-send-del)`
- L321: `;	(define-key eshell-term-raw-map [backspace] 'eshell-term-send-backspace)`
- L322: `;	(define-key eshell-term-raw-map [home] 'eshell-term-send-home)`
- L323: `;	(define-key eshell-term-raw-map [end] 'eshell-term-send-end)`
- L324: `;	(define-key eshell-term-raw-map [prior] 'eshell-term-send-prior)`
- L325: `;	(define-key eshell-term-raw-map [next] 'eshell-term-send-next)`
- L332: `(provide 'em-term)`

## em-tramp.el

- L28: `(require 'esh-util)`
- L29: `(require 'esh-cmd)`
- L34: `(require 'tramp)`
- L50: `(defun eshell-tramp-initialize ()   ;Called from 'eshell-mode' via intern-soft!`
- L61: `(defun eshell/su (&rest args)`
- L95: `(defun eshell--method-wrap-directory (directory method &optional user)`
- L110: `(defun eshell/sudo (&rest args)`
- L132: `(defun eshell/doas (&rest args)`
- L154: `(provide 'em-tramp)`

## em-unix.el

- L38: `(require 'esh-mode)`
- L39: `(require 'pcomplete)`
- L56: `(defcustom eshell-unix-load-hook nil`
- L62: `(defcustom eshell-plain-grep-behavior nil`
- L69: `(defcustom eshell-no-grep-available (not (eshell-search-path "grep"))`
- L74: `(defcustom eshell-plain-diff-behavior nil`
- L81: `(defcustom eshell-plain-locate-behavior (featurep 'xemacs)`
- L88: `(defcustom eshell-rm-removes-directories nil`
- L103: `(defcustom eshell-rm-interactive-query 'root`
- L111: `(defcustom eshell-mv-interactive-query 'root`
- L119: `(defcustom eshell-mv-overwrite-files t`
- L124: `(defcustom eshell-cp-interactive-query 'root`
- L132: `(defcustom eshell-cp-overwrite-files t`
- L137: `(defcustom eshell-ln-interactive-query 'root`
- L145: `(defcustom eshell-ln-overwrite-files nil`
- L150: `(defcustom eshell-default-target-is-dot nil`
- L155: `(defcustom eshell-du-prefer-over-ange nil`
- L163: `(defun eshell-unix-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L183: `(defun eshell-interactive-query-p (value)`
- L194: `(defun eshell/man (&rest args)`
- L200: `(defun eshell/info (&rest args)`
- L231: `(defun eshell-remove-entries (files &optional toplevel)`
- L262: `(defun eshell/rm (&rest args)`
- L346: `(defun eshell/mkdir (&rest args)`
- L364: `(defun eshell/rmdir (&rest args)`
- L385: `(defun eshell-shuffle-files (command action files target func deep &rest args)`
- L486: `(defun eshell-shorthand-tar-command (command args)`
- L508: `(defmacro eshell-mvcpln-template (command action func query-var`
- L537: `(defun eshell/mv (&rest args)`
- L566: `(defun eshell/cp (&rest args)`
- L605: `(defun eshell/ln (&rest args)`
- L639: `(defun eshell/cat (&rest args)`
- L691: `(defun eshell-compile (command args &optional method mode)`
- L716: `(defun eshell/compile (&rest args)`
- L734: `(defun eshell/make (&rest args)`
- L744: `(defun eshell-occur-mode-goto-occurrence ()`
- L751: `(defun eshell-occur-mode-mouse-goto (event)`
- L762: `(defun eshell-poor-mans-grep (args)`
- L806: `(defun eshell-grep (command args &optional maybe-use-occur)`
- L818: `(defun eshell/grep (&rest args)`
- L822: `(defun eshell/egrep (&rest args)`
- L826: `(defun eshell/fgrep (&rest args)`
- L830: `(defun eshell/agrep (&rest args)`
- L834: `(defun eshell/rgrep (&rest args)`
- L838: `(defun eshell/glimpse (&rest args)`
- L848: `(defun eshell-complete-host-reference ()`
- L876: `(defun eshell-du-sum-directory (path depth)`
- L911: `(defun eshell/du (&rest args)`
- L979: `(defun eshell-show-elapsed-time ()`
- L986: `(defun eshell/time (&rest args)`
- L1016: `(defun eshell/whoami ()`
- L1020: `(defun eshell-nil-blank-string (string)`
- L1028: `(defun eshell/diff (&rest args)`
- L1062: `(defun eshell/locate (&rest args)`
- L1079: `(defun eshell/occur (&rest args)`
- L1093: `(provide 'em-unix)`

## em-xtra.el

- L26: `(require 'cl-lib)`
- L27: `(require 'esh-util)`
- L45: `(defun eshell/expr (&rest args)`
- L49: `(defun eshell/substitute (&rest args)`
- L54: `(defun eshell/count (&rest args)`
- L59: `(defun eshell/mismatch (&rest args)`
- L64: `(defun eshell/union (&rest args)`
- L69: `(defun eshell/intersection (&rest args)`
- L74: `(defun eshell/set-difference (&rest args)`
- L79: `(defun eshell/set-exclusive-or (&rest args)`
- L87: `(provide 'em-xtra)`

## esh-arg.el

- L30: `(require 'esh-util)`
- L31: `(require 'esh-module)`
- L33: `(require 'pcomplete)`
- L59: `(defcustom eshell-arg-load-hook nil`
- L65: `(defcustom eshell-delimiter-argument-list '(?\; ?& ?\| ?\> ?\s ?\t ?\n)`
- L70: `(defcustom eshell-special-chars-inside-quoting '(?\\ ?\")`
- L75: `(defcustom eshell-special-chars-outside-quoting`
- L89: `(defcustom eshell-parse-argument-hook`
- L196: `(defcustom eshell-special-ref-default "buffer"`
- L205: `(defvar-keymap eshell-arg-mode-map`
- L210: `(define-minor-mode eshell-arg-mode`
- L216: `(defun eshell-arg-initialize ()     ;Called from 'eshell-mode' via intern-soft!`
- L232: `(defun eshell-concat (quoted &rest rest)`
- L272: `(defun eshell-concat-1 (quoted first second)`
- L282: `(defun eshell-concat-groups (quoted &rest args)`
- L315: `(defun eshell-resolve-current-argument ()`
- L339: `(defun eshell-finish-arg (&rest arguments)`
- L352: `(defun eshell-quote-argument (string)`
- L367: `(defun eshell-parse-arguments (beg end)`
- L400: `(defun eshell-parse-argument ()`
- L450: `(defun eshell-quote-backslash (string &optional index)`
- L462: `(defun eshell-parse-backslash ()`
- L494: `(defun eshell-parse-literal-quote ()`
- L506: `(defun eshell-parse-double-quote ()`
- L523: `(defun eshell-unescape-inner-double-quote (bound)`
- L547: `(defun eshell-parse-delimiter ()`
- L564: `(defun eshell-prepare-splice (args)`
- L600: `(defun eshell-parse-special-reference ()`
- L633: `(defun eshell-insert-special-reference (type &rest args)`
- L649: `(defun eshell-complete-special-reference ()`
- L709: `(defun eshell-get-buffer (buffer-or-name)`
- L715: `(defun eshell-insert-buffer-name (buffer-name)`
- L720: `(defun eshell-complete-buffer-ref ()`
- L724: `(defun eshell-get-marker (position buffer-or-name)`
- L733: `(defun eshell-insert-marker (position buffer-name)`
- L740: `(defun eshell-complete-marker-ref ()`
- L745: `(provide 'esh-arg)`

## esh-cmd.el

- L103: `(require 'esh-util)`
- L104: `(require 'esh-arg)`
- L105: `(require 'esh-proc)`
- L106: `(require 'esh-module)`
- L107: `(require 'esh-io)`
- L108: `(require 'esh-ext)`
- L110: `(require 'eldoc)`
- L111: `(require 'generator)`
- L112: `(require 'pcomplete)`
- L125: `(defcustom eshell-prefer-lisp-functions nil`
- L129: `(defcustom eshell-lisp-regexp "\\([(']\\|#'\\)"`
- L134: `(defcustom eshell-lisp-form-nil-is-failure t`
- L138: `(defcustom eshell-pre-command-hook nil`
- L142: `(defcustom eshell-post-command-hook nil`
- L146: `(defcustom eshell-prepare-command-hook nil`
- L156: `(defcustom eshell-named-command-hook nil`
- L184: `(defcustom eshell-pre-rewrite-command-hook`
- L192: `(defcustom eshell-rewrite-command-hook`
- L222: `(defcustom eshell-complex-commands '("ls")`
- L238: `(defcustom eshell-cmd-load-hook nil`
- L243: `(defcustom eshell-deferrable-commands`
- L253: `(defcustom eshell-subcommand-bindings`
- L323: `(defun eshell-cmd-initialize ()     ;Called from 'eshell-mode' via intern-soft!`
- L342: `(defun eshell-complete-lisp-symbols ()`
- L353: `(defun eshell-add-command (form &optional background)`
- L365: `(defun eshell-remove-command (command)`
- L377: `(defun eshell-commands-for-process (process)`
- L394: `(defun eshell-parse-command (command &optional args toplevel)`
- L448: `(defun eshell-debug-show-parsed-args (terms)`
- L453: `(defun eshell-no-command-conversion (terms)`
- L460: `(defun eshell-subcommand-arg-values (terms)`
- L470: `(defun eshell-rewrite-sexp-command (terms)`
- L477: `(defun eshell-rewrite-initial-subcommand (terms)`
- L483: `(defun eshell-rewrite-named-command (terms)`
- L529: `(defun eshell-rewrite-for-command (terms)`
- L556: `(defun eshell-structure-basic-command (func names keyword test body`
- L587: `(defun eshell-rewrite-while-command (terms)`
- L600: `(defun eshell-rewrite-if-command (terms)`
- L619: `(defun eshell-exit-success-p ()`
- L626: `(defun eshell-parse-pipeline (terms)`
- L664: `(defun eshell-parse-subcommand-argument ()`
- L680: `(defun eshell-parse-lisp-argument ()`
- L696: `(defun eshell-split-commands (terms separator &optional`
- L724: `(defun eshell-separate-commands (terms separator &optional`
- L760: `(defmacro eshell-do-subjob (object)`
- L770: `(defmacro eshell-commands (object &optional silent)`
- L779: `(defmacro eshell-trap-errors (object)`
- L796: `(defmacro eshell-with-copied-handles (object &optional steal-p)`
- L807: `(defmacro eshell-protect (object)`
- L813: `(defun eshell--unmark-deferrable (command)`
- L827: `(defmacro eshell-do-pipelines (pipeline &optional notfirst)`
- L854: `(defmacro eshell-do-pipelines-synchronously (pipeline)`
- L884: `(defmacro eshell-execute-pipeline (pipeline)`
- L891: `(defmacro eshell-as-subcommand (command)`
- L901: `(defmacro eshell-do-command-to-value (object)`
- L911: `(defmacro eshell-command-to-value (command)`
- L946: `(defun eshell--invoke-command-directly-p (command)`
- L978: `(defun eshell-invoke-directly-p (command)`
- L989: `(defun eshell-eval-argument (argument)`
- L997: `(defun eshell-eval-command (command &optional input)`
- L1028: `(defun eshell-resume-command (proc status)`
- L1053: `(defun eshell-resume-eval (command)`
- L1080: `(defmacro eshell-manipulate (form tag &rest body)`
- L1094: `(defun eshell-do-eval (form &optional synchronous-p)`
- L1321: `(defun eshell/which (command &rest names)`
- L1339: `(defun eshell-named-command (command &optional args)`
- L1365: `(defun eshell-find-alias-function (name)`
- L1385: `(defun eshell--find-plain-lisp-command (command)`
- L1394: `(defun eshell-plain-command--which (command)`
- L1403: `(defun eshell-plain-command (command args)`
- L1411: `(defun eshell-exec-lisp (printer errprint func-or-form args form-p)`
- L1499: `(defun eshell/funcall (func &rest args)`
- L1509: `(defun eshell-lisp-command (object &optional args)`
- L1563: `(provide 'esh-cmd)`

## esh-ext.el

- L35: `(require 'esh-io)`
- L36: `(require 'esh-arg)`
- L37: `(require 'esh-opt)`
- L38: `(require 'esh-proc)`
- L39: `(require 'esh-util)`
- L49: `(defcustom eshell-ext-load-hook nil`
- L55: `(defcustom eshell-binary-suffixes exec-suffixes`
- L60: `(defcustom eshell-force-execution`
- L73: `(defun eshell-search-path (name)`
- L93: `(defcustom eshell-windows-shell-file`
- L118: `(defcustom eshell-interpreter-alist`
- L142: `(defcustom eshell-alternate-command-hook nil`
- L155: `(defcustom eshell-command-interpreter-max-length 256`
- L160: `(defcustom eshell-explicit-command-char ?*`
- L167: `(defcustom eshell-explicit-remote-commands t`
- L181: `(defun eshell-ext-initialize ()     ;Called from 'eshell-mode' via intern-soft!`
- L186: `(defun eshell-explicit-command--which (command)`
- L191: `(defun eshell-explicit-command (command args)`
- L206: `(defun eshell-quoted-file-command--which (command)`
- L210: `(defun eshell-quoted-file-command (command args)`
- L220: `(defun eshell-remote-command (command args)`
- L238: `(defun eshell-connection-local-command (command args)`
- L258: `(defun eshell-external-command--which (command)`
- L263: `(defun eshell-external-command (command args)`
- L276: `(defun eshell/addpath (&rest args)`
- L298: `(defun eshell-script-interpreter (file)`
- L326: `(defun eshell-find-interpreter (file args &optional no-examine-p)`
- L383: `(provide 'esh-ext)`

## esh-io.el

- L71: `(require 'esh-arg)`
- L72: `(require 'esh-util)`
- L88: `(defcustom eshell-io-load-hook nil`
- L94: `(defcustom eshell-number-of-handles 3`
- L103: `(defcustom eshell-output-handle 1`
- L108: `(defcustom eshell-error-handle 2`
- L113: `(defcustom eshell-print-queue-size 5`
- L122: `(defcustom eshell-buffered-print-size 2048`
- L132: `(defcustom eshell-buffered-print-redisplay-throttle 0.025`
- L140: `(defcustom eshell-virtual-targets`
- L217: `(defun eshell-io-initialize ()      ;Called from 'eshell-mode' via intern-soft!`
- L227: `(defun eshell-parse-redirection ()`
- L287: `(defun eshell-strip-redirections (terms)`
- L320: `(defun eshell--apply-redirections (cmd)`
- L328: `(defun eshell-create-handles`
- L359: `(defun eshell-duplicate-handles (handles &optional steal-p)`
- L378: `(defun eshell-protect-handles (handles)`
- L385: `(defun eshell-close-handles (&optional exit-code result handles)`
- L405: `(defun eshell-close-handle (handle status)`
- L418: `(defun eshell-set-output-handle (index mode &optional target handles)`
- L440: `(defun eshell-copy-output-handle (index index-to-copy &optional handles)`
- L450: `(defun eshell-set-all-output-handles (mode &optional target handles)`
- L456: `(defun eshell-kill-append (string)`
- L461: `(defun eshell-clipboard-append (string)`
- L467: `(defun eshell-interactive-output-p (&optional index handles)`
- L497: `(defun eshell-init-print-buffer ()`
- L503: `(defun eshell-flush (&optional redisplay-now)`
- L525: `(defun eshell-buffered-print (&rest strings)`
- L536: `(defmacro eshell-with-buffered-print (&rest body)`
- L565: `(defun eshell--output-maybe-n (object handle)`
- L774: `(defun eshell-output-object (object &optional handle-index handles)`
- L784: `(defun eshell-maybe-output-newline (&optional handle-index handles)`
- L797: `(provide 'esh-io)`

## esh-mode.el

- L63: `(require 'esh-arg)`
- L64: `(require 'esh-cmd)`
- L65: `(require 'esh-ext)`
- L66: `(require 'esh-io)`
- L67: `(require 'esh-module)`
- L68: `(require 'esh-proc)`
- L69: `(require 'esh-util)`
- L70: `(require 'esh-var)`
- L79: `(defcustom eshell-mode-unload-hook nil`
- L84: `(defcustom eshell-mode-hook nil`
- L88: `(defcustom eshell-first-time-mode-hook nil`
- L93: `(defcustom eshell-exit-hook nil`
- L99: `(defcustom eshell-kill-on-exit t`
- L104: `(defcustom eshell-input-filter-functions nil`
- L110: `(defcustom eshell-send-direct-to-subprocesses nil`
- L114: `(defcustom eshell-expand-input-functions nil`
- L120: `(defcustom eshell-scroll-to-bottom-on-input nil`
- L130: `(defcustom eshell-scroll-to-bottom-on-output nil`
- L143: `(defcustom eshell-scroll-show-maximum-output t`
- L151: `(defcustom eshell-buffer-maximum-lines 1024`
- L158: `(defcustom eshell-output-filter-functions`
- L169: `(defcustom eshell-preoutput-filter-functions nil`
- L175: `(defcustom eshell-password-prompt-regexp`
- L185: `(defcustom eshell-skip-prompt-function nil`
- L191: `(defcustom eshell-status-in-mode-line t`
- L195: `(defcustom eshell-directory-name`
- L283: `(defvar-keymap eshell-mode-map`
- L289: `(defvar-keymap eshell-command-map`
- L305: `(defvar-keymap eshell-command-repeat-map`
- L313: `(defun eshell-kill-buffer-function ()`
- L325: `(define-derived-mode eshell-mode fundamental-mode "Eshell"`
- L414: `(defun eshell-command-started ()`
- L419: `(defun eshell-command-finished ()`
- L426: `(defun eshell-toggle-direct-send ()`
- L437: `(defun eshell-self-insert-command ()`
- L445: `(defun eshell-intercept-commands ()`
- L466: `(defun eshell-find-tag (&optional tagname next-p regexp-p)`
- L478: `(defun eshell-move-argument (limit func property arg)`
- L496: `(defun eshell-forward-argument (&optional arg)`
- L501: `(defun eshell-backward-argument (&optional arg)`
- L506: `(defun eshell-repeat-argument (&optional arg)`
- L530: `(defun eshell-interactive-print (string)`
- L557: `(defun eshell-parse-command-input (beg end &optional args)`
- L579: `(defun eshell-update-markers (pmark)`
- L585: `(defun eshell-queue-input (&optional use-region)`
- L592: `(defun eshell-send-input (&optional use-region queue-p no-newline)`
- L674: `(defun eshell-send-eof-to-process ()`
- L687: `(defun eshell-interactive-filter (buffer string)`
- L728: `(defun eshell-run-output-filters ()`
- L736: `(defun eshell-preinput-scroll-to-bottom ()`
- L762: `(defun eshell-postoutput-scroll-to-bottom ()`
- L794: `(defun eshell-beginning-of-input ()`
- L798: `(defun eshell-beginning-of-output ()`
- L802: `(defun eshell-end-of-output ()`
- L808: `(defun eshell-delete-output (&optional kill)`
- L825: `(defun eshell-show-output (&optional arg)`
- L840: `(defun eshell-mark-output (&optional arg)`
- L847: `(defun eshell-kill-input ()`
- L856: `(defun eshell-show-maximum-output (&optional interactive)`
- L865: `(defun eshell/clear (&optional scrollback)`
- L875: `(defun eshell/clear-scrollback ()`
- L880: `(defun eshell-get-old-input (&optional use-current-region)`
- L894: `(defun eshell-copy-old-input ()`
- L901: `(defun eshell/exit ()`
- L905: `(defun eshell-life-is-too-much ()`
- L912: `(defun eshell-truncate-buffer ()`
- L936: `(defun eshell-send-invisible ()`
- L948: `(defun eshell-watch-for-password-prompt ()`
- L975: `(defun eshell-handle-control-codes ()`
- L1008: `(defun eshell-handle-ansi-color ()`
- L1022: `(defun eshell-bookmark-name ()`
- L1028: `(defun eshell-bookmark-make-record ()`
- L1035: `(defun eshell-bookmark-jump (bookmark)`
- L1042: `(provide 'esh-mode)`

## esh-module-loaddefs.el

- L224: `(provide 'esh-module-loaddefs)`

## esh-module.el

- L27: `(require 'esh-util)`
- L45: `(defcustom eshell-module-unload-hook`
- L52: `(defcustom eshell-module-loading-messages t`
- L58: `(defcustom eshell-modules-list`
- L113: `(defun eshell-load-modules (modules)`
- L132: `(defun eshell-initialize-modules (modules)`
- L145: `(defun eshell-unload-modules (modules &optional kind)`
- L165: `(defun eshell-unload-extension-modules ()`
- L169: `(provide 'esh-module)`

## esh-opt.el

- L30: `(require 'esh-util)`
- L37: `(defmacro eshell-eval-using-options (name macro-args options &rest body-forms)`
- L125: `(defun eshell--get-option-symbols (options)`
- L133: `(defun eshell--do-opts (name args orig-args options option-syms)`
- L155: `(defun eshell-show-usage (name options)`
- L204: `(defun eshell--split-switch (switch kind)`
- L217: `(defun eshell--set-option (name ai opt value options opt-vals)`
- L240: `(defun eshell--process-option (name switch kind ai options opt-vals)`
- L281: `(defun eshell--process-args (name args options option-syms)`
- L317: `(provide 'esh-opt)`

## esh-proc.el

- L26: `(require 'esh-arg)`
- L27: `(require 'esh-io)`
- L28: `(require 'esh-util)`
- L30: `(require 'pcomplete)`
- L41: `(defcustom eshell-proc-load-hook nil`
- L46: `(defcustom eshell-process-wait-time 0.05`
- L51: `(defcustom eshell-process-wait-seconds 0`
- L57: `(defcustom eshell-process-wait-milliseconds 50`
- L63: `(defcustom eshell-done-messages-in-minibuffer t`
- L67: `(defcustom eshell-delete-exited-processes t`
- L86: `(defcustom eshell-reset-signals`
- L91: `(defcustom eshell-exec-hook nil`
- L100: `(defcustom eshell-kill-hook nil`
- L133: `(defvar-keymap eshell-proc-mode-map`
- L143: `(defun eshell-kill-process-function (proc status)`
- L155: `(define-minor-mode eshell-proc-mode`
- L161: `(defun eshell-proc-initialize ()    ;Called from 'eshell-mode' via intern-soft!`
- L177: `(defun eshell-process-active-p (process)`
- L187: `(defun eshell-wait-for-process (&rest procs)`
- L198: `(defun eshell/jobs ()`
- L204: `(defun eshell/kill (&rest args)`
- L252: `(defun eshell-remove-process-entry (entry)`
- L263: `(defun eshell-record-process-properties (process &optional index)`
- L283: `(defun eshell-gather-process-output (command args)`
- L445: `(defun eshell-interactive-process-filter (process string)`
- L459: `(defun eshell-insertion-filter (proc string)`
- L500: `(defun eshell-sentinel (proc string)`
- L561: `(defun eshell-process-interact (func &optional all query)`
- L583: `(defcustom eshell-kill-process-wait-time 5`
- L587: `(defcustom eshell-kill-process-signals '(SIGINT SIGQUIT SIGKILL)`
- L595: `(defcustom eshell-kill-processes-on-exit nil`
- L617: `(defun eshell-round-robin-kill (&optional query)`
- L631: `(defun eshell-query-kill-processes ()`
- L648: `(defun eshell--reset-after-signal (status)`
- L660: `(defun eshell-interrupt-process ()`
- L666: `(defun eshell-kill-process ()`
- L672: `(defun eshell-quit-process ()`
- L695: `(defun eshell-read-process-name (prompt)`
- L705: `(defun eshell-insert-process (process)`
- L714: `(defun eshell-complete-process-ref ()`
- L718: `(provide 'esh-proc)`

## esh-util.el

- L26: `(require 'seq)`
- L36: `(defcustom eshell-stringify-t t`
- L43: `(defcustom eshell-group-file "/etc/group"`
- L47: `(defcustom eshell-passwd-file "/etc/passwd"`
- L51: `(defcustom eshell-hosts-file "/etc/hosts"`
- L61: `(defcustom eshell-handle-errors t`
- L66: `(defcustom eshell-private-file-modes #o600 ; umask 177`
- L70: `(defcustom eshell-private-directory-modes #o700 ; umask 077`
- L74: `(defcustom eshell-tar-regexp`
- L80: `(defcustom eshell-convert-numeric-arguments t`
- L97: `(defcustom eshell-ange-ls-uids nil`
- L105: `(defcustom eshell-debug-command nil`
- L176: `(defmacro eshell-condition-case (tag form &rest handlers)`
- L186: `(defun eshell-debug-command-start (command)`
- L195: `(defun eshell-always-debug-command (kind string &rest objects)`
- L204: `(defmacro eshell-debug-command (kind string &rest objects)`
- L216: `(defun eshell--mark-as-output (start end &optional object)`
- L224: `(defun eshell--mark-yanked-as-output (start end)`
- L237: `(defun eshell--unmark-string-as-output (string)`
- L251: `(defmacro eshell-with-temp-command (command &rest body)`
- L288: `(defun eshell-find-delimiter`
- L338: `(defun eshell-convertible-to-number-p (string)`
- L346: `(defun eshell-convert-to-number (string)`
- L355: `(defun eshell-convert (string &optional to-string)`
- L401: `(defun eshell-get-path (&optional literal-p)`
- L427: `(defun eshell-set-path (path)`
- L440: `(defun eshell-parse-colon-path (path-env)`
- L451: `(defun eshell-split-filename (filename)`
- L479: `(defun eshell-to-flat-string (value)`
- L491: `(defun eshell-stringify (object)`
- L520: `(defun eshell-regexp-arg (prompt)`
- L532: `(defun eshell-printable-size (filesize &optional human-readable`
- L554: `(defun eshell-winnow-list (entries exclude &optional predicates)`
- L578: `(defun eshell-user-login-name ()`
- L583: `(defun eshell-read-passwd-file (file)`
- L603: `(defun eshell-read-passwd (file result-var timestamp-var)`
- L615: `(defun eshell-read-group-names ()`
- L629: `(defun eshell-read-user-names ()`
- L653: `(defun eshell-subgroups (groupsym)`
- L663: `(defmacro eshell-with-file-modes (modes &rest forms)`
- L668: `(defmacro eshell-with-private-file-modes (&rest forms)`
- L684: `(defun eshell-directory-files-and-attributes (dir &optional full match nosort id-format)`
- L695: `(defun eshell-current-ange-uids ()`
- L712: `(defun eshell-parse-ange-ls (dir)`
- L772: `(defun eshell-file-attributes (file &optional id-format)`
- L797: `(defun eshell-process-list-p (procs)`
- L802: `(defun eshell-make-process-list (procs)`
- L880: `(defun eshell-sublist (l &optional n m)`
- L888: `(provide 'esh-util)`

## esh-var.el

- L113: `(require 'esh-util)`
- L114: `(require 'esh-cmd)`
- L115: `(require 'esh-opt)`
- L116: `(require 'esh-module)`
- L117: `(require 'esh-arg)`
- L118: `(require 'esh-io)`
- L120: `(require 'pcomplete)`
- L121: `(require 'ring)`
- L136: `(defcustom eshell-var-load-hook nil`
- L141: `(defcustom eshell-prefer-lisp-variables nil`
- L145: `(defcustom eshell-complete-export-definition t`
- L149: `(defcustom eshell-modify-global-environment nil`
- L153: `(defcustom eshell-variable-name-regexp "[A-Za-z0-9_-]+"`
- L160: `(defcustom eshell-variable-aliases-list`
- L255: `(defvar-keymap eshell-var-mode-map`
- L274: `(define-minor-mode eshell-var-mode`
- L280: `(defun eshell-var-initialize ()     ;Called from 'eshell-mode' via intern-soft!`
- L309: `(defun eshell-parse-local-variables (args)`
- L335: `(defun eshell-handle-local-variables ()`
- L340: `(defun eshell-interpolate-variable ()`
- L348: `(defun eshell/define (var-alias definition)`
- L374: `(defun eshell/export (&rest sets)`
- L382: `(defun pcomplete/eshell-mode/export ()`
- L389: `(defun eshell/unset (&rest args)`
- L396: `(defun pcomplete/eshell-mode/unset ()`
- L400: `(defun eshell/set (&rest args)`
- L408: `(defun pcomplete/eshell-mode/set ()`
- L412: `(defun eshell/setq (&rest args)`
- L422: `(defun pcomplete/eshell-mode/setq ()`
- L428: `(defun eshell/env (&rest args)`
- L445: `(defun eshell-insert-envvar (envvar-name)`
- L451: `(defun eshell-envvar-names (&optional environment)`
- L462: `(defun eshell-environment-variables ()`
- L474: `(defun eshell-parse-variable ()`
- L504: `(defun eshell-parse-variable-ref (&optional modifier-p)`
- L614: `(defun eshell-parse-indices ()`
- L637: `(defun eshell-parse-index (index)`
- L667: `(defun eshell-eval-indices (indices)`
- L672: `(defun eshell-prepare-indices (indices)`
- L677: `(defun eshell-get-variable (name &optional indices quoted)`
- L715: `(defun eshell-set-variable (name value)`
- L753: `(defun eshell-apply-indices (value indices &optional quoted)`
- L809: `(defun eshell-index-value (value index)`
- L840: `(defun eshell-complete-variable-reference ()`
- L872: `(defun eshell-variables-list ()`
- L880: `(defun eshell-complete-variable-assignment ()`
- L898: `(provide 'esh-var)`

## eshell.el

- L177: `(require 'esh-util)`
- L178: `(require 'esh-module)                   ;For eshell-using-module`
- L179: `(require 'esh-proc)                     ;For eshell-wait-for-process`
- L180: `(require 'esh-io)                       ;For eshell-last-command-status`
- L181: `(require 'esh-cmd)`
- L197: `(defcustom eshell-load-hook nil`
- L202: `(defcustom eshell-unload-hook nil`
- L208: `(defcustom eshell-buffer-name "*eshell*"`
- L226: `(defun eshell (&optional arg)`
- L262: `(defun eshell-command-mode-exit ()`
- L271: `(define-minor-mode eshell-command-mode`
- L275: `(define-key map [(control ?g)] #'abort-recursive-edit)`
- L276: `(define-key map [(control ?m)] #'eshell-command-mode-exit)`
- L277: `(define-key map [(control ?j)] #'eshell-command-mode-exit)`
- L278: `(define-key map [(meta control ?m)] #'eshell-command-mode-exit)`
- L288: `(defun eshell-read-command (&optional prompt)`
- L299: `(defun eshell-command (command &optional to-current-buffer)`
- L355: `(defun eshell-command-result (command &optional status-var)`
- L380: `(defun eshell-unload-function ()`
- L391: `(provide 'eshell)`
