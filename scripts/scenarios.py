"""Declarative launch steps; all actions are public commands/default keys.
A prefix or a prompt answer is explicit. No package keymaps are modified.
"""
def spec(feature,launch=None,second=None,answers=None,prefix=False,setup='',back=None,tui=True):
 return dict(feature=feature,launch=launch or feature,second=second or launch or feature,answers=answers or [],prefix=prefix,setup=setup,back=back,tui=tui)
SCENARIOS={
 'ansi-term':spec('term','ansi-term',answers=['']),
 'term':spec('term',answers=[''],second='ansi-term'),
 'shell':spec('shell',prefix=True,answers=[],tui=False),
 'eshell':spec('eshell',prefix=True,tui=False),
 'eat':spec('eat',prefix=True),
 'vterm':spec('vterm',prefix=True),
 'ghostel':spec('ghostel',prefix=True),
 'mistty':spec('mistty',prefix=True),
 'el-be-back':spec('ebb',prefix=True),
 'alacritty':spec('alacritty'),
 'kuro':spec('kuro','kuro-create',answers=['']),
 'cooked':spec('cooked',prefix=True),
 'coterm':spec('coterm','shell',prefix=True,setup='(coterm-mode 1)'),
 'multi-term':spec('multi-term',back='multi-term-prev'),
 'multi-vterm':spec('multi-vterm',back='multi-vterm-prev'),
 'multi-buf':spec('multi-buf','multi-buf-vterm-dwim',prefix=True,back='multi-buf-vterm-dwim',setup="(require 'vterm)"),
 'vtplex':spec('vtplex','vtplex-create',back='vtplex-prev'),
 'ghostel-mux':spec('ghostel-mux',second='ghostel-mux-new-window',back='ghostel-mux-previous-window'),
 'vterm-toggle':spec('vterm-toggle',second='vterm',prefix=True,back='vterm-toggle-backward'),
 'shell-pop':spec('shell-pop',second='shell-pop',prefix=True,tui=False),
 'eshell-toggle':spec('eshell-toggle',second='eshell',prefix=True,tui=False),
 'aweshell':spec('aweshell','aweshell-new',back='aweshell-prev',tui=False),
 'term-mux':spec('term-mux','term-mux-create',back='term-mux-prev'),
 'terminal-here':spec('terminal-here','terminal-here'),
 'shell-here':spec('shell-here',tui=False),
 'terminal-toggle':spec('terminal-toggle',second='ansi-term',setup='(setq terminal-toggle--term-shell shell-file-name)'),
 'project-terminal':spec('project-terminal','project-terminal-add',tui=False),
 'vterms':spec('vterms','vterms-project-vterm',prefix=True),
 'vterm-ring':spec('vterm-ring','vterm-ring-new'),
 'vterm-manager':spec('vtm','vtm-mode'),
 'multi-shell':spec('multi-shell','multi-shell-new',tui=False),
 'multi-eshell':spec('multi-eshell','multi-eshell',tui=False),
 'shell-switcher':spec('shell-switcher','shell-switcher-new-shell',tui=False),
 'better-shell':spec('better-shell','better-shell-shell',tui=False),
 'friendly-shell':spec('friendly-shell',tui=False),
 'sticky-shell':spec('sticky-shell','shell',prefix=True,setup="(add-hook 'shell-mode-hook #'sticky-shell-mode)",tui=False),
 'toggle-term':spec('toggle-term','toggle-term-shell',tui=False),
 'tramp-term':spec('tramp-term','tramp-term'),
 'popterm':spec('popterm','popterm-toggle',prefix=True),
 'bshell':spec('bshell'),
}

SCENARIOS.update({
 'lterm':spec('lterm',answers=[''],tui=False),
 'term-manager':spec('term-project','term-project-default-directory-create-new',back='term-project-default-directory-backward'),
 'ghostel-switch':spec('ghostel-switch','ghostel-switch-all',answers=['']),
 'term-control':spec('term-control','term-control-switch-to-term',answers=['web']),
 'term-plus-mux':spec('term+mux','term+mux-new'),
 'elscreen-multi-term':spec('elscreen-multi-term','emt-multi-term',setup='(elscreen-start)'),
 'emux-el':spec('emux','emux:term-new'),
})
SCENARIOS['ghostel-mux']['second_key']='\x02c'
SCENARIOS['ghostel-mux']['back_key']='\x02p'
SCENARIOS['vtplex']['second_key']='\x01c'
SCENARIOS['vtplex']['back_key']='\x01p'

SCENARIOS['vterm-toggle']['setup']="(require 'vterm)"
SCENARIOS['better-shell'].update(second='shell',prefix=True,back='better-shell-shell')
SCENARIOS['shell-here'].update(second='shell',prefix=True)
SCENARIOS['toggle-term'].update(launch='toggle-term-find',second='toggle-term-find',answers=['web','bottom','shell'],answers2=['db','bottom','shell'])
SCENARIOS['popterm'].update(launch='popterm-toggle-named',second='popterm-toggle-named',answers=['web'],answers2=['db'],prefix=False,before_second=['popterm-toggle'],setup="(require 'vterm) (setq popterm-display-method 'window)")
SCENARIOS['ghostel-switch'].update(answers=['@empty'],setup="(require 'ghostel)")
SCENARIOS['terminal-toggle'].update(answers2=[''])
SCENARIOS['sticky-shell'].update(second='shell',prefix=True)
SCENARIOS['shell-switcher'].update(back='shell-switcher-switch-buffer')
SCENARIOS['term-run']=spec('term-run','term-run-shell-command',answers=['/bin/bash --noprofile --norc'],prefix=True)
SCENARIOS['navorski']=spec('navorski','nav/term')
SCENARIOS['term+']=spec('term+','ansi-term',answers=[''])
SCENARIOS['eterm-256color']=spec('eterm-256color','ansi-term',answers=[''],setup="(add-hook 'term-mode-hook #'eterm-256color-mode)")
SCENARIOS['eshell-vterm']=spec('eshell-vterm','eshell',prefix=True,setup="(require 'vterm) (eshell-vterm-mode 1)",tui=False)
SCENARIOS['eat-eshell']=spec('eat','eshell',prefix=True,setup="(eat-eshell-mode 1)",tui=False)

SCENARIOS['term-sessions']=spec('term-sessions','term-sessions-open',answers=['web'])
SCENARIOS['term-sessions'].update(answers2=['db'])

SCENARIOS['term-run']['after_launch_key']='\x18o'
SCENARIOS['multi-buffer']=spec('multi-buffer','eat',setup="(require 'eat) (add-hook 'eat-mode-hook #'multi-buffer-mode)")
SCENARIOS['term-toggle']=spec('term-toggle','term-toggle-ansi',second='ansi-term')
SCENARIOS['term-toggle'].update(answers2=[''])
SCENARIOS['vtermux']=spec('vtermux','study-bash',setup='(require \'vterm) (vtermux-define study-bash :program "bash" :args "--noprofile --norc")')
SCENARIOS['vtermux'].update(answers2=['db'])

SCENARIOS['multi-buffer'].update(feature='eat',setup="(load (expand-file-name \"sources/multi-buffer/multi-buffer.el\" study-root)) (add-hook 'eat-mode-hook #'multi-buffer-mode)")
from pathlib import Path
_STUDY_ROOT=Path(__file__).resolve().parents[1]
SCENARIOS['vterm-manager']=spec('vtm','find-file',answers=[str(_STUDY_ROOT/'lab/vtm/web.vtm')])
SCENARIOS['vterm-manager'].update(answers2=[str(_STUDY_ROOT/'lab/vtm/db.vtm')])
SCENARIOS['eterm-256color']['setup']+=" (setenv \"TERMINFO_DIRS\" (concat (expand-file-name \".runtime/terminfo\" study-root) \":/usr/share/terminfo:/lib/terminfo\"))"
SCENARIOS['term+']['setup']="(require 'term+key-intercept)"
SCENARIOS['term-plus-mux']['setup']="(require 'term+key-intercept)"
SCENARIOS['emux']=spec('emux-term','emux-term-create')

SCENARIOS['terminal']=spec('terminal','terminal-emulator',answers=[''],tui=False)
