# Indice del codice: alert

Fonte: https://github.com/jwiegley/alert.git

Revisione: `31fc56855289d0846e73d7ca9b84b628aeac16a0`.


## alert-test.el

- L11: `(require 'ert)`
- L12: `(require 'alert)`
- L180: `(provide 'alert-test)`

## alert.el

- L192: `(require 'cl-lib)`
- L193: `(require 'gntp nil t)`
- L198: `(require 'notifications nil t)`
- L199: `(require 'log4e nil t)`
- L226: `(defcustom alert-severity-faces`
- L237: `(defcustom alert-severity-colors`
- L249: `(defcustom alert-log-severity-functions`
- L260: `(defcustom alert-log-level`
- L266: `(defcustom alert-reveal-idle-time 15`
- L271: `(defcustom alert-persist-idle-time 900`
- L277: `(defcustom alert-fade-time 5`
- L283: `(defcustom alert-hide-all-notifications nil`
- L288: `(defcustom alert-log-messages t`
- L293: `(defcustom alert-default-icon`
- L302: `(defun alert-styles-radio-type (widget-name)`
- L316: `(defcustom alert-default-style 'message`
- L323: `(defun alert-configuration-type ()`
- L393: `(defcustom alert-user-configuration nil`
- L434: `(defun alert-define-style (name &rest plist)`
- L486: `(cl-defun alert-add-rule (&key severity status mode category title`
- L568: `(defun alert-log-notify (info)`
- L586: `(defun alert-legacy-log-notify (mes sev len)`
- L597: `(defun alert-log-clear (info)`
- L614: `(defun alert-message-notify (info)`
- L622: `(defun alert-message-remove (_info)`
- L630: `(defun alert-momentary-notify (info)`
- L652: `(defun alert-fringe-notify (info)`
- L656: `(defun alert-fringe-restore (_info)`
- L665: `(defun alert-mode-line-notify (info)`
- L670: `(defun alert-mode-line-restore (_info)`
- L680: `(defcustom alert-growl-command (executable-find "growlnotify")`
- L686: `(defcustom alert-growl-priorities`
- L700: `(defun alert-growl-notify (info)`
- L737: `(defcustom alert-libnotify-command (executable-find "notify-send")`
- L744: `(defcustom alert-libnotify-additional-args`
- L751: `(defcustom alert-libnotify-priorities`
- L762: `(defun alert-libnotify-notify (info)`
- L813: `(defcustom alert-gntp-icon`
- L838: `(defcustom alert-notifications-priorities`
- L887: `(defcustom alert-notifier-command (executable-find "terminal-notifier")`
- L893: `(defcustom alert-notifier-default-icon`
- L900: `(defun alert-notifier-notify (info)`
- L912: `(defun alert-osx-notifier-notify (info)`
- L929: `(defun alert-frame-notify (info)`
- L951: `(defun alert-frame-remove (info)`
- L957: `(defun x-urgency-hint (frame arg &optional source)`
- L975: `(defun x-urgent (&optional arg)`
- L984: `(defun alert-x11-notify (_info)`
- L992: `(defcustom alert-toaster-default-icon`
- L1002: `(defcustom alert-toaster-command (executable-find "toast")`
- L1009: `(defun alert-toaster-notify (info)`
- L1022: `(defcustom alert-termux-command (executable-find "termux-notification")`
- L1029: `(defun alert-termux-notify (info)`
- L1052: `(defun alert-buffer-status (&optional buffer)`
- L1067: `(defun alert-remove-when-active (remover info)`
- L1078: `(defun alert-remove-on-command ()`
- L1089: `(defun alert-send-notification`
- L1104: `(cl-defun alert (message &key (severity 'normal) title icon category`
- L1252: `(provide 'alert)`
