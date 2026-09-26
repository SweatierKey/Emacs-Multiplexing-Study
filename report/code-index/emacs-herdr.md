# Indice del codice: emacs-herdr

Fonte: https://github.com/baongoc124/emacs-herdr.git

Revisione: `4c84bfe4d7487df53f03dd073a91d3f43b18643d`.


## herdr.el

- L46: `(require 'ghostel)`
- L47: `(require 'project)`
- L48: `(require 'json)`
- L49: `(require 'transient)`
- L50: `(require 'vc-git)`
- L59: `(defcustom herdr-executable "herdr"`
- L63: `(defcustom herdr-poll-interval 2`
- L67: `(defcustom herdr-default-agent-kind "claude"`
- L71: `(defcustom herdr-sync-workspace-labels 'project`
- L80: `(defcustom herdr-sync-tab-labels t`
- L84: `(defcustom herdr-workspace-label-function #'identity`
- L89: `(defcustom herdr-agent-display 'tui`
- L97: `(defcustom herdr-attach-takeover t`
- L104: `(defun herdr--bind-menu-key (key bind)`
- L109: `(keymap-global-set key #'herdr-menu)`
- L118: `(defcustom herdr-menu-repeat-command #'herdr-toggle`
- L126: `(defcustom herdr-menu-key nil`
- L164: `(defun herdr--call-json-sync (&rest args)`
- L174: `(defun herdr--call-async (callback &rest args)`
- L202: `(defun herdr--extract-agents (json)`
- L228: `(defun herdr--workspace-for-root (root json)`
- L240: `(defun herdr--fetch-agents-sync ()`
- L247: `(defun herdr--sort-agents (agents)`
- L257: `(defun herdr--format-candidate (agent)`
- L272: `(defun herdr--pick-agent (&optional prompt)`
- L284: `(defun herdr--project-name (dir)`
- L293: `(defun herdr--generic-title-p (title kind)`
- L299: `(defun herdr--workspace-label (agent)`
- L312: `(defun herdr--sync-labels (agents)`
- L319: `(defun herdr--sync-tab-labels (agents)`
- L331: `(defun herdr--sync-workspace-labels (agents)`
- L344: `(defun herdr--buffer-live-p ()`
- L351: `(defun herdr--create-buffer ()`
- L364: `(defun herdr ()`
- L378: `(defun herdr--attach-buffer-name (agent)`
- L386: `(defun herdr--find-attach-buffer (pane-id)`
- L396: `(defun herdr--create-attach-buffer (agent)`
- L412: `(defun herdr--attach-agent (agent &optional reattach)`
- L424: `(defun herdr--attach-buffers ()`
- L432: `(defun herdr-last-agent ()`
- L440: `(defun herdr--show-agent (agent)`
- L450: `(defun herdr-hide ()`
- L458: `(defun herdr-toggle ()`
- L466: `(defun herdr-switch-agent ()`
- L472: `(defun herdr-attach-agent (&optional reattach)`
- L479: `(defun herdr-goto-blocked ()`
- L488: `(defun herdr--sanitize-name (str)`
- L495: `(defun herdr--unique-agent-name (base agents)`
- L506: `(defun herdr-new-agent ()`
- L546: `(defun herdr--detect-language ()`
- L554: `(defun herdr--format-region (beg end)`
- L576: `(defun herdr-send-region (beg end &optional submit)`
- L595: `(defun herdr--mode-line-segment ()`
- L603: `(defun herdr--poll ()`
- L626: `(defun herdr--ensure-timer ()`
- L633: `(defun herdr--stop-timer ()`
- L641: `(defvar-keymap herdr-agents-mode-map`
- L651: `(define-derived-mode herdr-agents-mode tabulated-list-mode "Herdr-Agents"`
- L665: `(defun herdr--status-face (status)`
- L673: `(defun herdr--agent-entry (agent)`
- L688: `(defun herdr--agents-set-entries (agents)`
- L693: `(defun herdr--agents-render (agents)`
- L701: `(defun herdr--agents-revert ()`
- L705: `(defun herdr--agent-at-point ()`
- L715: `(defun herdr-agents-sort ()`
- L734: `(defun herdr-agents-show (&optional reattach)`
- L742: `(defun herdr-agents-attach (&optional reattach)`
- L749: `(defun herdr-agents ()`
- L766: `(defun herdr--invoking-key ()`
- L775: `(defun herdr-submit-region (beg end)`
- L780: `(defun herdr--menu-description ()`
- L787: `(defun herdr--repeat-description ()`
- L794: `(defun herdr--menu-children (_)`
- L836: `(define-minor-mode herdr-mode`
- L850: `(provide 'herdr)`
