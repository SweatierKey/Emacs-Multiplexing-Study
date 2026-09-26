# Indice del codice: posframe

Fonte: https://github.com/tumashu/posframe.git

Revisione: `bdabcec96f127b2daa2f8bf988a71ec146e301d5`.


## posframe-benchmark.el

- L30: `(require 'cl-lib)`
- L31: `(require 'posframe)`
- L70: `(defun posframe-benchmark ()`
- L81: `(provide 'posframe-benchmark)`

## posframe.el

- L41: `(require 'cl-lib)`
- L48: `(defcustom posframe-inhibit-double-buffering nil`
- L53: `(defcustom posframe-mouse-banish-function #'posframe-mouse-banish-default`
- L61: `(defcustom posframe-text-scale-factor-function #'posframe-text-scale-factor-default`
- L132: `(defun posframe-workable-p ()`
- L142: `(cl-defun posframe-show (buffer-or-name`
- L591: `(defun posframe--get-font-height (position)`
- L608: `(cl-defun posframe--create-posframe (buffer-or-name`
- L814: `(defun posframe--find-existing-posframe (buffer &optional last-args)`
- L836: `(defun posframe-delete-frame (buffer-or-name)`
- L856: `(defun posframe--insert-string (string no-properties)`
- L869: `(defun posframe--set-frame-size (size-info)`
- L893: `(defun posframe--set-frame-size-and-position (size-info position parent-frame-width parent-frame-height)`
- L909: `(defun posframe--fit-frame-to-buffer (posframe max-height min-height max-width min-width only)`
- L923: `(defun posframe--run-refresh-timer (repeat size-info)`
- L944: `(defun posframe-run-poshandler (info)`
- L960: `(defun posframe--get-valid-poshandler (info)`
- L972: `(defun posframe--calculate-new-position (info position ref-position)`
- L989: `(defun posframe--set-frame-position (posframe position`
- L1010: `(defun posframe--save-new-posframe-position (posframe`
- L1021: `(defun posframe--make-frame-visible (posframe)`
- L1028: `(defun posframe--posframe-need-redraw-p (posframe)`
- L1036: `(defun posframe--run-timeout-timer (posframe secs)`
- L1045: `(defun posframe--make-frame-invisible (frame)`
- L1051: `(defun posframe-mouse-banish-simple (info)`
- L1069: `(defun posframe-mouse-banish-default (info)`
- L1097: `(defun posframe-refresh (buffer-or-name)`
- L1128: `(defun posframe-hide-all ()`
- L1135: `(defun posframe-hide (buffer-or-name)`
- L1150: `(defun posframe-hidehandler-daemon ()`
- L1157: `(defun posframe-hidehandler-daemon-function ()`
- L1173: `(defun posframe-hidehandler-when-buffer-switch (info)`
- L1184: `(defun posframe-delete-all ()`
- L1196: `(defun posframe--kill-buffer (buffer-or-name)`
- L1202: `(defun posframe-delete (buffer-or-name)`
- L1211: `(defun posframe-funcall (buffer-or-name function &rest arguments)`
- L1221: `(defun posframe-poshandler-absolute-x-y (info)`
- L1235: `(defun posframe-poshandler-point-1 (info &optional font-height upward)`
- L1275: `(defun posframe-poshandler-point-bottom-left-corner (info)`
- L1285: `(defun posframe-poshandler-point-window-center (info)`
- L1298: `(defun posframe-poshandler-point-frame-center (info)`
- L1311: `(defun posframe-poshandler-point-bottom-left-corner-upward (info)`
- L1321: `(defun posframe-poshandler-point-top-left-corner (info)`
- L1332: `(defun posframe-poshandler-frame-center (info)`
- L1347: `(defun posframe-poshandler-frame-top-center (info)`
- L1360: `(defun posframe-poshandler-frame-top-left-corner (_info)`
- L1370: `(defun posframe-poshandler-frame-top-right-corner (_info)`
- L1380: `(defun posframe-poshandler-frame-top-left-or-right-other-corner (info)`
- L1399: `(defun posframe-poshandler-frame-bottom-left-corner (info)`
- L1411: `(defun posframe-poshandler-frame-bottom-right-corner (info)`
- L1423: `(defun posframe-poshandler-frame-bottom-center (info)`
- L1439: `(defun posframe-poshandler-window-center (info)`
- L1456: `(defun posframe-poshandler-window-top-left-corner (info)`
- L1469: `(defun posframe-poshandler-window-top-right-corner (info)`
- L1485: `(defun posframe-poshandler-window-top-center (info)`
- L1500: `(defun posframe-poshandler-window-bottom-left-corner (info)`
- L1517: `(defun posframe-poshandler-window-bottom-right-corner (info)`
- L1537: `(defun posframe-poshandler-window-bottom-center (info)`
- L1556: `(defun posframe-refposhandler-xwininfo (&optional frame)`
- L1583: `(defun posframe--redirect-posframe-focus ()`
- L1593: `(defun posframe-text-scale-factor-default (parent-text-scale-mode-amount)`
- L1598: `(provide 'posframe)`
