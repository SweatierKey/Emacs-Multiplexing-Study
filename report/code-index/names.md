# Indice del codice: names

Fonte: https://github.com/Malabarba/names.git

Revisione: `45a272fae915148d9a74d4cb3c39917b272ee9c3`.


## names-dev.el

- L36: `(require 'names)`
- L37: `(require 'elisp-mode nil t)`
- L38: `(require 'lisp-mode nil t)`
- L44: `(defmacro names-compare-forms (name form-a form-b)`
- L52: `(defmacro names-compare-forms-assert (name form-a form-b)`
- L60: `(defmacro names-print (name &rest forms)`
- L83: `(defun names--looking-at-namespace ()`
- L92: `(defun names--generate-new-buffer (name &optional form)`
- L105: `(defmacro names--wrapped-in-namespace (command form &optional kill &rest body)`
- L153: `(defun names--top-of-namespace ()`
- L166: `(defun names-eval-defun (edebug-it)`
- L188: `(defun names--preceding-sexp ()`
- L194: `(defun names-eval-last-sexp (eval-last-sexp-arg-internal)`
- L202: `(defun names-eval-print-last-sexp (eval-last-sexp-arg-internal)`
- L212: `(defun names-pprint ()`
- L224: `(require 'find-func nil t)`
- L230: `(defun names--find-function-read (&optional type)`
- L241: `(defun names--dev-fboundp (sym)`
- L244: `(defun names--dev-boundp (sym)`
- L253: `(define-key map [remap eval-defun] #'names-eval-defun)`
- L254: `(define-key map [remap eval-last-sexp] #'names-eval-last-sexp)`
- L255: `(define-key map [remap eval-print-last-sexp] #'names-eval-print-last-sexp)))`
- L257: `(provide 'names-dev)`

## names.el

- L40: `(require 'cl-lib)`
- L53: `(require 'edebug)`
- L54: `(require 'bytecomp)`
- L55: `(require 'advice)`
- L309: `(defmacro names--prepend (sbl)`
- L315: `(defmacro names--filter-if-bound (var &optional pred)`
- L325: `(defmacro names--next-keyword (body)`
- L347: `(defmacro define-namespace (name &rest body)`
- L416: `(defun names--define-namespace-implementation (name body)`
- L497: `(defun names--reload-if-upgraded ()`
- L518: `(defun names-convert-form (form)`
- L571: `(defun names-view-manual ()`
- L576: `(defun names--package-name ()`
- L588: `(defun names--generate-defgroup ()`
- L597: `(defun names--generate-version ()`
- L613: `(defun names--add-macro-to-environment (form)`
- L657: `(defun names--extract-autoloads (body)`
- L689: `(defun names--make-autoload-compat (form file)`
- L697: `(defun names--handle-args (func args)`
- L711: `(defun names--message (f &rest rest)`
- L716: `(defun names--warn (f &rest rest)`
- L723: `(defun names--error-if-using-vars ()`
- L732: `(defun names--remove-namespace-from-list (&rest lists)`
- L738: `(defun names--remove-namespace (symbol)`
- L742: `(defun names--remove-protection (symbol)`
- L746: `(defun names--remove-regexp (s r)`
- L752: `(defun names--quote-p (sbl)`
- L756: `(defun names--fboundp (sbl)`
- L763: `(defun names--macrop (sbl)`
- L769: `(defun names--keyword (keyword)`
- L773: `(defun names--boundp (sbl)`
- L786: `(defun names--args-of-function-or-macro (function args macro)`
- L804: `(defun names--get-edebug-spec (name)`
- L824: `(defun names--macro-args-using-edebug (form)`
- L878: `(defun names--edebug-message (&rest args)`
- L883: `(defun names--edebug-make-enter-wrapper (forms)`
- L890: `(defun names--gensym (prefix)`
- L898: `(defun names--edebug-form (cursor)`
- L950: `(defun names--maybe-append-group (form)`
- L962: `(defun names--handle-keyword (body)`
- L990: `(defun names--convert-defmacro (form)`
- L1015: `(defun names--convert-defvaralias (form)`
- L1026: `(defun names--convert-defalias (form)`
- L1037: `(defun names--convert-defvar (form &optional dont-add)`
- L1052: `(defun names--convert-defcustom (form)`
- L1057: `(defun names--convert-custom-declare-variable (form)`
- L1076: `(defun names--convert-defface (form)`
- L1083: `(defun names--convert-define-derived-mode (form)`
- L1103: `(defun names--convert-define-minor-mode (form)`
- L1129: `(defun names--convert-define-globalized-minor-mode (form)`
- L1161: `(defun names--convert-quote (form)`
- L1196: `(defun names--handle-symbol-as-function (s)`
- L1203: `(defun names--convert-macro (form)`
- L1208: `(defun names--convert-lambda (form)`
- L1230: `(defun names--convert-clojure (form)`
- L1240: `(defun names--vars-from-arglist (args)`
- L1253: `(defun names--convert-defun (form)`
- L1265: `(defun names--let-var-convert-then-add (sym add)`
- L1274: `(defun names--convert-let (form &optional star)`
- L1297: `(defun names--convert-let* (form)`
- L1301: `(defun names--convert-cond (form)`
- L1309: `(defun names--convert-condition-case (form)`
- L1322: `(provide 'names)`
