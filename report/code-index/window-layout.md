# Indice del codice: window-layout

Fonte: https://github.com/kiwanami/emacs-window-layout.git

Revisione: `277d0a8247adf13707703574cbbc16ddcff7c5fd`.


## window-layout.el

- L126: `(defmacro wlf:aif (test-form then-form &rest else-forms)`
- L132: `(defmacro wlf:acond (&rest clauses)`
- L142: `(defun wlf:current-first-line-point (window)`
- L179: `(defun wlf:window-shown-set (winfo i)`
- L183: `(defun wlf:window-shown-p (winfo)`
- L187: `(defun wlf:window-shown-toggle (winfo)`
- L194: `(defun wlf:window-window-by-edge (winfo)`
- L210: `(defun wlf:window-live-window (winfo)`
- L216: `(defun wlf:window-size (winfo)`
- L225: `(defmacro wlf:window-option-get (winfo option-key)`
- L232: `(defun wlf:clear-windows (winfo-list wholep)`
- L251: `(defun wlf:get-winfo (name winfo-list)`
- L259: `(defun wlf:build-windows-rec (recipe winfo-list)`
- L307: `(defun wlf:apply-split-options (split-options verticalp)`
- L326: `(defun wlf:window-shrink (window verticalp shrink-size)`
- L334: `(defun wlf:window-resize (window verticalp target-size)`
- L347: `(defun wlf:apply-winfo (winfo)`
- L358: `(defun wlf:set-window-points (winfo)`
- L381: `(defun wlf:collect-window-edges (winfo-list)`
- L390: `(defun wlf:calculate-last-window-sizes (winfo-list)`
- L404: `(defun wlf:calculate-init-window-sizes (winfo-list)`
- L418: `(defun wlf:restore-window-sizes (winfo-list)`
- L440: `(defun wlf:make-winfo-list (wparams)`
- L447: `(defun wlf:translate-recipe (recipe)`
- L484: `(defun wlf:max-window-size-p (winfo)`
- L494: `(defun wlf:save-current-window-sizes (recipe winfo-list)`
- L518: `(defun wlf:layout (recipe window-params &optional subwindow-p)`
- L528: `(defun wlf:no-layout (recipe window-params &optional subwindow-p)`
- L535: `(defmacro wlf:with-wset (wset &rest body)`
- L546: `(defun wlf:layout-internal (wset &optional restore-window-size)`
- L576: `(defun wlf:layout-hook-add (wset func)`
- L584: `(defun wlf:layout-hook-remove (wset func)`
- L591: `(defun wlf:refresh (wset)`
- L596: `(defun wlf:reset-window-sizes (wset)`
- L600: `(defun wlf:reset-init (wset)`
- L606: `(defun wlf:show (wset &rest winfo-names)`
- L617: `(defun wlf:hide (wset &rest winfo-names)`
- L628: `(defun wlf:toggle (wset &rest winfo-names)`
- L638: `(defun wlf:select (wset winfo-name)`
- L648: `(defun wlf:get-window (wset winfo-name)`
- L665: `(defun wlf:set-buffer (wset winfo-name buf &optional selectp)`
- L688: `(defun wlf:get-buffer (wset winfo-name)`
- L697: `(defun wlf:window-name-p (wset winfo-name)`
- L702: `(defun wlf:window-displayed-p (wset winfo-name)`
- L708: `(defun wlf:wopts-replace-buffer (wopts buffer-alist)`
- L724: `(defun wlf:copy-windows (wset)`
- L733: `(defun wlf:copy-winfo (winfo)`
- L744: `(defun wlf:maximize-info-get ()`
- L748: `(defun wlf:maximize-info-set (val)`
- L752: `(defun wlf:maximize-info-clear ()`
- L756: `(defun wlf:collect-window-states (wset)`
- L762: `(defun wlf:revert-window-states (wset states)`
- L771: `(defun wlf:maximize-window-states (wset winfo-name)`
- L780: `(defun wlf:toggle-maximize (wset winfo-name)`
- L802: `(defun wlf:get-window-name (wset window)`
- L814: `(defun wlf:wset-live-p (wset)`
- L837: `(defun wlf:wset-clear-window-points (wset)`
- L846: `(defun wlf:wset-fix-windows (wset)`
- L941: `(provide 'window-layout)`
