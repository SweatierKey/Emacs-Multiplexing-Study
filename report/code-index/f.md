# Indice del codice: f

Fonte: https://github.com/rejeep/f.el.git

Revisione: `931b6d0667fe03e7bf1c6c282d6d8d7006143c52`.


## .dir-locals.el


## bin/docs.el

- L15: `(require 'f f-lib-file)`

## f-shortdoc.el

- L436: `(provide 'f-shortdoc)`

## f.el

- L41: `(require 's)`
- L42: `(require 'dash)`
- L55: `(defmacro f--destructive (path &rest body)`
- L71: `(defun f-join (&rest args)`
- L90: `(defun f-split (path)`
- L97: `(defun f-expand (path &optional dir)`
- L106: `(defun f-filename (path)`
- L112: `(defun f-dirname (path)`
- L121: `(defun f-common-parent (paths)`
- L145: `(defun f-swap-ext (path ext)`
- L152: `(defun f-base (path)`
- L161: `(defun f-long (path)`
- L167: `(defun f-slash (path)`
- L176: `(defun f-full (path)`
- L180: `(defun f--uniquify (paths)`
- L202: `(defun f-uniquify (files)`
- L208: `(defun f-uniquify-alist (files)`
- L218: `(defun f-read-bytes (path &optional beg end)`
- L231: `(defun f-read-text (path &optional coding)`
- L240: `(defun f-write-text (text coding path)`
- L247: `(defun f-unibyte-string-p (s)`
- L251: `(defun f-write-bytes (data path)`
- L258: `(defun f-append-text (text coding path)`
- L264: `(defun f-append-bytes (data path)`
- L270: `(defun f--write-bytes (data filename append)`
- L286: `(defun f-mkdir (&rest dirs)`
- L306: `(defun f-mkdir-full-path (dir)`
- L313: `(defun f-delete (path &optional force)`
- L322: `(defun f-symlink (source path)`
- L326: `(defun f-move (from to)`
- L331: `(defun f-copy (from to)`
- L351: `(defun f-copy-contents (from to)`
- L360: `(defun f-touch (path)`
- L383: `(defun f-symlink-p (path)`
- L401: `(defun f-relative-p (path)`
- L407: `(defun f-root-p (path)`
- L413: `(defun f-ext-p (path &optional ext)`
- L430: `(defun f-same-p (path-a path-b)`
- L438: `(defun f-parent-of-p (path-a path-b)`
- L445: `(defun f-child-of-p (path-a path-b)`
- L452: `(defun f-ancestor-of-p (path-a path-b)`
- L460: `(defun f-descendant-of-p (path-a path-b)`
- L475: `(defun f-hidden-p (path &optional behavior)`
- L509: `(defun f-empty-p (path)`
- L522: `(defun f-size (path)`
- L531: `(defun f-depth (path)`
- L543: `(defun f--get-time (path timestamp-p fn)`
- L578: `(defun f-change-time (path &optional timestamp-p)`
- L590: `(defun f-modification-time (path &optional timestamp-p)`
- L601: `(defun f-access-time (path &optional timestamp-p)`
- L612: `(defun f--three-way-compare (a b)`
- L623: `(defun f--date-compare (file other method)`
- L650: `(defun f-older-p (file other &optional method)`
- L658: `(defun f-newer-p (file other &optional method)`
- L666: `(defun f-same-time-p (file other &optional method)`
- L678: `(defun f-this-file ()`
- L689: `(defun f-path-separator ()`
- L694: `(defun f-glob (pattern &optional path)`
- L699: `(defun f--collect-entries (path recursive)`
- L720: `(defmacro f--entries (path body &optional recursive)`
- L729: `(defun f-entries (path &optional fn recursive)`
- L738: `(defmacro f--directories (path body &optional recursive)`
- L747: `(defun f-directories (path &optional fn recursive)`
- L752: `(defmacro f--files (path body &optional recursive)`
- L761: `(defun f-files (path &optional fn recursive)`
- L766: `(defmacro f--traverse-upwards (body &optional path)`
- L774: `(defun f-traverse-upwards (fn &optional path)`
- L789: `(defun f-root ()`
- L793: `(defmacro f-with-sandbox (path-or-paths &rest body)`
- L804: `(provide 'f)`
