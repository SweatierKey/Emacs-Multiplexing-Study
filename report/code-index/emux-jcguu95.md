# Indice del codice: emux-jcguu95

Fonte: https://github.com/jcguu95/emux.git

Revisione: `54ce53ea351db4d34e70cee6973214f116d8a659`.


## early-init.el

- L18: `(provide 'early-init)`

## init.el

- L5: `(require 'init-elpaca)                  ; NOTE Emacs' Package Manager`
- L6: `(require 'init-benchmark)               ; NOTE 平常沒必要時，把這個刪掉以增加 booting 效率。`
- L16: `(require 'init-core-profile)`

## lisp/init-benchmark.el

- L13: `(provide 'init-benchmark)`

## lisp/init-bindings.el

- L58: `(provide 'init-bindings)`

## lisp/init-clipboard.el

- L24: `(provide 'init-clipboard)`

## lisp/init-completion.el

- L36: `;; 例如：(global-set-key (kbd "C-c C-r") 'consult-recent-files)`
- L39: `(provide 'init-completion)`

## lisp/init-core-profile.el

- L6: `(require 'init-ui)`
- L7: `(require 'init-evil)`
- L8: `(require 'init-terminal)`
- L9: `(require 'init-bindings)`
- L10: `(require 'init-window)`
- L11: `(require 'init-completion)`
- L12: `(require 'init-clipboard)`
- L16: `(provide 'init-core-profile)`

## lisp/init-eat.el

- L18: `(provide 'init-eat)`

## lisp/init-elpaca.el

- L48: `(provide 'init-elpaca)`

## lisp/init-evil.el

- L20: `(provide 'init-evil)`

## lisp/init-extended-profile.el

- L44: `(provide 'init-extended-profile)`

## lisp/init-terminal.el

- L4: `(require 'init-vterm)`
- L6: `(provide 'init-terminal)`

## lisp/init-ui.el

- L22: `(defun my/toggle-scratch-buffer (&optional same-window-p)`
- L35: `(provide 'init-ui)`

## lisp/init-vterm.el

- L167: `(provide 'init-vterm)`

## lisp/init-window.el

- L17: `(provide 'init-window)`
