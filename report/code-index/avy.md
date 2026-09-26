# Indice del codice: avy

Fonte: https://github.com/abo-abo/avy.git

Revisione: `933d1f36cca0f71e4acb5fac707e9ae26c536264`.


## .dir-locals.el


## avy-test.el

- L27: `(require 'ert)`
- L28: `(require 'avy)`
- L70: `(provide 'avy-test)`

## avy.el

- L57: `(require 'cl-lib)`
- L58: `(require 'ring)`
- L66: `(defcustom avy-keys '(?a ?s ?d ?f ?g ?h ?j ?k ?l)`
- L101: `(defcustom avy-keys-alist nil`
- L107: `(defcustom avy-orders-alist '((avy-goto-char . avy-order-closest))`
- L114: `(defcustom avy-words`
- L147: `(defcustom avy-style 'at-full`
- L158: `(defcustom avy-styles-alist nil`
- L188: `(defcustom avy-dispatch-alist`
- L212: `(defcustom avy-background nil`
- L216: `(defcustom avy-all-windows t`
- L224: `(defcustom avy-case-fold-search t`
- L228: `(defcustom avy-word-punc-regexp "[!-/:-@[-'{-~]"`
- L235: `(defcustom avy-goto-word-0-regexp "\\b\\sw"`
- L243: `(defcustom avy-ignored-modes '(image-mode doc-view-mode pdf-view-mode)`
- L248: `(defcustom avy-single-candidate-jump t`
- L252: `(defcustom avy-del-last-char-by '(?\b ?\d)`
- L258: `(defcustom avy-escape-chars '(?\e ?\C-g)`
- L314: `(defmacro avy-multipop (lst n)`
- L324: `(defun avy--de-bruijn (keys n)`
- L345: `(defun avy--path-alist-1 (lst seq-len keys)`
- L390: `(defun avy-order-closest (x)`
- L400: `(defun avy-tree (lst keys)`
- L426: `(defun avy-subdiv (n b)`
- L440: `(defun avy-traverse (tree walker &optional recur-key)`
- L461: `(defun avy-handler-default (char)`
- L480: `(defun avy-show-dispatch-help ()`
- L499: `(defun avy-mouse-event-window (char)`
- L509: `(defun avy-read (tree display-fn cleanup-fn)`
- L543: `(defun avy-read-de-bruijn (lst keys)`
- L578: `(defun avy-read-words (lst words)`
- L629: `(defun avy-window-list ()`
- L643: `(defcustom avy-all-windows-alt nil`
- L650: `(defmacro avy-dowindows (flip &rest body)`
- L662: `(defun avy-resume ()`
- L667: `(defmacro avy-with (command &rest body)`
- L686: `(defun avy-action-goto (pt)`
- L694: `(defun avy-forward-item ()`
- L700: `(defun avy-action-mark (pt)`
- L706: `(defun avy-action-copy (pt)`
- L721: `(defun avy-action-yank (pt)`
- L727: `(defun avy-action-yank-line (pt)`
- L732: `(defun avy-action-kill-move (pt)`
- L740: `(defun avy-action-kill-stay (pt)`
- L753: `(defun avy-action-zap-to-char (pt)`
- L759: `(defun avy-action-teleport (pt)`
- L771: `(defcustom avy-flyspell-correct-function #'flyspell-correct-word-before-point`
- L776: `(defun avy-action-ispell (pt)`
- L798: `(defun avy-pre-action-default (res)`
- L808: `(defun avy--process-1 (candidates overlay-fn &optional cleanup-fn)`
- L834: `(defun avy--last-candidates-cycle (advancer)`
- L849: `(defun avy-prev ()`
- L858: `(defun avy-next ()`
- L868: `(defun avy-process (candidates &optional overlay-fn cleanup-fn)`
- L911: `(defun avy--make-backgrounds (wnd-list)`
- L925: `(defun avy--done ()`
- L931: `(defun avy--visible-p (s)`
- L937: `(defun avy--next-visible-point ()`
- L944: `(defun avy--next-invisible-point ()`
- L951: `(defun avy--find-visible-regions (rbeg rend)`
- L967: `(defun avy--regex-candidates (regex &optional beg end pred group)`
- L1000: `(defun avy--remove-leading-chars ()`
- L1005: `(defun avy--old-str (pt wnd)`
- L1013: `(defun avy--overlay (str beg end wnd &optional compose-fn)`
- L1045: `(defcustom avy-highlight-first nil`
- L1050: `(defun avy--key-to-char (c)`
- L1058: `(defun avy-candidate-beg (leaf)`
- L1067: `(defun avy-candidate-end (leaf)`
- L1076: `(defun avy-candidate-wnd (leaf)`
- L1082: `(defun avy--overlay-pre (path leaf)`
- L1103: `(defun avy--overlay-at (path leaf)`
- L1124: `(defun avy--overlay-at-full (path leaf)`
- L1195: `(defun avy--overlay-post (path leaf)`
- L1213: `(defun avy--update-offset-and-str (offset str lep)`
- L1254: `(defun avy--style-fn (style)`
- L1266: `(cl-defun avy-jump (regex &key window-flip beg end action pred group)`
- L1283: `(defun avy--generic-jump (regex window-flip &optional beg end)`
- L1298: `(defun avy-goto-char (char &optional arg)`
- L1311: `(defun avy-goto-char-in-line (char)`
- L1321: `(defun avy-goto-char-2 (char1 char2 &optional arg beg end)`
- L1354: `(defun avy-goto-char-2-above (char1 char2 &optional arg)`
- L1369: `(defun avy-goto-char-2-below (char1 char2 &optional arg)`
- L1384: `(defun avy-isearch ()`
- L1398: `(defun avy-goto-word-0 (arg &optional beg end)`
- L1411: `(defun avy-goto-whitespace-end (arg &optional beg end)`
- L1424: `(defun avy-goto-word-0-above (arg)`
- L1432: `(defun avy-goto-word-0-below (arg)`
- L1440: `(defun avy-goto-whitespace-end-above (arg)`
- L1448: `(defun avy-goto-whitespace-end-below (arg)`
- L1457: `(defun avy-goto-word-1 (char &optional arg beg end symbol)`
- L1484: `(defun avy-goto-word-1-above (char &optional arg)`
- L1496: `(defun avy-goto-word-1-below (char &optional arg)`
- L1508: `(defun avy-goto-symbol-1 (char &optional arg)`
- L1518: `(defun avy-goto-symbol-1-above (char &optional arg)`
- L1530: `(defun avy-goto-symbol-1-below (char &optional arg)`
- L1544: `(defcustom avy-subword-extra-word-chars '(?{ ?= ?} ?* ?: ?> ?<)`
- L1550: `(defun avy-goto-subword-0 (&optional arg predicate beg end)`
- L1592: `(defun avy-goto-subword-1 (char &optional arg)`
- L1606: `(defun avy-goto-word-or-subword-1 ()`
- L1616: `(defcustom avy-indent-line-overlay nil`
- L1621: `(defun avy--line-cands (&optional arg beg end bottom-up)`
- L1652: `(defun avy--linum-strings ()`
- L1673: `(define-minor-mode avy-linum-mode`
- L1684: `(defun avy--linum-update-window (_ win)`
- L1736: `(defun avy--line (&optional arg beg end bottom-up)`
- L1752: `(defun avy-goto-line (&optional arg)`
- L1789: `(defun avy-goto-line-above (&optional offset bottom-up)`
- L1805: `(defun avy-goto-line-below (&optional offset bottom-up)`
- L1821: `(defcustom avy-line-insert-style 'above`
- L1828: `(defun avy-goto-end-of-line (&optional arg)`
- L1835: `(defun avy-copy-line (arg)`
- L1861: `(defun avy-move-line (arg)`
- L1886: `(defun avy-copy-region (arg)`
- L1916: `(defun avy-move-region ()`
- L1936: `(defun avy-kill-region (arg)`
- L1970: `(defun avy-kill-ring-save-region (arg)`
- L2000: `(defun avy-kill-whole-line (arg)`
- L2025: `(defun avy-kill-ring-save-whole-line (arg)`
- L2050: `(defun avy-setup-default ()`
- L2053: `'(define-key isearch-mode-map (kbd "C-'") 'avy-isearch)))`
- L2055: `(defcustom avy-timeout-seconds 0.5`
- L2059: `(defcustom avy-enter-times-out t`
- L2066: `(defun avy--read-candidates (&optional re-builder)`
- L2153: `(defun avy-goto-char-timer (&optional arg)`
- L2164: `(defun avy-push-mark ()`
- L2172: `(defun avy-pop-mark ()`
- L2191: `(defun avy-transpose-lines-in-region ()`
- L2214: `(defun avy-org-refile-as-child ()`
- L2235: `(defun avy-org-goto-heading-timer (&optional arg)`
- L2249: `(provide 'avy)`

## targets/avy-init.el

- L24: `(require 'avy)`
- L25: `(global-set-key (kbd "C-c j") 'avy-goto-char)`
- L26: `(global-set-key (kbd "C-'") 'avy-goto-char-2)`

## targets/checkdoc.el

