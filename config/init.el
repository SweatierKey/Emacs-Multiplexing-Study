;;; init.el --- Isolated study configuration -*- lexical-binding: t; -*-
(setq package-enable-at-startup nil)
(defconst study-root (file-name-directory (directory-file-name (file-name-directory load-file-name))))
(setq user-emacs-directory (expand-file-name ".runtime/emacs/" study-root))
(make-directory user-emacs-directory t)
(setq inhibit-startup-screen t initial-scratch-message nil
      create-lockfiles nil make-backup-files nil auto-save-default nil
      confirm-kill-processes nil ring-bell-function #'ignore)
;; Load paths, never a user's configuration or package cache.
(let ((default-directory (expand-file-name "sources/" study-root)))
  (normal-top-level-add-subdirs-to-load-path))
(dolist (dir '("compat" "vertico" "marginalia" "ghostel/lisp" "cooked/lisp" "kuro/emacs-lisp/core" "circe/lisp"))
  (let ((path (expand-file-name (concat "sources/" dir) study-root)))
    (setq load-path (cons path (delete path load-path)))))
(require 'json)
(require 'vertico)
(require 'marginalia)
(vertico-mode 1)
(marginalia-mode 1)
(setq shell-file-name (expand-file-name "lab/bash" study-root)
      explicit-shell-file-name shell-file-name
      explicit-bash-args '("--noprofile" "--norc")
      vterm-shell shell-file-name
      alacritty-shell shell-file-name
      ghostel-shell shell-file-name
      multi-term-program shell-file-name
      ghostel-module-directory (expand-file-name "native/" study-root)
      ghostel-module-auto-install nil
      alacritty-module-path (expand-file-name "native/libalacritty_emacs.so" study-root)
      cooked-native-module (expand-file-name "native/libcooked.so" study-root)
      kuro-module-binary-path (expand-file-name "native/libkuro_core.so" study-root))
(add-to-list 'load-path (expand-file-name "native/" study-root))
(setenv "SHELL" shell-file-name)
(setenv "PS1" "local@lab:\\w\\$ ")
(setenv "HISTFILE" "/dev/null")
(setenv "PROMPT_COMMAND" "")
(setq default-directory study-root)
;; No global or package keymap remapping. M-x uses actual Vertico/Marginalia.
(when (getenv "STUDY_SPEC") (load (getenv "STUDY_SPEC") nil t))
(require 'server)
(setq server-socket-dir (expand-file-name ".runtime/sockets/" study-root))
(make-directory server-socket-dir t)
(set-file-modes server-socket-dir #o700)
(setq server-name (file-name-nondirectory (or (getenv "STUDY_SERVER") "emacs-study")))
(unless noninteractive (server-start))
