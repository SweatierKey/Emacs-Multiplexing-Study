# Indice del codice: tiling

Fonte: https://github.com/lgfang/tiling.git

Revisione: `95c8cf543214eda33202a417a4ef7bb5095991c0`.


## tiling.el

- L38: `;; (define-key global-map (kbd "C-\\") 'tiling-cycle) ; accepts prefix number`
- L39: `;; (define-key global-map (kbd "C-M-<up>") 'tiling-tile-up)`
- L40: `;; (define-key global-map (kbd "C-M-<down>") 'tiling-tile-down)`
- L41: `;; (define-key global-map (kbd "C-M-<right>") 'tiling-tile-right)`
- L42: `;; (define-key global-map (kbd "C-M-<left>") 'tiling-tile-left)`
- L63: `(defun tiling-tile-4 (bufs)`
- L85: `(defun tiling-master(bufs horizontal)`
- L108: `(defun tiling-master-left(bufs)`
- L113: `(defun tiling-master-top(bufs)`
- L119: `(defun tiling-even (bufs horizontal)`
- L137: `(defun tiling-even-horizontal (bufs) (tiling-even bufs t))`
- L139: `(defun tiling-even-vertical (bufs) (tiling-even bufs nil))`
- L142: `(defun tiling-cycle (&optional numOfWins)`
- L182: `(defun tiling-tile-move (direction)`
- L197: `(defun tiling-tile-up () (interactive) (tiling-tile-move 'up))`
- L199: `(defun tiling-tile-down () (interactive) (tiling-tile-move 'down))`
- L201: `(defun tiling-tile-left () (interactive) (tiling-tile-move 'left))`
- L203: `(defun tiling-tile-right () (interactive) (tiling-tile-move 'right))`
- L205: `(provide 'tiling)`
