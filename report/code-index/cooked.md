# Indice del codice: cooked

Fonte: https://github.com/vodik/cooked.git

Revisione: `dd8e9fcc3c09d85d9dd598682dbe6390bd138262`.


## lisp/cooked-command-decorations.el

- L43: `(require 'cooked)`
- L44: `(require 'cooked-mode)`
- L45: `(require 'seq)`
- L57: `(defcustom cooked-command-decoration-bitmap 'cooked-command-bar`
- L110: `(defvar cooked-command-decorations--marker-map`
- L112: `(define-key map [mouse-1] #'cooked-command-decorations--click)`
- L113: `(define-key map [left-fringe mouse-1] #'cooked-command-decorations--click)`
- L123: `(defun cooked-command-decorations--anchor (command)`
- L134: `(defun cooked-command-decorations--decoration-at (position command)`
- L174: `(defun cooked-command-decorations--decoration (command)`
- L181: `(defun cooked-command-decorations--place (overlay pos face help &optional keymap)`
- L225: `(defun cooked-command-decorations--paint (command)`
- L278: `(defun cooked-command-decorations--drop-running ()`
- L284: `(defun cooked-command-decorations--sync-running ()`
- L311: `(defun cooked-command-decorations--started (_anchor)`
- L319: `(defun cooked-command-decorations--add (command)`
- L337: `(defun cooked-command-decorations--rearm (_beg _end)`
- L385: `(defun cooked-command-decorations--help (command)`
- L391: `(defun cooked-command-decorations--running-help ()`
- L401: `(defun cooked-command-decorations--clear-live ()`
- L432: `(defun cooked-command-decorations--command-at (position)`
- L447: `(defun cooked-command-decorations--act (command)`
- L468: `(defun cooked-command-decorations-menu ()`
- L481: `(defun cooked-command-decorations--click (event)`
- L489: `(define-key cooked-mode-map (kbd "C-c C-o") #'cooked-command-decorations-menu)`
- L491: `(provide 'cooked-command-decorations)`

## lisp/cooked-command.el

- L24: `(require 'cl-lib)`
- L25: `(require 'seq)`
- L26: `(require 'cooked-util)`
- L63: `(defun cooked--command-start-position (command)`
- L67: `(defun cooked--command-end-position (command)`
- L71: `(defun cooked--command-prompt-position (command)`
- L93: `(defcustom cooked-command-started-functions nil`
- L117: `(defun cooked--running-anchor ()`
- L130: `(defcustom cooked-command-finished-functions nil`
- L152: `(defun cooked--mark-command-end (code end)`
- L179: `(defun cooked-last-exit-code ()`
- L184: `(defun cooked-goto-last-command ()`
- L199: `(defun cooked--command-at (point)`
- L207: `(defun cooked--prompt-starts ()`
- L229: `(defun cooked--command-region (command &optional outer)`
- L248: `(defun cooked--command-around (position)`
- L286: `(defun cooked--goto-nth-command (n direction)`
- L299: `(defun cooked-previous-command (&optional n)`
- L309: `(defun cooked-next-command (&optional n)`
- L315: `(defun cooked--output-region-at-point ()`
- L336: `(defun cooked--command-here (&optional command)`
- L352: `(defun cooked-show-output (&optional command)`
- L377: `(defun cooked-write-output (file &optional outer command)`
- L398: `(defun cooked-copy-command (&optional command)`
- L405: `(defun cooked-copy-output (&optional command)`
- L412: `(provide 'cooked-command)`

## lisp/cooked-completion.el

- L24: `(require 'cooked)`
- L53: `(defun cooked--executable-table ()`
- L63: `(defun cooked-flush-executables ()`
- L68: `(defun cooked--completion-bounds ()`
- L76: `(defun cooked--native-completion ()`
- L107: `(defun cooked-completion-at-point ()`
- L120: `(provide 'cooked-completion)`

## lisp/cooked-deco.el

- L25: `(require 'cooked-util)`
- L26: `(require 'cooked-face)`
- L27: `(require 'cooked-glyph)`
- L34: `(defcustom cooked-inline-images t`
- L48: `(defcustom cooked-box-drawing-images t`
- L102: `(defcustom cooked-box-glyph-run-cache-limit 512`
- L240: `(defun cooked--cell-size (window)`
- L261: `(defun cooked--deco-cell-size ()`
- L293: `(defun cooked--box-glyph-cell (bits size &optional phase)`
- L306: `(defun cooked--box-glyph-bits (bits size &optional phase count)`
- L319: `(defun cooked--box-glyph-ascent (window height)`
- L339: `(defun cooked--box-phase (bits size column row)`
- L359: `(defun cooked--box-glyph-image (bits window size phase &optional count)`
- L385: `(defun cooked--uncolored (image)`
- L412: `(defun cooked--box-glyph-image-1 (bits window size phase count)`
- L456: `(defun cooked--apply-deco (start deco &optional origin row)`
- L519: `(defun cooked--reset-images ()`
- L542: `(defun cooked--image-order-append (id)`
- L553: `(defun cooked--image-order-set (order)`
- L563: `(defun cooked--install-images (images)`
- L591: `(defcustom cooked-image-cache-size (* 64 1024 1024)`
- L650: `(defun cooked--displayed-image-table ()`
- L660: `(defun cooked--evict-images (&optional arriving)`
- L715: `(defun cooked--image-displayed-p (id)`
- L725: `(defun cooked--forget-image (id)`
- L758: `(defun cooked--flush-image-specs (id)`
- L798: `(defun cooked--image-ids-between (beg end)`
- L812: `(defun cooked--release-images (beg end)`
- L821: `(defun cooked--collect-images (ids)`
- L844: `(defun cooked--image-spec (id cells size)`
- L885: `(defun cooked--deco-image (deco size window &optional count)`
- L923: `(defun cooked--deco-display (deco image size)`
- L962: `(defun cooked--deco-display-value (deco size window)`
- L991: `(defun cooked--apply-image-deco (start packed size)`
- L1058: `(defun cooked--apply-glyph-deco (start packed window size origin row)`
- L1112: `(defun cooked--rescale-deco ()`
- L1193: `(defun cooked--rescale-deco-on-zoom (_symbol _newval operation where)`
- L1223: `(defun cooked--flush-deco-cache ()`
- L1233: `(provide 'cooked-deco)`

## lisp/cooked-evil.el

- L52: `;; 'cooked-input-map' included.  A plain '(define-key cooked-input-map ...)'`
- L74: `(require 'cooked-mode)`
- L75: `(require 'cl-lib)`
- L82: `(defcustom cooked-evil-integration t`
- L88: `(defcustom cooked-evil-child-state 'emacs`
- L107: `(defcustom cooked-evil-normal-state-render 'still`
- L124: `(defcustom cooked-evil-visual-state-render 'frozen`
- L136: `(defcustom cooked-evil-hybrid-insert t`
- L144: `(defun cooked-evil-sync ()`
- L166: `(defun cooked-evil--come-back-to (state)`
- L186: `(defun cooked-evil--input-mode ()`
- L209: `(defun cooked-evil--state-changed ()`
- L227: `(defcustom cooked-evil-insert-state-submits t`
- L245: `(defcustom cooked-evil-normal-state-pastes t`
- L272: `(defun cooked-evil-paste ()`
- L291: `(defun cooked-evil-undo (count)`
- L312: `(defun cooked-evil--visual-writable-p ()`
- L326: `(defun cooked-evil-visual-case ()`
- L363: `(defun cooked-evil--goto-input-first-non-blank ()`
- L371: `(defun cooked-evil-insert-line (count &optional vcount)`
- L400: `(defcustom cooked-evil-command-text-object "c"`
- L414: `(defcustom cooked-evil-section-motions t`
- L423: `(defun cooked-evil--command-at-point (outer)`
- L429: `(defun cooked-evil--command-range (count outer)`
- L567: `(provide 'cooked-evil)`

## lisp/cooked-face.el

- L16: `(require 'cooked-util)`
- L30: `(defcustom cooked-color-names`
- L52: `(defun cooked--xterm-256 (index)`
- L64: `(defun cooked--color (spec)`
- L79: `(defun cooked--flush-face-cache (&rest _)`
- L107: `(defun cooked--underline-spec (attrs ul)`
- L207: `(defun cooked--face-key (fgc bgc ulc attrs)`
- L230: `(defun cooked--face-packed (packed i)`
- L283: `(defun cooked--face (fg bg attrs &optional ul)`
- L306: `(defun cooked--face-build (fg bg attrs ul)`
- L331: `(provide 'cooked-face)`

## lisp/cooked-file-link.el

- L48: `(require 'cooked)`
- L49: `(require 'cooked-link)`
- L50: `(require 'ffap)`
- L51: `(require 'compile)`
- L52: `(require 'project)`
- L54: `(defcustom cooked-file-link-highlight t`
- L63: `(defcustom cooked-file-link-scan-limit 400`
- L74: `(defcustom cooked-file-link-display #'find-file-other-window`
- L84: `(defcustom cooked-file-link-error-rules '(gnu gcc-include)`
- L117: `(defun cooked-file-link--split (string)`
- L135: `(defun cooked-file-link--exists (name)`
- L162: `(defun cooked-file-link--at-point ()`
- L174: `(defun cooked-file-link--group (spec)`
- L181: `(defun cooked-file-link--position (name)`
- L210: `(defun cooked-file-link-follow ()`
- L222: `(defun cooked-file-link-scan (beg end)`
- L264: `(provide 'cooked-file-link)`

## lisp/cooked-glyph.el

- L33: `(require 'cl-lib)`
- L69: `(defun cooked--box-block-p (bits)`
- L73: `(defun cooked--box-shade-p (bits)`
- L78: `(defun cooked--box-weight (bits edge)`
- L82: `(defun cooked--box-dashes (bits)`
- L100: `(defun cooked--bitmap-make (width height)`
- L118: `(defun cooked--bitmap-fill (bitmap x0 y0 x1 y1 &optional clear)`
- L145: `(defun cooked--bitmap-extent (bitmap axis)`
- L151: `(defun cooked--bitmap-fill-axis (bitmap axis along0 along1 across0 across1 &optional clear)`
- L158: `(defun cooked--bitmap-set-axis (bitmap axis along across)`
- L164: `(defun cooked--bitmap-stroke (bitmap axis along0 along1 center thickness)`
- L176: `(defun cooked--bitmap-band (bitmap axis along0 along1 &optional clear)`
- L188: `(defun cooked--bitmap-pack (bitmap)`
- L213: `(defun cooked--box-edge-span (bitmap edge cx cy)`
- L225: `(defun cooked--box-draw-edge (bitmap edge weight cx cy light heavy)`
- L240: `(defun cooked--box-draw-arc (bitmap cx cy thickness down-p right-p)`
- L277: `(defun cooked--box-draw-diagonal (bitmap thickness forward backward)`
- L331: `(defun cooked--box-draw-dashes (bitmap axis count)`
- L365: `(defun cooked--box-draw-line (bitmap bits)`
- L410: `(defun cooked--box-draw-shade (bitmap level phase)`
- L436: `(defun cooked--box-draw-quadrant (bitmap mask)`
- L449: `(defun cooked--box-draw-block (bitmap bits phase)`
- L471: `(defun cooked--bitmap-repeat (bitmap count)`
- L505: `(defun cooked--render-box-glyph-cell (bits width height &optional phase)`
- L523: `(defun cooked--pack-box-glyph-cell (bitmap count)`
- L536: `(defun cooked--render-box-glyph (bits width height &optional phase count)`
- L548: `(provide 'cooked-glyph)`

## lisp/cooked-keys.el

- L36: `(require 'cl-lib)`
- L37: `(require 'cooked)`
- L38: `(require 'cooked-util)`
- L39: `(require 'cooked-mouse)`
- L182: `(defun cooked--key-sequence (entry)`
- L199: `(defun cooked--modifier-param (mods)`
- L206: `(defun cooked--app-keypad-p ()`
- L224: `(defun cooked--encode-literal (entry code param mods)`
- L242: `(defun cooked--encode-entry (entry param mods)`
- L280: `(defun cooked--encode-event (event)`
- L317: `(defun cooked-send-key ()`
- L329: `(defun cooked-send-meta-key ()`
- L346: `(defvar cooked-send-string-map`
- L349: `(define-key map (kbd "S-<return>") #'newline)`
- L350: `(define-key map (kbd "M-RET") #'newline)`
- L369: `(defun cooked-send-string (string)`
- L384: `(defcustom cooked-paste-confirm-lines t`
- L398: `(defun cooked--bracketed-paste (text)`
- L408: `(defun cooked--send-paste (text)`
- L427: `(defun cooked-paste ()`
- L476: `(defcustom cooked-key-overrides nil`
- L554: `(defun cooked--foreground-program ()`
- L584: `(defun cooked--update-foreground-label ()`
- L604: `(defun cooked--override-applies-p (condition)`
- L611: `(defun cooked--override-bytes-for (action event)`
- L625: `(defun cooked-send-override ()`
- L634: `(defun cooked--build-override-map ()`
- L649: `(define-key map keys action)`
- L655: `(define-key map keys #'cooked-send-override)))))))`
- L658: `(defun cooked--update-key-overrides ()`
- L678: `(defcustom cooked-key-protocol-overrides '(("\\'claude\\'" . kitty))`
- L719: `(defun cooked--assumed-key-protocol ()`
- L744: `(defun cooked-meta-x ()`
- L772: `(defun cooked--exception-code (key)`
- L784: `(defun cooked--build-passthrough-map (exceptions &optional reserve-meta)`
- L806: `(define-key map [remap self-insert-command] #'cooked-send-key)`
- L811: `(define-key map (vector code) #'cooked-send-key)))`
- L819: `(define-key map (vector (intern (concat prefix (symbol-name (car entry)))))`
- L826: `(define-key map (vector event) #'cooked-mouse-event))`
- L837: `(defun cooked--build-meta-overlay (map)`
- L864: `(define-key esc (vector code) #'cooked-send-meta-key)))`
- L865: `(define-key overlay (vector meta-prefix-char) esc)`
- L866: `(define-key overlay [escape] #'cooked-send-key)`
- L870: `(defun cooked--frame-keymap-type (&optional frame)`
- L891: `(defun cooked--forwarding-map (map)`
- L915: `(defun cooked--replace-keymap (map fresh)`
- L931: `(defun cooked--passthrough-setter (map &optional reserve-meta)`
- L947: `(defcustom cooked-raw-exceptions '("C-g" "C-x" "C-h" "C-u" "C-l")`
- L988: `(defvar cooked-raw-map`
- L992: `(defvar cooked-command-map`
- L1003: `(defvar cooked-alt-map`
- L1014: `(defcustom cooked-semi-exceptions '("C-g" "C-x" "C-h" "C-u" "C-l")`
- L1028: `(defvar cooked-semi-map`
- L1061: `(defvar cooked-peek-map`
- L1063: `(define-key map [remap self-insert-command] #'cooked--peek-resume-and-send)`
- L1064: `(define-key map (kbd "RET") #'cooked--peek-resume-and-send)`
- L1065: `(define-key map (kbd "<return>") #'cooked--peek-resume-and-send)`
- L1079: `(defun cooked-send-literal-key ()`
- L1102: `(defun cooked--build-input-map (delegated)`
- L1111: `(define-key map (kbd "RET") #'cooked-send-input)`
- L1112: `(define-key map (kbd "<S-return>") #'cooked-newline)`
- L1113: `(define-key map (kbd "C-d") #'cooked-delete-char-or-eof)`
- L1114: `(define-key map (kbd "TAB") #'completion-at-point)`
- L1115: `(define-key map (kbd "M-p") #'cooked-previous-input)`
- L1116: `(define-key map (kbd "M-n") #'cooked-next-input)`
- L1121: `(define-key map [remap move-beginning-of-line] #'cooked-beginning-of-line)`
- L1125: `(define-key map (kbd key) #'cooked-delegate-this-key))`
- L1128: `(defvar cooked-input-map`
- L1139: `(defun cooked-delegate-key (key)`
- L1175: `(defun cooked-delegate-this-key ()`
- L1183: `(defcustom cooked-delegate-keys '("C-r")`
- L1209: `(provide 'cooked-keys)`

## lisp/cooked-link.el

- L53: `(require 'seq)`
- L54: `(require 'goto-addr)`
- L55: `(require 'browse-url)`
- L56: `(require 'thingatpt)`
- L64: `(require 'cooked-util)`
- L76: `(defcustom cooked-detect-links t`
- L86: `(defcustom cooked-detect-links-on-alt-screen nil`
- L145: `(defun cooked--install-links (links)`
- L159: `(defun cooked-link-uri (&optional pos)`
- L167: `(defun cooked--link-forwarding-keys-p ()`
- L171: `(defun cooked--open-link-at-point ()`
- L186: `(defun cooked-follow-link (&optional event)`
- L220: `(defun cooked-follow-link-at-point ()`
- L231: `(defvar-keymap cooked-link-map`
- L249: `(defun cooked-link--claimed-p (pos)`
- L272: `(defun cooked-link--propertize (beg end &rest extra)`
- L289: `(defun cooked--link-help-echo (_window object pos)`
- L312: `(defun cooked--render-link-spans (start spans)`
- L342: `(defun cooked--url-scheme-regexp ()`
- L350: `(defun cooked--fontify-links (beg end)`
- L396: `(provide 'cooked-link)`

## lisp/cooked-mode-line.el

- L16: `(require 'cooked)`
- L17: `(require 'cooked-command)`
- L57: `(defcustom cooked-integration-hint t`
- L67: `(defcustom cooked-integration-hint-delay 3`
- L87: `(defun cooked--mode-line-bare (state)`
- L106: `(defun cooked--schedule-integration-hint (buffer)`
- L132: `(defun cooked--mode-line-click (command help)`
- L142: `(defun cooked--mode-line-state ()`
- L164: `(defun cooked--mode-line-subject ()`
- L185: `(defun cooked--mode-line ()`
- L239: `(defcustom cooked-sticky-scroll nil`
- L259: `(defcustom cooked-sticky-scroll-style 'window`
- L282: `(defun cooked--sticky-command (window)`
- L297: `(defun cooked--sticky-label (input width)`
- L308: `(defun cooked--sticky-header ()`
- L344: `(provide 'cooked-mode-line)`

## lisp/cooked-mode.el

- L26: `(require 'cl-lib)`
- L27: `(require 'format-spec)`
- L28: `(require 'seq)`
- L29: `(require 'cooked)`
- L30: `(require 'cooked-osc)`
- L31: `(require 'cooked-render)`
- L32: `(require 'cooked-scrollback)`
- L33: `(require 'cooked-keys)`
- L34: `(require 'cooked-completion)`
- L35: `(require 'cooked-mouse)`
- L36: `(require 'cooked-shell-integration)`
- L37: `(require 'cooked-mode-line)`
- L38: `(require 'cooked-secret)`
- L39: `(require 'comint)`
- L57: `(defcustom cooked-buffer-name "*cooked: %p*"`
- L77: `(defcustom cooked-buffer-name-auto-update nil`
- L88: `(defun cooked--format-buffer-name (dir title host)`
- L95: `(defun cooked--buffer-name (&optional directory)`
- L101: `(defun cooked--buffer-name-shows-title-p ()`
- L113: `(defun cooked--update-buffer-name ()`
- L135: `(defcustom cooked-rejoin-wrapped-lines t`
- L147: `(defun cooked-toggle-rejoin-wrapped-lines ()`
- L174: `(defcustom cooked-shell (or (bound-and-true-p explicit-shell-file-name) shell-file-name)`
- L194: `(defun cooked--track-wandering ()`
- L234: `(defun cooked--snap-to-cursor ()`
- L286: `(defvar cooked-mode-map)                ; 'define-derived-mode' below makes it`
- L288: `(defun cooked--peek-resume-and-send ()`
- L300: `(defun cooked--resume-forwarding ()`
- L323: `(defun cooked-toggle-peek ()`
- L357: `(defun cooked-send-input ()`
- L378: `(defun cooked--send-input-string (text)`
- L418: `(defun cooked-newline ()`
- L454: `(defun cooked--replace-input (text)`
- L464: `(defun cooked--history-record (text)`
- L475: `(defun cooked--history-move (delta)`
- L496: `(defun cooked--history-key (key n)`
- L510: `(defun cooked-previous-input (&optional n)`
- L525: `(defun cooked-next-input (&optional n)`
- L534: `(defun cooked--eof-byte ()`
- L550: `(defun cooked-delete-char-or-eof ()`
- L557: `(defun cooked-send-eof ()`
- L574: `(defun cooked--send-job-control (session key signal)`
- L599: `(defun cooked-suspend ()`
- L607: `(defun cooked-quit ()`
- L620: `(defun cooked-interrupt ()`
- L633: `(defun cooked-kill-session ()`
- L656: `(defun cooked-continue ()`
- L680: `(defun cooked--resample-mode ()`
- L737: `(defun cooked--guard-insertion ()`
- L783: `(defun cooked--set-mode (mode)`
- L792: `(defcustom cooked-state-change-hook nil`
- L838: `(defun cooked--default-input-mode ()`
- L847: `(defun cooked--state-keymap (mode policy)`
- L886: `(defun cooked--refresh-keymap (&optional quiet)`
- L986: `(defun cooked--get-old-input ()`
- L996: `(defun cooked-delete-output ()`
- L1033: `(defun cooked-toggle-fold ()`
- L1068: `(defun cooked-rerun-command (&optional command)`
- L1094: `(defun cooked--sync-size (&optional _frame)`
- L1165: `(defun cooked--session-cell-size ()`
- L1176: `(defun cooked--frame-size-changed (frame)`
- L1190: `(defun cooked--keymap-frame-stale-p (&optional frame)`
- L1201: `(defun cooked--window-selection-changed (frame)`
- L1234: `(defun cooked--user-window ()`
- L1245: `(defun cooked--defer (function)`
- L1257: `(defun cooked--update-attention (&rest _)`
- L1307: `(defun cooked--install-global-hooks ()`
- L1345: `(defun cooked--focused-p ()`
- L1352: `(defun cooked--report-focus ()`
- L1361: `(defun cooked--frame-focus-changed (&rest _)`
- L1369: `(defcustom cooked-kill-buffer-on-exit nil`
- L1386: `(defun cooked--kill-buffer-on-exit-p (code)`
- L1394: `(defun cooked--stop-session ()`
- L1413: `(defun cooked--on-exit (code)`
- L1490: `(defun cooked--imenu-prompt-line (command)`
- L1502: `(defun cooked--imenu-label (command)`
- L1543: `(defun cooked--imenu-index ()`
- L1593: `(defun cooked--outline-heading-list ()`
- L1614: `(defun cooked--outline-headings ()`
- L1623: `(defun cooked--outline-search (&optional bound move backward looking-at)`
- L1665: `(defun cooked--outline-level ()`
- L1670: `(defun cooked--session-in-directory (directory)`
- L1681: `(defun cooked--bookmark-record ()`
- L1717: `(defun cooked-bookmark-jump (bookmark)`
- L1740: `(define-derived-mode cooked-mode comint-mode "cooked"`
- L1900: `(define-key cooked-mode-map (kbd "C-c C-c") #'cooked-interrupt)`
- L1901: `(define-key cooked-mode-map (kbd "C-c C-d") #'cooked-send-eof)`
- L1902: `(define-key cooked-mode-map (kbd "C-c C-e") #'cooked-send-string)`
- L1903: `(define-key cooked-mode-map (kbd "C-c M-x") #'cooked-meta-x)`
- L1904: `(define-key cooked-mode-map (kbd "C-c C-z") #'cooked-suspend)`
- L1905: `(define-key cooked-mode-map (kbd "C-c C-y") #'cooked-paste)`
- L1906: `(define-key cooked-mode-map (kbd "C-c C-q") #'cooked-send-literal-key)`
- L1907: `(define-key cooked-mode-map (kbd "C-c C-v") #'cooked-toggle-peek)`
- L1908: `(define-key cooked-mode-map (kbd "C-c C-p") #'cooked-previous-command)`
- L1909: `(define-key cooked-mode-map (kbd "C-c C-n") #'cooked-next-command)`
- L1910: `(define-key cooked-mode-map (kbd "C-c TAB") #'cooked-toggle-fold)`
- L1911: `(define-key cooked-mode-map (kbd "C-c C-l") #'cooked-refresh)`
- L1917: `(define-key cooked-mode-map (kbd "C-c C->") #'cooked-goto-last-command)`
- L1923: `(define-key cooked-mode-map (kbd "C-c RET") #'cooked-follow-link-at-point)`
- L1930: `(define-key cooked-mode-map (kbd "C-c C-\\") #'cooked-quit)`
- L1931: `(define-key cooked-mode-map (kbd "C-c M-o") #'cooked-clear-scrollback)`
- L1932: `(define-key cooked-mode-map (kbd "C-c SPC") #'cooked-newline)`
- L1952: `(define-key cooked-mode-map [mouse-2] #'cooked-paste)`
- L1999: `(define-key cooked-mode-map (vector 'remap (car remap)) (cdr remap)))`
- L2034: `(define-key cooked-mode-map [menu-bar inout] nil)`
- L2035: `(define-key cooked-mode-map [menu-bar signals] nil)`
- L2036: `(define-key cooked-mode-map [menu-bar completion] nil)`
- L2193: `(defun cooked--context-menu (menu click)`
- L2233: `(defun cooked-kill-input ()`
- L2239: `(defcustom cooked-beginning-of-line-skips-prompt t`
- L2264: `(defun cooked--input-line-start ()`
- L2279: `(defun cooked-beginning-of-line (&optional n)`
- L2303: `(defun cooked--cleanup ()`
- L2313: `(defun cooked--kill-emacs ()`
- L2339: `(defun cooked--live-buffers ()`
- L2346: `(defun cooked--display (buffer action)`
- L2356: `(defun cooked--start-session (&optional command)`
- L2368: `(provide 'cooked-mode)`

## lisp/cooked-module.el

- L24: `(require 'cooked-util)`
- L29: `(defcustom cooked-term-name "cooked-256color"`
- L45: `(defun cooked--terminfo-source ()`
- L49: `(defun cooked--terminfo-entry (database name)`
- L59: `(defun cooked--terminfo-usable-p (database name)`
- L73: `(defun cooked--terminfo-install (&optional database)`
- L92: `(defun cooked--terminfo-database ()`
- L117: `(defun cooked--terminfo ()`
- L126: `(defun cooked-version ()`
- L140: `(defun cooked-install-terminfo ()`
- L157: `(defun cooked-install-terminfo-remote (host)`
- L173: `(defcustom cooked-native-module nil`
- L180: `(defun cooked--module-stale-p (built root)`
- L210: `(defun cooked--build-module (root built)`
- L264: `(defun cooked--check-core-drift (built)`
- L293: `(defun cooked--load-module ()`
- L314: `(provide 'cooked-module)`

## lisp/cooked-mouse.el

- L31: `(require 'cl-lib)`
- L32: `(require 'cooked)`
- L33: `(require 'cooked-util)`
- L98: `(define-key map (vector event) #'cooked-mouse-event))`
- L129: `(define-key map (vector event) #'cooked-mouse-event))`
- L190: `(defun cooked--set-mouse-state (enabled sgr drag motion)`
- L225: `(defvar cooked--mouse-map-alist`
- L248: `(defcustom cooked-alternate-scroll-lines 3`
- L254: `(defun cooked--alt-scroll-active-p ()`
- L261: `(defun cooked--update-mouse-grab ()`
- L282: `(defun cooked--mouse-cell (posn)`
- L299: `(defun cooked--mouse-report (button row col pressed)`
- L312: `(defun cooked--send-mouse (button row col pressed)`
- L333: `(defun cooked--report-button (button row col pressed)`
- L341: `(defun cooked--report-motion (row col)`
- L354: `(defun cooked--mouse-track (window)`
- L386: `(defun cooked--alt-scroll-keys (button)`
- L397: `(defun cooked--mouse-buffer (window)`
- L402: `(defun cooked-mouse-event ()`
- L502: `(defun cooked--mouse-fallback (event)`
- L535: `(provide 'cooked-mouse)`

## lisp/cooked-next-error.el

- L41: `(require 'cooked)`
- L42: `(require 'compile)`
- L43: `(require 'cl-lib)`
- L56: `(defun cooked-next-error--command ()`
- L78: `(defun cooked-next-error--safe-region (command)`
- L101: `(defun cooked-next-error--parse-region (start end)`
- L131: `(defun cooked-next-error--key (loc)`
- L140: `(defun cooked-next-error--locate (matches key)`
- L149: `(defun cooked-next-error--visit (position message)`
- L159: `(defun cooked-next-error-function (n reset)`
- L182: `(defun cooked-next-error--setup ()`
- L188: `(provide 'cooked-next-error)`

## lisp/cooked-osc-eval.el

- L43: `(require 'cooked)`
- L45: `(require 'cooked-scrollback)`
- L56: `(defun cooked-osc-eval-visit-file (name)`
- L61: `(defun cooked-osc-eval-visit-file-other-window (name)`
- L66: `(defun cooked-osc-eval-dired (name)`
- L71: `(defcustom cooked-eval-commands nil`
- L102: `(defun cooked-osc-eval-named (payload)`
- L117: `(defun cooked-osc-eval-request (payload)`
- L147: `(provide 'cooked-osc-eval)`

## lisp/cooked-osc.el

- L26: `(require 'cooked)`
- L27: `(require 'url-util)`
- L73: `(defun cooked--handle-osc (code bell parts)`
- L94: `(defun cooked--osc-title (parts)`
- L98: `(defun cooked--set-title (title)`
- L111: `(defun cooked--handle-title-stack (push)`
- L124: `(defun cooked--osc-cwd (parts)`
- L136: `(defcustom cooked-allow-color-set nil`
- L146: `(defcustom cooked-allow-notifications nil`
- L156: `(defcustom cooked-notification-rate '(3 . 10)`
- L180: `(defun cooked--notification-clean (text limit)`
- L186: `(defun cooked--notification-allowed-p ()`
- L196: `(defun cooked--notify (title body)`
- L211: `(defun cooked--osc-99-metadata (meta)`
- L223: `(defun cooked--osc-notify (parts)`
- L251: `(defun cooked--osc-notify-777 (parts)`
- L264: `(defun cooked--default-color (kind)`
- L285: `(defun cooked--color-scheme ()`
- L302: `(defun cooked--sync-color-scheme ()`
- L318: `(defun cooked--color-to-osc (color)`
- L324: `(defun cooked--parse-osc-color (spec)`
- L341: `(defun cooked--osc-color (parts)`
- L359: `(defun cooked--set-default-color (kind spec)`
- L381: `(defun cooked--reset-default-color (kind)`
- L388: `(defun cooked--osc-color-reset (_parts)`
- L455: `(defun cooked--osc-announce (payload)`
- L478: `(defun cooked--osc-emacs (parts)`
- L517: `(defcustom cooked-clipboard-write t`
- L524: `(defcustom cooked-clipboard-max-size 100000`
- L531: `(defun cooked--osc-clipboard (parts)`
- L543: `(defun cooked--set-directory (url)`
- L582: `(provide 'cooked-osc)`

## lisp/cooked-process.el

- L125: `(require 'cl-lib)`
- L126: `(require 'cooked)`
- L140: `(defcustom cooked-process-rows 8`
- L149: `(defcustom cooked-process-columns 120`
- L166: `(defcustom cooked-process-styled t`
- L181: `(defcustom cooked-process-live-tail t`
- L243: `(defun cooked-process--environment ()`
- L251: `(defun cooked-process--size (buffer)`
- L259: `(defun cooked-process-start (name buffer argv &optional directory)`
- L310: `(defun cooked-process-start-shell-command (name buffer command)`
- L321: `(defun cooked-process--text (block)`
- L375: `(defun cooked-process--emit (text)`
- L389: `(defun cooked-process--remember-rows (rows height)`
- L408: `(defun cooked-process--tail-text ()`
- L418: `(defun cooked-process--refresh-tail (host)`
- L453: `(defun cooked-process--drop-tail ()`
- L469: `(defun cooked-process--pump (host)`
- L493: `(defun cooked-process--residue (host)`
- L525: `(defun cooked-process--finish (host exit)`
- L542: `(defun cooked-process--report (host exit)`
- L576: `(defun cooked-process-reap (host)`
- L608: `(defun cooked-process--buffer-killed ()`
- L612: `(defun cooked-process-interrupt (buffer)`
- L623: `(defun cooked-process-send-string (buffer string)`
- L639: `(defcustom cooked-process-commands nil`
- L648: `(defcustom cooked-process-excluded-modes '(grep-mode)`
- L661: `(defun cooked-process--wanted-p (command)`
- L666: `(defun cooked-process--around-compilation-start (fn command &rest args)`
- L702: `(defun cooked-process--around-kill-compilation (fn &rest args)`
- L711: `(define-minor-mode cooked-process-mode`
- L733: `(provide 'cooked-process)`

## lisp/cooked-project.el

- L28: `(require 'project)`
- L29: `(require 'cooked)`
- L39: `(defun cooked-project--session (root new display-action)`
- L49: `(defun cooked-project--here-root ()`
- L56: `(defun cooked-project (&optional new)`
- L68: `(defun cooked-project-other-window (&optional new)`
- L77: `(defun cooked-here (&optional new)`
- L88: `(defun cooked-here-other-window (&optional new)`
- L111: `;;   (keymap-set project-prefix-map "t" #'cooked-project)`
- L144: `(provide 'cooked-project)`

## lisp/cooked-render.el

- L49: `(require 'cl-lib)`
- L50: `(require 'seq)`
- L51: `(require 'cooked)`
- L52: `(require 'cooked-util)`
- L53: `(require 'cooked-deco)`
- L54: `(require 'cooked-link)`
- L55: `(require 'cooked-mouse)`
- L56: `(require 'cooked-osc)`
- L57: `(require 'cooked-scrollback)`
- L109: `(defun cooked--schedule-repaint ()`
- L116: `(defun cooked--flush-pending-repaint ()`
- L134: `(defun cooked--drain-and-apply ()`
- L209: `(defun cooked--on-wake (buffer)`
- L250: `(defcustom cooked-clear-selection-on-output t`
- L270: `(defun cooked--following-windows ()`
- L291: `(defun cooked--install-resources (update)`
- L347: `(defun cooked--capture-viewport ()`
- L361: `(defun cooked--apply-levels (update)`
- L374: `(defun cooked--place-point (viewport)`
- L396: `(defun cooked--scroll-windows (viewport)`
- L419: `(defun cooked--pin-alt-screen (windows)`
- L437: `(defun cooked--pin-transcript-bottom (windows &optional pos bottom)`
- L491: `(defun cooked--scroll-transcript (viewport here others)`
- L516: `(defun cooked--apply (update)`
- L598: `(defun cooked--handle-event (event batch-start)`
- L632: `(defun cooked-refresh ()`
- L663: `(provide 'cooked-render)`

## lisp/cooked-scrollback.el

- L40: `(require 'seq)`
- L41: `(require 'cooked)`
- L42: `(require 'cooked-util)`
- L43: `(require 'cooked-command)`
- L44: `(require 'cooked-deco)`
- L60: `(defcustom cooked-scrollback-lines 10000`
- L93: `(defun cooked--split-seam ()`
- L140: `(defun cooked--trim-scrollback ()`
- L185: `(defun cooked--discard-scrollback (end)`
- L228: `(defun cooked--discard-scrollback-region (beg end)`
- L258: `(defun cooked-clear-scrollback ()`
- L286: `(provide 'cooked-scrollback)`

## lisp/cooked-secret.el

- L18: `(require 'cooked)`
- L23: `(defcustom cooked-password-function nil`
- L29: `(defcustom cooked-secret-debounce 0.03`
- L46: `(defun cooked--schedule-secret ()`
- L75: `(defun cooked--resume-secret ()`
- L92: `(defun cooked--cancel-secret ()`
- L117: `(defun cooked--dismiss-secret (minibuffer)`
- L124: `(defvar cooked-secret-map`
- L126: `(define-key map (kbd "C-c C-c") #'cooked-secret-abort)`
- L137: `(defun cooked-secret-abort ()`
- L146: `(defun cooked--read-passwd (prompt)`
- L164: `(defun cooked--prompt-secret (buffer)`
- L209: `(provide 'cooked-secret)`

## lisp/cooked-shell-completion.el

- L59: `(require 'cooked)`
- L60: `(require 'cooked-completion)`
- L61: `(require 'cl-lib)`
- L62: `(require 'seq)`
- L66: `(defcustom cooked-completion-backend 'shell`
- L86: `(defcustom cooked-completion-timeout 0.4`
- L128: `(defun cooked--completion-encode (string)`
- L134: `(defun cooked--completion-candidates (blob)`
- L143: `(defun cooked--completion-handle (payload)`
- L166: `(defun cooked--shell-completions (line point)`
- L206: `(defun cooked--completion-annotation (display match)`
- L219: `(defun cooked--completion-group (group)`
- L236: `(defun cooked--completion-index (records extra annotations groups)`
- L262: `(defun cooked--completion-settled-p (word cached-word cached-matches)`
- L279: `(defun cooked--completion-dynamic (head tail annotations groups seed)`
- L330: `(defun cooked--shell-completion-at-point (region)`
- L400: `(provide 'cooked-shell-completion)`

## lisp/cooked-shell-integration.el

- L19: `(require 'cooked-util)`
- L20: `(require 'cooked-completion)`
- L22: `(defcustom cooked-shell-integration 'detect`
- L64: `(defcustom cooked-shell-integration-features`
- L113: `(defun cooked--integration-shell (shell)`
- L131: `(defun cooked--integration-feature-p (feature)`
- L135: `(defun cooked--integration-environment ()`
- L150: `(defun cooked--integration-directory ()`
- L158: `(defun cooked--scratch-directory ()`
- L162: `(defun cooked--remove-scratch ()`
- L175: `(defun cooked--zsh-source-user (file)`
- L184: `(defun cooked--write-zsh-startup (scratch integration capture-p)`
- L220: `(defun cooked--shell-invocation (shell)`
- L271: `(provide 'cooked-shell-integration)`

## lisp/cooked-util.el

- L17: `(require 'cl-lib)`
- L36: `(defun cooked-session-p (object)`
- L45: `(defmacro cooked--dolist-buffers (&rest body)`
- L69: `(defmacro cooked--protect-hook (&rest body)`
- L102: `(defmacro cooked--protect-seam (key &rest body)`
- L132: `(defun cooked--seam-failed (key err)`
- L155: `(defun cooked--seam-notify (fn &rest args)`
- L160: `(defun cooked--seam-answer (fn &rest args)`
- L165: `(defun cooked--run-seam (seam &rest args)`
- L181: `(defun cooked--run-seam-until-success (seam &rest args)`
- L196: `(defmacro cooked--dolist-windows (var windows &rest body)`
- L235: `(defmacro cooked--cached (table key &rest body)`
- L256: `(defmacro cooked--cached-bounded (table limit key &rest body)`
- L279: `(defmacro cooked--with-child-edit (&rest body)`
- L307: `(defun cooked--live-session ()`
- L316: `(defun cooked--require-session ()`
- L325: `(defun cooked--send-to-child (bytes)`
- L329: `(defun cooked--send-if-live (bytes)`
- L351: `(defun cooked--root ()`
- L370: `(defun cooked--local-name (name)`
- L394: `(provide 'cooked-util)`

## lisp/cooked.el

- L55: `(require 'cl-lib)`
- L56: `(require 'jit-lock)`
- L57: `(require 'comint)`
- L58: `(require 'face-remap)`
- L59: `(require 'cooked-util)`
- L60: `(require 'cooked-module)`
- L61: `(require 'cooked-command)`
- L62: `(require 'cooked-face)`
- L63: `(require 'cooked-deco)`
- L64: `(require 'cooked-link)`
- L107: `(defun cooked--cursor-decode (spec)`
- L113: `(defun cooked--cursor-cell ()`
- L141: `(defun cooked--screen-start-position ()`
- L206: `(defun cooked--suspended-p ()`
- L236: `(defun cooked--frozen-p ()`
- L247: `(defun cooked--follow-p ()`
- L310: `(defun cooked--foreign-host-p ()`
- L333: `(defun cooked--csi (final &rest params)`
- L361: `(defun cooked--csi-private (prefix final &rest params)`
- L380: `(defun cooked--ss3 (final)`
- L394: `(defun cooked--cursor-key (final)`
- L421: `(defun cooked--render-block (block &optional row)`
- L586: `(defun cooked--policy ()`
- L632: `(defun cooked--ownership-license ()`
- L666: `(defun cooked--secret-p ()`
- L672: `(defun cooked--input-state-p ()`
- L676: `(defun cooked--child-owns-keyboard-p ()`
- L686: `(defun cooked--input-mark ()`
- L703: `(defun cooked--set-input-mark (position)`
- L708: `(defun cooked--clear-input-region ()`
- L713: `(defun cooked--input-region ()`
- L726: `(defun cooked--check-undo-anchor ()`
- L757: `(defun cooked--discard-undo ()`
- L791: `(defun cooked--input-start-position ()`
- L795: `(defun cooked--pending-input ()`
- L829: `(defun cooked--snap-to-input ()`
- L849: `(defun cooked--take-pending-input ()`
- L856: `(defun cooked--restore-pending-input (text)`
- L882: `(defun cooked--point-after-input ()`
- L887: `(defun cooked--register-mark (id at batch-start)`
- L901: `(defun cooked--relocate-marks (marks batch-start)`
- L927: `(defun cooked--prune-marks ()`
- L947: `(defun cooked--handle-semantic (event batch-start)`
- L1058: `(defun cooked--goto-screen-row (index &optional extend)`
- L1087: `(defun cooked--pad-to-cursor ()`
- L1122: `(defun cooked--render-scrolled (block)`
- L1171: `(defcustom cooked-cursor-shapes`
- L1182: `(defun cooked--cursor-type ()`
- L1230: `(defun cooked--restore-point (window)`
- L1249: `(defun cooked--sync-cursor-type ()`
- L1284: `(defun cooked--ghost-cursor-visible-p ()`
- L1304: `(defun cooked--update-ghost-cursor ()`
- L1332: `(defcustom cooked-alt-change-hook nil`
- L1350: `(defun cooked--set-alt (on)`
- L1370: `(defun cooked--sync-fontification ()`
- L1400: `(defun cooked--apply-alt-pin ()`
- L1422: `(defun cooked--screen-restricted-p ()`
- L1433: `(defun cooked--release-alt-pin ()`
- L1439: `(defun cooked--pin-alt-windows ()`
- L1483: `(defun cooked--fit-screen ()`
- L1532: `(defun cooked--check-seam ()`
- L1566: `(defun cooked--protect (limit)`
- L1629: `(defcustom cooked-wrap-cache-limit 4096`
- L1683: `(defun cooked--layout-stamp (window)`
- L1738: `(defun cooked--string-pixel-width (string)`
- L1752: `(defun cooked--ascii-fixed-pitch-p (window)`
- L1800: `(defun cooked--wrap-cache (window)`
- L1815: `(defun cooked--row-mismeasured-p (width uniform fixed-pitch)`
- L1853: `(defun cooked--row-wraps-p (start end window memo)`
- L1894: `(defun cooked--trim-to-one-line (start window)`
- L1917: `(defun cooked--guard-row-width (start width &optional window uniform cache)`
- L1997: `(defcustom cooked-truncation-bitmap nil`
- L2008: `(defun cooked--mark-truncation (start cut window)`
- L2047: `(defun cooked--truncation-bitmap ()`
- L2059: `(defun cooked--truncation-glyph ()`
- L2096: `(defun cooked--render-rows (rows &optional alt)`
- L2203: `(defun cooked--notify-rows-rendered (bounds)`
- L2217: `(defun cooked--fontify-region (beg end)`
- L2266: `(defun cooked--cursor-position ()`
- L2274: `(defun cooked--anchor-position (anchor batch-start)`
- L2304: `(defun cooked--screen-cell (&optional pos)`
- L2326: `(defun cooked--goto-screen-cell (cell)`
- L2331: `(defun cooked--at-child-cursor-p ()`
- L2345: `(defun cooked--window-size ()`
- L2368: `(defun cooked--window-rows (window)`
- L2379: `(defun cooked--layout-window ()`
- L2412: `(defun cooked--set-tuning-option (symbol value)`
- L2448: `(defcustom cooked-min-redisplay-interval 0.008`
- L2489: `(defcustom cooked-backlog-limit 8000`
- L2513: `(defcustom cooked-confirm-kill 'auto`
- L2557: `(defun cooked--query-on-kill-p ()`
- L2565: `(defun cooked--sync-query-flag ()`
- L2575: `(defun cooked--start (argv &optional directory extra-env)`
- L2667: `(defun cooked--child-environment (&optional extra)`
- L2744: `(defun cooked--deactivate-mark ()`
- L2786: `(defcustom cooked-display-action '((display-buffer-same-window`
- L2829: `(defun cooked--open-session (new command action)`
- L2841: `(defun cooked (&optional new command)`
- L2850: `(defun cooked-other-window (&optional new command)`
- L2857: `(provide 'cooked)`
