# Indice del codice: wterm

Fonte: https://github.com/admmq/wterm.el.git

Revisione: `08a78cc300f3d39432e53f15bbc558ceacec35a8`.


## wterm.el

- L28: `(require 'subr-x)`
- L29: `(require 'ansi-color)`
- L30: `(require 'url-util)`
- L40: `(defcustom wterm-shell`
- L45: `(defcustom wterm-conpty-program`
- L50: `(defcustom wterm-max-scrollback 10000`
- L54: `(defcustom wterm-timer-delay 0.01`
- L60: `(defcustom wterm-buffer-name "*wterm*"`
- L64: `(defcustom wterm-buffer-name-string nil`
- L69: `(defcustom wterm-kill-buffer-on-exit t`
- L73: `(defcustom wterm-environment`
- L78: `(defcustom wterm-track-directory t`
- L84: `(defcustom wterm-bell t`
- L88: `(defcustom wterm-keymap-exceptions`
- L129: `(defun wterm--special-keys ()`
- L138: `(defvar wterm-mode-map`
- L140: `(define-key map [remap self-insert-command] #'wterm--self-insert)`
- L142: `(define-key map (kbd key) #'wterm--self-insert))`
- L148: `(define-key map (kbd key) #'wterm--self-insert)))))`
- L152: `(define-key map (kbd key) #'wterm--self-insert))))`
- L153: `(define-key map (kbd "C-_") #'wterm--self-insert)`
- L154: `(define-key map (kbd "C-/") #'wterm--self-insert)`
- L155: `(define-key map (kbd "M-DEL") #'wterm--self-insert)`
- L160: `(define-key map (vector (event-convert-list (append mods (list k))))`
- L163: `(define-key map (kbd "C-c C-c") #'wterm-send-C-c)`
- L164: `(define-key map (kbd "C-c C-z") #'wterm-send-C-z)`
- L165: `(define-key map (kbd "C-c C-t") #'wterm-copy-mode)`
- L166: `(define-key map (kbd "C-c C-l") #'wterm-clear-scrollback)`
- L167: `(define-key map (kbd "C-q") #'wterm-send-next-key)`
- L168: `(define-key map (kbd "C-y") #'wterm-yank)`
- L169: `(define-key map (kbd "M-w") #'wterm-copy-region-or-send)`
- L170: `(define-key map [S-insert] #'wterm-yank)`
- L171: `(define-key map [mouse-2] #'wterm-yank-primary)`
- L175: `(defvar wterm-copy-mode-map`
- L177: `(define-key map (kbd "C-c C-t") #'wterm-copy-mode)`
- L178: `(define-key map (kbd "q") #'wterm-copy-mode)`
- L179: `(define-key map (kbd "RET") #'wterm-copy-mode-done)`
- L180: `(define-key map (kbd "M-w") #'wterm-copy-mode-done)`
- L186: `(define-derived-mode wterm-mode fundamental-mode "WTerm"`
- L212: `(defun wterm (&optional arg)`
- L232: `(defun wterm-other-window (&optional arg)`
- L240: `(defun wterm--window-size ()`
- L248: `(defun wterm--start (command)`
- L279: `(defun wterm--palette ()`
- L291: `(defun wterm--update-palettes (&rest _)`
- L304: `(defun wterm--send-bytes (bytes)`
- L309: `(defun wterm--sanitize (string)`
- L313: `(defun wterm--filter (proc output)`
- L326: `(defun wterm--schedule-redraw ()`
- L344: `(defun wterm--redraw-now (buf)`
- L365: `(defun wterm--handle-events ()`
- L379: `(defun wterm--set-cursor-visible (visible)`
- L399: `(defun wterm--handle-osc (cmd text)`
- L411: `(defun wterm--local-directory (path)`
- L419: `(defun wterm--sentinel (proc event)`
- L433: `(defun wterm--on-kill ()`
- L441: `(defun wterm--adjust-process-window-size (process windows)`
- L454: `(defun wterm--resize (rows cols)`
- L461: `(defun wterm--mod-bits (mods)`
- L466: `(defun wterm-send-event (event)`
- L486: `(defun wterm--self-insert ()`
- L491: `(defun wterm-send-next-key ()`
- L496: `(defun wterm-send-C-c ()`
- L501: `(defun wterm-send-C-z ()`
- L506: `(defun wterm-send-string (string &optional paste)`
- L518: `(defun wterm-yank (&optional arg)`
- L526: `(defun wterm-yank-primary (event)`
- L532: `(defun wterm-copy-region-or-send ()`
- L539: `(defun wterm-clear-scrollback ()`
- L549: `(define-minor-mode wterm-copy-mode`
- L563: `(defun wterm-copy-mode-done ()`
- L570: `(provide 'wterm)`
