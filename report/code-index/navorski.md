# Indice del codice: navorski

Fonte: https://github.com/roman/navorski.el.git

Revisione: `698c1c62da70164aebe9a7a5d034778fbc30ea5b`.


## navorski.el

- L27: `(require 'time-stamp)`
- L28: `(require 'multi-term)`
- L29: `(require 'assoc)`
- L30: `(require 'dash)`
- L40: `(defcustom navorski-buffer-name "terminal"`
- L45: `(defcustom navorski-verbose nil`
- L50: `(defvar navorski-profile-map (make-hash-table :test 'equal)`
- L53: `(defvar navorski-read-only-term-map (suppress-keymap (make-sparse-keymap))`
- L62: `(defun -navorski-term-reverse-search ()`
- L68: `(defun -navorski-term-dabbrev ()`
- L75: `(defun -navorski-term-backward-kill-word ()`
- L81: `(defun -navorski-insert-path (file)`
- L86: `(defun -navorski-term-insert-path ()`
- L93: `(defun -navorski-term-yank ()`
- L99: `(defun -navorski-interrupt-process ()`
- L160: `(defun -navorski-merge-alist (a1 a2)`
- L169: `(defun -navorski-profile-setting-to-list (setting)`
- L178: `(defun -navorski-put-profile (profile-name profile)`
- L181: `(defun -navorski-get-profile (profile-name)`
- L189: `(defun -navorski-profile-get (profile key &optional def)`
- L195: `(defun -navorski-profile-set (profile0 key val)`
- L204: `(defun -navorski-profile-modify (profile key f)`
- L212: `(defun -navorski-get-kill-buffer-on-stop (profile)`
- L215: `(defun -navorski-get-profile-name (profile)`
- L218: `(defun -navorski-get-interactive (profile)`
- L221: `(defun -navorski-get-shell-path (profile)`
- L230: `(defun -navorski-indexed-buffer-name (buffer-name &optional current-index)`
- L237: `(defun -navorski-get-unnamed-terminal-count ()`
- L241: `(defun -navorski-next-buffer-name (&optional buffer-name)`
- L247: `(defun -navorski-get-buffer-name (profile)`
- L258: `(defun -navorski-get-default-directory (profile)`
- L264: `(defun -navorski-get-init-script (profile)`
- L268: `(defun -navorski-get-read-only (profile)`
- L271: `(defun -navorski-get-program-args (profile)`
- L275: `(defun -navorski-get-hostname (profile)`
- L284: `(defun -navorski-decorate-multi-term-sentinel (profile term-buffer)`
- L301: `(defun -navorski-decorate-multi-term-process-filter (profile term-buffer)`
- L315: `(defun -navorski-read-only-term-mode ()`
- L321: `(defun -navorski-create-term-buffer (profile)`
- L358: `(defun -navorski-get-raw-buffer (profile)`
- L368: `(defun -navorski-get-buffer (profile0)`
- L384: `(defun -navorski-remote-term-setup-tramp-string (&optional remote-host)`
- L425: `(defun -navorski-remote-term-setup-program-args (profile)`
- L441: `(defun -navorski-remote-term-setup-tramp (profile)`
- L453: `(defun -navorski-remote-term-setup-remote-host (profile)`
- L463: `(defun -navorski-remote-term-setup-buffer-name (profile)`
- L471: `(defun -navorski-remote-term-to-local-term (profile)`
- L482: `(defun -navorski-persistent-term-setup-session-name (profile)`
- L492: `(defun -navorski-persistent-term-setup-program-args (profile)`
- L505: `(defun -navorski-persistent-term-to-local-term (profile)`
- L514: `(defun nav/pop-to-buffer (profile)`
- L517: `(defun nav/kill-buffer (profile &optional kill-process)`
- L524: `(defun nav/send-string (profile str)`
- L529: `(defun nav/send-region (profile start end)`
- L535: `(defmacro -navorski-def-interactive (profile-name profile)`
- L570: `(defmacro nav/defterminal (profile-name &rest args)`
- L705: `(defun nav/term (&optional profile)`
- L711: `(defun nav/remote-term (&optional remote-profile)`
- L721: `(defun nav/persistent-term (&optional profile)`
- L731: `(defun nav/remote-persistent-term (&optional profile)`
- L743: `(defun nav/setup-tramp ()`
- L752: `(defun nav/tramp-to-term ()`
- L763: `(provide 'navorski)`
