# Indice del codice: eat-serial

Fonte: https://github.com/ArthurHeymans/eat-serial.git

Revisione: `5510c23cd97994e98c068903c93545f3e4077881`.


## eat-serial-codec.el

- L22: `(require 'cl-lib)`
- L29: `(defcustom eat-serial-invalid-byte-policy 'replacement`
- L46: `(defun eat-serial-codec-make-state (&optional invalid-byte-policy)`
- L55: `(defun eat-serial-codec-reset (state)`
- L59: `(defun eat-serial-codec--unibyte (string)`
- L78: `(defun eat-serial-codec--continuation-byte-p (byte)`
- L82: `(defun eat-serial-codec--valid-sequence-byte-p (lead offset byte)`
- L93: `(defun eat-serial-codec--valid-prefix-p (bytes index end)`
- L105: `(defun eat-serial-codec--invalid-byte-string (byte policy)`
- L112: `(defun eat-serial-codec--valid-codepoint-p (codepoint min-codepoint)`
- L118: `(defun eat-serial-codec--decode-codepoint (bytes index length)`
- L134: `(defun eat-serial-codec--sequence-shape (byte)`
- L143: `(defun eat-serial-codec-decode (state chunk)`
- L205: `(defun eat-serial-codec-flush (state)`
- L218: `(provide 'eat-serial-codec)`

## eat-serial-tests.el

- L10: `(require 'ert)`
- L11: `(require 'cl-lib)`
- L12: `(require 'eat-serial-codec)`
- L38: `(defun eat-serial-tests--require-eat-serial ()`
- L43: `(defun eat-serial-tests--sleep-process (buffer)`
- L50: `(defun eat-serial-tests--decode-chunks (chunks &optional policy)`
- L254: `(provide 'eat-serial-tests)`

## eat-serial.el

- L23: `(require 'cl-lib)`
- L24: `(require 'subr-x)`
- L25: `(require 'format-spec)`
- L26: `(require 'eat)`
- L27: `(require 'eat-serial-codec)`
- L34: `(defcustom eat-serial-default-speed 115200`
- L39: `(defcustom eat-serial-default-coding-system 'utf-8-unix`
- L44: `(defcustom eat-serial-default-input-mode 'semi-char`
- L52: `(defcustom eat-serial-speed-history`
- L58: `(defcustom eat-serial-buffer-name-format "*eat-serial %p*"`
- L65: `(defcustom eat-serial-break-duration 0`
- L72: `(defcustom eat-serial-send-break-function nil`
- L92: `(defvar eat-serial-mode-map`
- L94: `(define-key map (kbd "C-c C-k") #'eat-serial-disconnect)`
- L95: `(define-key map (kbd "C-c C-s r") #'eat-serial-reconnect)`
- L96: `(define-key map (kbd "C-c C-s d") #'eat-serial-disconnect)`
- L97: `(define-key map (kbd "C-c C-s c") #'eat-serial-configure)`
- L98: `(define-key map (kbd "C-c C-s b") #'eat-serial-send-break)`
- L99: `(define-key map (kbd "C-c C-s x") #'eat-serial-send-byte)`
- L103: `(define-minor-mode eat-serial-mode`
- L108: `(defun eat-serial--buffer-name (port)`
- L112: `(defun eat-serial--read-port ()`
- L116: `(defun eat-serial--live-process-p (&optional process)`
- L123: `(defun eat-serial--require-process ()`
- L129: `(defun eat-serial--mode-line-string ()`
- L155: `(defun eat-serial--mode-line-item (text help-echo command)`
- L163: `(defun eat-serial--speed-string ()`
- L169: `(defun eat-serial--configuration-summary ()`
- L184: `(defun eat-serial--popup-mode-line-menu (event keymap)`
- L196: `(defun eat-serial--install-mode-line ()`
- L204: `(defun eat-serial--display-window ()`
- L215: `(defun eat-serial--resize-terminal-to-window (&rest _)`
- L229: `(defun eat-serial--set-terminal-parameter-if-bound (parameter function)`
- L234: `(defun eat-serial--set-terminal-process (process)`
- L241: `(defun eat-serial--buffer-processes (&optional buffer)`
- L253: `(defun eat-serial--delete-foreign-buffer-processes ()`
- L264: `(defun eat-serial--serial-terminal-p ()`
- L270: `(defun eat-serial--reset-foreign-terminal ()`
- L284: `(defun eat-serial--install-terminal-functions (&optional process)`
- L309: `(defun eat-serial--select-default-input-mode ()`
- L317: `(defun eat-serial--ensure-terminal ()`
- L337: `(defun eat-serial--setup-buffer (port speed)`
- L354: `(defun eat-serial--set-configuration (speed bytesize parity stopbits flowcontrol)`
- L362: `(defun eat-serial--configure-process`
- L373: `(defun eat-serial--apply-configuration`
- L395: `(defun eat-serial-set-speed (speed)`
- L406: `(defun eat-serial-set-framing (bytesize parity stopbits)`
- L432: `(defun eat-serial-set-flowcontrol (flowcontrol)`
- L450: `(defun eat-serial--clear-process-state (&optional state)`
- L457: `(defun eat-serial--process-arguments ()`
- L474: `(defun eat-serial--open-process ()`
- L499: `(defun eat-serial--queue-output (process text)`
- L509: `(defun eat-serial--filter (process chunk)`
- L523: `(defun eat-serial--sentinel (process message)`
- L542: `(defun eat-serial--send-raw-string (process bytes)`
- L558: `(defun eat-serial--send-input (_terminal input)`
- L571: `(defun eat-serial (port &optional speed)`
- L598: `(defun eat-serial-reconnect ()`
- L608: `(defun eat-serial-disconnect ()`
- L618: `(defun eat-serial--read-choice (prompt choices current)`
- L627: `(defun eat-serial-configure (speed bytesize parity stopbits flowcontrol)`
- L669: `(defun eat-serial--parse-byte (string)`
- L682: `(defun eat-serial--read-byte ()`
- L691: `(defun eat-serial-send-byte (byte)`
- L697: `(defun eat-serial--python-send-break (process duration)`
- L712: `(defun eat-serial-send-break (&optional duration)`
- L727: `(defun eat-serial-copy-port-name ()`
- L735: `(defun eat-serial--connection-menu ()`
- L738: `(define-key map [copy-port]`
- L741: `(define-key map [send-byte]`
- L744: `(define-key map [send-break]`
- L747: `(define-key map [separator-1] '(menu-item "--"))`
- L748: `(define-key map [configure]`
- L751: `(define-key map [disconnect]`
- L754: `(define-key map [reconnect]`
- L759: `(defun eat-serial--speed-menu ()`
- L768: `(define-key map [other]`
- L771: `(define-key map [separator-1] '(menu-item "--"))`
- L784: `(defun eat-serial--config-menu ()`
- L787: `(define-key map [configure]`
- L790: `(define-key map [separator-1] '(menu-item "--"))`
- L806: `(define-key map [separator-2] '(menu-item "--"))`
- L819: `(define-key map [separator-3] '(menu-item "--"))`
- L835: `(define-key map [separator-4] '(menu-item "--"))`
- L848: `(define-key map [separator-5] '(menu-item "--"))`
- L864: `(defun eat-serial-mode-line-connection-menu (event)`
- L869: `(defun eat-serial-mode-line-speed-menu (event)`
- L874: `(defun eat-serial-mode-line-config-menu (event)`
- L879: `(provide 'eat-serial)`
