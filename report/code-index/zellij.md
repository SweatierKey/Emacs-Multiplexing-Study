# Indice del codice: zellij

Fonte: https://github.com/mandoo180/zellij.el.git

Revisione: `985ebccd222d5e288c178729328ab8e94eda3ba3`.


## examples/zellij-config.el

- L56: `(define-key org-mode-map (kbd "C-c z e") #'zellij-org-babel-execute)`
- L57: `(define-key org-mode-map (kbd "C-c z b") #'zellij-org-send-block)))`
- L62: `(defun my/ask-claude ()`
- L75: `(defun my/zellij-run-tests ()`
- L83: `(defun my/send-to-opencode ()`
- L101: `(defun my/pane-name-with-emoji (command)`
- L116: `(defun my/setup-project-zellij ()`
- L134: `(global-set-key (kbd "C-c a c") #'my/ask-claude)`
- L135: `(global-set-key (kbd "C-c a o") #'my/send-to-opencode)`
- L139: `(define-key zellij-mode-map (kbd "C-c z r") #'my/zellij-run-tests)`
- L140: `(define-key zellij-mode-map (kbd "C-c z P") #'my/setup-project-zellij))`
- L145: `(defun my/set-project-zellij-session ()`
- L159: `(defun my/get-language-for-mode ()`
- L177: `(defun my/disable-formatting-for-text-modes ()`
- L206: `(defun my/auto-target-for-python ()`
- L248: `(global-set-key (kbd "C-c z z") #'hydra-zellij/body))`

## zellij-org.el

- L57: `(require 'zellij)`
- L58: `(require 'org)`
- L62: `(defun zellij-org--get-target-from-properties ()`
- L79: `(defun zellij-org-babel-execute ()`
- L114: `(defun zellij-org-send-block ()`
- L148: `(defvar zellij-org-mode-map`
- L150: `(define-key map (kbd "C-c z e") #'zellij-org-babel-execute)`
- L151: `(define-key map (kbd "C-c z b") #'zellij-org-send-block)`
- L156: `(define-minor-mode zellij-org-mode`
- L164: `(defun zellij-org-setup ()`
- L169: `(provide 'zellij-org)`

## zellij.el

- L55: `(require 'cl-lib)`
- L56: `(require 'project)`
- L65: `(defcustom zellij-executable "zellij"`
- L70: `(defcustom zellij-default-session nil`
- L77: `(defcustom zellij-default-pane-direction "right"`
- L84: `(defcustom zellij-use-project-root t`
- L90: `(defcustom zellij-prompt-for-pane-name t`
- L95: `(defcustom zellij-default-pane-name-function #'zellij--default-pane-name`
- L101: `(defcustom zellij-echo-commands nil`
- L106: `(defcustom zellij-log-buffer-name "*Zellij Log*"`
- L111: `(defcustom zellij-enable-logging t`
- L116: `(defcustom zellij-format-code-blocks t`
- L121: `(defcustom zellij-auto-detect-language t`
- L126: `(defcustom zellij-ai-cli-patterns`
- L139: `(defcustom zellij-pane-targeting-strategy 'navigate`
- L160: `(defun zellij-available-p ()`
- L164: `(defun zellij--current-session ()`
- L169: `(defun zellij--effective-session (&optional session)`
- L176: `(defun zellij--log (format-string &rest args)`
- L188: `(defun zellij--error (format-string &rest args)`
- L194: `(defun zellij--call (args)`
- L209: `(defun zellij--call-async (args &optional callback)`
- L227: `(defun zellij--get-working-directory ()`
- L235: `(defun zellij--default-pane-name (command)`
- L241: `(defun zellij--get-language-for-mode ()`
- L279: `(defun zellij-list-sessions ()`
- L291: `(defun zellij-select-session ()`
- L299: `(defun zellij-session-exists-p (session)`
- L305: `(defun zellij-write-chars (text &optional session)`
- L312: `(defun zellij-write-bytes (bytes &optional session)`
- L320: `(defun zellij-send-command (command &optional session)`
- L328: `(defun zellij-send-text (text &optional session)`
- L335: `(defun zellij-send-lines (lines &optional session)`
- L343: `(defun zellij-go-to-tab (tab &optional session)`
- L353: `(defun zellij-next-tab (&optional session)`
- L360: `(defun zellij-previous-tab (&optional session)`
- L367: `(defun zellij-focus-next-pane (&optional session)`
- L374: `(defun zellij-focus-previous-pane (&optional session)`
- L381: `(defun zellij--navigate-to-pane (tab pane-offset &optional session)`
- L426: `(defun zellij--send-with-navigation (tab pane-offset text &optional session)`
- L471: `(defun zellij--parse-layout (&optional session)`
- L481: `(defun zellij--parse-layout-string (layout-str)`
- L503: `(defun zellij--parse-panes-in-region (start end)`
- L549: `(defun zellij--get-focused-pane (&optional session)`
- L567: `(defun zellij--pane-exists-p (tab pane-offset &optional session)`
- L581: `(defun zellij--detect-ai-panes (&optional session)`
- L599: `(defun zellij--match-ai-pattern (command args)`
- L607: `(defun zellij--get-ai-pane-suggestions (&optional session)`
- L620: `(defun zellij--get-all-panes-for-selection (&optional session)`
- L665: `(defun zellij--should-format-as-code (target)`
- L685: `(defun zellij--format-as-code-block (text &optional language)`
- L695: `(defun zellij-send-to-pane (tab pane-offset command &optional session)`
- L709: `(defun zellij-new-pane (&optional command direction name cwd session)`
- L736: `(defun zellij-new-pane-with-command ()`
- L747: `(defun zellij-new-tab (&optional name cwd layout session)`
- L780: `(defun zellij-new-tab-with-name ()`
- L788: `(defun zellij--get-target (&optional specified-target)`
- L817: `(defun zellij--set-target-manual ()`
- L831: `(defun zellij-set-target-pane ()`
- L854: `(defun zellij-clear-target-pane ()`
- L862: `(defun zellij-show-target ()`
- L870: `(defun zellij-list-panes ()`
- L897: `(defun zellij--send-to-target (text target)`
- L925: `(defun zellij-send-region (start end &optional target)`
- L937: `(defun zellij-send-buffer (&optional target)`
- L942: `(defun zellij-send-region-or-buffer ()`
- L949: `(defun zellij-send-line ()`
- L954: `(defun zellij-send-paragraph ()`
- L964: `(defun zellij-send-to-pane-interactive ()`
- L982: `(defun zellij-send-command-to-target (command)`
- L989: `(defun zellij-send-to-ai (text)`
- L1002: `(defun zellij-toggle-code-formatting ()`
- L1011: `(defun zellij-show-log ()`
- L1020: `(defun zellij-clear-log ()`
- L1039: `(defun zellij--setup-mode-line ()`
- L1044: `(defun zellij--teardown-mode-line ()`
- L1051: `(defvar zellij-mode-map`
- L1054: `(define-key map (kbd "C-c z s") #'zellij-send-region-or-buffer)`
- L1055: `(define-key map (kbd "C-c z l") #'zellij-send-line)`
- L1056: `(define-key map (kbd "C-c z p") #'zellij-send-paragraph)`
- L1057: `(define-key map (kbd "C-c z c") #'zellij-send-command-to-target)`
- L1058: `(define-key map (kbd "C-c z a") #'zellij-send-to-ai)`
- L1061: `(define-key map (kbd "C-c z t") #'zellij-set-target-pane)`
- L1062: `(define-key map (kbd "C-c z T") #'zellij-clear-target-pane)`
- L1063: `(define-key map (kbd "C-c z ?") #'zellij-show-target)`
- L1064: `(define-key map (kbd "C-c z i") #'zellij-list-panes)`
- L1067: `(define-key map (kbd "C-c z n") #'zellij-new-pane-with-command)`
- L1070: `(define-key map (kbd "C-c z N") #'zellij-new-tab-with-name)`
- L1073: `(define-key map (kbd "C-c z g") #'zellij-send-to-pane-interactive)`
- L1076: `(define-key map (kbd "C-c z f") #'zellij-toggle-code-formatting)`
- L1079: `(define-key map (kbd "C-c z L") #'zellij-show-log)`
- L1085: `(define-minor-mode zellij-mode`
- L1103: `(provide 'zellij)`
