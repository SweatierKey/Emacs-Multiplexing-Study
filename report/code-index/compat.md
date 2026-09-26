# Indice del codice: compat

Fonte: https://github.com/emacs-compat/compat.git

Revisione: `90880f81419577e1d3f68424d2a3adf31e6d663e`.


## .dir-locals.el


## compat-26.el

- L549: `(provide 'compat-26)`

## compat-27.el

- L289: `(define-key map [remap self-insert-command] #'read-char-from-minibuffer-insert-char)`
- L290: `(define-key map [remap exit-minibuffer] #'read-char-from-minibuffer-insert-other)`
- L324: `(define-key map (vector help-char)`
- L330: `(define-key map (vector char)`
- L332: `(define-key map [remap self-insert-command]`
- L884: `(provide 'compat-27)`

## compat-28.el

- L864: `(provide 'compat-28)`

## compat-29.el

- L927: `(define-key keymap (key-parse key) definition))`
- L953: `(keymap-set (current-global-map) key command))`
- L969: `(keymap-set map key command)))`
- L1000: `(define-key KEYMAP [remap OLDDEF] NEWDEF)`
- L1201: `(keymap-set keymap key def)))))`
- L1293: `(define-key keymap key def)`
- L1296: `(define-key keymap key nil)`
- L1590: `(provide 'compat-29)`

## compat-30.el

- L459: `(provide 'compat-30)`

## compat-31.el

- L414: `(provide 'compat-31)`

## compat-macs.el

- L33: `(require 'subr-x)`
- L34: `(require 'cl-lib)`
- L39: `(defun compat-macs--strict (cond &rest error)`
- L44: `(defun compat-macs--assert (cond &rest error)`
- L48: `(defun compat-macs--docstring (type name docstring)`
- L61: `(defun compat-macs--check-attributes (attrs preds)`
- L71: `(defun compat-macs--guard (attrs preds fun)`
- L96: `(defun compat-macs--defun (type name arglist docstring rest)`
- L142: `(defmacro compat-guard (cond &rest rest)`
- L161: `(defmacro compat-defalias (name def &rest attrs)`
- L183: `(defmacro compat-defun (name arglist docstring &rest rest)`
- L208: `(defmacro compat-defmacro (name arglist docstring &rest rest)`
- L216: `(defmacro compat-defvar (name initval docstring &rest attrs)`
- L260: `(defmacro compat-version (version)`
- L265: `(defmacro compat-require (feature version)`
- L271: `(provide 'compat-macs)`

## compat-tests.el

- L52: `(require 'compat)`
- L53: `(require 'ert-x)`
- L54: `(require 'subr-x)`
- L55: `(require 'cl-lib)`
- L56: `(require 'time-date)`
- L57: `(require 'image)`
- L58: `(require 'text-property-search nil t)`
- L59: `(require 'color)`
- L62: `(require 'tramp)`
- L76: `(defmacro should-equal (a b)`
- L511: `(defvar compat-tests--map-1`
- L513: `(define-key map (kbd "C-x C-f") #'find-file)`
- L514: `(define-key map (kbd "SPC") #'minibuffer-complete-word)`
- L515: `(define-key map (kbd "RET") #'exit-minibuffer)`
- L516: `(define-key map [remap exit-minibuffer] #'minibuffer-force-complete-and-exit)`
- L517: `(define-key map (kbd "C-c") mode-specific-map)`
- L518: `(define-key map (kbd "s-c") [?\C-c ?\C-c])`
- L519: `(define-key map [t] 'compat-default-command)`
- L521: `(defvar compat-tests--map-2`
- L523: `(keymap-set map "C-x C-f" #'find-file)`
- L524: `(keymap-set map "SPC" #'minibuffer-complete-word)`
- L525: `(keymap-set map "RET" #'exit-minibuffer)`
- L526: `(keymap-set map "<remap> <exit-minibuffer>" #'minibuffer-force-complete-and-exit)`
- L527: `(keymap-set map "C-c" mode-specific-map)`
- L528: `(keymap-set map "s-c" "C-c C-c")`
- L529: `(keymap-set map "<t>" 'compat-default-command)`
- L531: `(defvar-keymap compat-tests--map-3`
- L539: `(defvar compat-tests--map-4`
- L832: `(keymap-global-set "H-c" 'test)`
- L833: `(keymap-global-set "<t>" 'default)`
- L847: `(define-key map "\M-x" #'execute-extended-command)`
- L848: `(define-key map "\C-x\C-f" #'find-file)`
- L849: `(define-key map "\C-y" #'yank)`
- L855: `(define-key map "\M-x" #'execute-extended-command)`
- L856: `(define-key map "\C-x\C-f" #'find-file)`
- L857: `(define-key map "\C-y" #'yank)`
- L869: `(define-key map "\M-x" #'execute-extended-command)`
- L870: `(define-key map "\C-x\C-f" #'find-file)`
- L871: `(define-key map "\C-y" #'yank)`
- L884: `(define-key map "\M-x" #'execute-extended-command)`
- L885: `(define-key map "\C-x\C-f" #'find-file)`
- L886: `(define-key map "\C-y" #'yank)`
- L895: `(define-key map "\M-x" #'execute-extended-command)`
- L896: `(define-key map "\C-x\C-f" #'find-file)`
- L897: `(define-key map "\C-y" #'yank)`
- L1792: `(defmacro compat--should-value< (x y)`
- L2124: `(defmacro compat-tests--string-to-multibyte (str)`
- L2629: `(defun compat-tests--color-approx-equal (color1 color2)`
- L2670: `(define-key a-map "x" 'foo)`
- L2671: `(define-key b-map "x" 'bar)`
- L2680: `(defmacro compat-tests--filename ()`
- L2690: `(defun compat-tests--with-suppressed-warnings ()`
- L3030: `(defmacro compat-tests--with-gensyms ()`
- L3045: `(defmacro compat-tests--once-only (x)`
- L3490: `(provide 'compat-tests)`

## compat.el

- L60: `(defmacro compat-function (fun)`
- L75: `(defmacro compat-call (fun &rest args)`
- L92: `(provide 'compat)`
