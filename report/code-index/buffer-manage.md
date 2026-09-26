# Indice del codice: buffer-manage

Fonte: https://github.com/plandes/buffer-manage.git

Revisione: `f32c756a261aebca0a864e41958097b30690e171`.


## buffer-manage.el

- L48: `(require 'cl-lib)`
- L49: `(require 'eieio)`
- L50: `(require 'derived)`
- L51: `(require 'choice-program-complete)`
- L52: `(require 'config-manage)`
- L72: `(defcustom buffer-manage-key-bindings`
- L98: `(defvar buffer-manage-remap-instances nil`
- L416: `(defun buffer-manager-process-sentinel (process msg entry manager)`
- L427: `(defun buffer-manager-kill-buffer-callback ()`
- L458: `(defun buffer-manage-post-command-hook ()`
- L719: `(define-key keymap key (cl-second def))`
- L777: `(defun buffer-manager-read-bind-choices (&optional use-last-default-p)`
- L800: `(defun buffer-manager-bind-functions (buffer-manager-instance-var)`
- L817: `(provide 'buffer-manage)`

## config-manage-base.el

- L36: `(require 'cl-lib)`
- L37: `(require 'seq)`
- L38: `(require 'time-stamp)`
- L39: `(require 'dash)`
- L40: `(require 'eieio)`
- L41: `(require 'eieio-base)`
- L42: `(require 'choice-program)`
- L43: `(require 'config-manage-declare)`
- L48: `(defun config-manage-error-report (err reason)`
- L343: `(defun config-manage-base-insert-at-position (seq elt pos)`
- L546: `(defun config-manage-base-iterate-name (name names)`
- L749: `(defun config-manage-base-mode-refresh ()`
- L761: `(defun config-manage-base-refresh-windows ()`
- L770: `(provide 'config-manage-base)`

## config-manage-declare.el

- L36: `(require 'eieio)`
- L37: `(require 'eieio-core)`
- L42: `(defmacro config-manage-declare-functions (&rest fns)`
- L55: `(defmacro config-manage-declare-methods (&rest fns)`
- L68: `(defmacro config-manage-declare-variables (&rest vars)`
- L79: `(defun config-manage-declare-mode-assert (&optional no-error-p this)`
- L95: `(defun config-manage-declare-slots (class)`
- L115: `(provide 'config-manage-declare)`

## config-manage-mode.el

- L38: `(require 'dash)`
- L39: `(require 'config-manage-declare)`
- L40: `(require 'config-manage-base)`
- L41: `(require 'config-manage-prop)`
- L53: `(defcustom config-manage-highlight t`
- L98: `(defun config-manage-mode-quit ()`
- L108: `(defun config-manage-mode-name-at-point ()`
- L118: `(defun config-manage-mode-mouse-down (event)`
- L125: `(defun config-manage-mode-mouse-up (event)`
- L134: `(defun config-manage-mode-next ()`
- L142: `(defun config-manage-mode-previous ()`
- L150: `(defun config-manage-mode-activate-entry (&optional name)`
- L159: `(defun config-manage-mode-view (&optional name)`
- L171: `(defun config-manage-mode-info (&optional name)`
- L180: `(defun config-manage-mode-edit (&optional name)`
- L191: `(defun config-manage-mode-set-status (status)`
- L200: `(defun config-manage-mode-mark-delete ()`
- L205: `(defun config-manage-mode-mark-show ()`
- L210: `(defun config-manage-mode-mark-undelete ()`
- L215: `(defun config-manage-mode-apply-selected (status replace func)`
- L231: `(defun config-manage-mode-delete-selected ()`
- L238: `(defun config-manage-mode-rename (new-name)`
- L251: `(defun config-manage-mode-new ()`
- L257: `(define-derived-mode config-manage-mode fundamental-mode "Configuration Manager"`
- L267: `(define-key config-manage-mode-map "q" 'config-manage-mode-quit)`
- L268: `(define-key config-manage-mode-map [down-mouse-2] 'config-manage-mode-mouse-down)`
- L269: `(define-key config-manage-mode-map [mouse-2] 'config-manage-mode-mouse-up)`
- L270: `(define-key config-manage-mode-map [return] 'config-manage-mode-activate-entry)`
- L271: `(define-key config-manage-mode-map "n" 'config-manage-mode-next)`
- L272: `(define-key config-manage-mode-map "p" 'config-manage-mode-previous)`
- L273: `(define-key config-manage-mode-map [(control down)] 'config-manage-mode-next)`
- L274: `(define-key config-manage-mode-map [(control up)] 'config-manage-mode-previous)`
- L275: `(define-key config-manage-mode-map "d" 'config-manage-mode-mark-delete)`
- L276: `(define-key config-manage-mode-map "s" 'config-manage-mode-mark-show)`
- L277: `(define-key config-manage-mode-map "u" 'config-manage-mode-mark-undelete)`
- L278: `(define-key config-manage-mode-map "i" 'config-manage-mode-new)`
- L279: `(define-key config-manage-mode-map "x" 'config-manage-mode-delete-selected)`
- L280: `(define-key config-manage-mode-map "g" 'config-manage-mode-refresh)`
- L281: `(define-key config-manage-mode-map "r" 'config-manage-mode-rename)`
- L282: `(define-key config-manage-mode-map "v" 'config-manage-mode-view)`
- L283: `(define-key config-manage-mode-map "?" 'config-manage-mode-info)`
- L284: `(define-key config-manage-mode-map "e" 'config-manage-mode-edit)`
- L333: `(provide 'config-manage-mode)`

## config-manage-prop.el

- L36: `(require 'dash)`
- L37: `(require 'eieio)`
- L38: `(require 'choice-program-complete)`
- L39: `(require 'config-manage-base)`
- L606: `(provide 'config-manage-prop)`

## config-manage.el

- L42: `(require 'config-manage-declare)`
- L47: `(require 'config-manage-base)`
- L48: `(require 'config-manage-prop)`
- L49: `(require 'config-manage-mode)`
- L57: `(provide 'config-manage)`
