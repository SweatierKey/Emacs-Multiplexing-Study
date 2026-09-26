#!/usr/bin/env python3
"""End-to-end sysadmin scenario. Exit nonzero when any selected scenario fails.
The verdict requires observed output in two distinct live terminal buffers,
not merely a successful package load or the presence of typed commands.
"""
from record import Session, ROOT
from scenarios import SCENARIOS
import sys,json,re,traceback,time,pathlib,subprocess

def selected(s,form):return s.eval('(with-current-buffer (window-buffer (selected-window)) '+form+')')
def emacs_keys(s):
 if selected(s,"(and (derived-mode-p 'term-mode) (bound-and-true-p term+char-mode))")=='t':
  s.key(b'\x1b\r','M-RET: term+ edit mode');return
 if s.snapshot()['mode']=='terminal-mode':
  s.key(b'\x1eb','C-^ b: leave historical emulator');s.command('*scratch*');return
 if selected(s,'(and (derived-mode-p \'term-mode) (term-in-char-mode))')=='t':s.key(b'\x03\x0a','C-c C-j: term line mode')
def input_mode(s):
 if selected(s,"(and (derived-mode-p 'term-mode) (bound-and-true-p term+line-mode))")=='t':
  s.key(b'\x1b\r','M-RET: term+ char mode');return
 if selected(s,"(and (derived-mode-p 'term-mode) (not (term-in-char-mode)))")=='t':s.key(b'\x03\x0b','C-c C-k: term char mode')
def launch(s,sp,second=False):
 if second and sp.get('second_key'):s.key(sp['second_key'],'native create key',1)
 else:
  emacs_keys(s);s.mx(sp['second'] if second else sp['launch'],prefix=second and sp['prefix'])
 if second and sp['feature'] in ['shell','coterm','shell-here','sticky-shell']:s.key(b'\x01\x0b','C-a C-k');s.command('*shell-db*')
 else:
  for a in sp.get('answers2' if second else 'answers1',sp['answers']):
   if a=='@empty':s.key(b'\x1b\r','M-RET: accept empty input')
   else:s.command('db' if second and sp['feature']=='term-control' else a)
 s.pump(.5)
 if sp.get('after_launch_key'):s.key(sp['after_launch_key'],'C-x o: select displayed terminal')
 if s.snapshot()['mode'] in ['lisp-interaction-mode','minibuffer-mode']:raise AssertionError('Launch did not enter a terminal: '+str(s.snapshot()))

def check_role(s,role):
 input_mode(s);s.command('lab-ssh lab-'+role,1)
 s.command('cat status.txt; tail -n 3 service.log',1)
 snap=s.snapshot()
 if not re.search(r'^role='+role+r'\s*$',snap['text'],re.M):raise AssertionError('Missing actual remote role output: '+snap['text'][-1500:])
 if not re.search(r'^WARN '+role+r' disk threshold=75\s*$',snap['text'],re.M):raise AssertionError('Missing fixture log')
 return snap

def run(name):
 sp=SCENARIOS[name];s=None;result={'id':name,'status':'running','scenario':'two-ssh-endpoints','started':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'snapshots':[],'checks':{}}
 setup=f"(let ((p (expand-file-name \"sources/{name}\" study-root))) (setq load-path (cons p (delete p load-path))))\n(require '{sp['feature']})\n"+sp['setup']
 try:
  s=Session(name,setup)
  result['checks']['completion_enabled']=s.eval('(and vertico-mode marginalia-mode)')=='t'
  assert result['checks']['completion_enabled'], 'Required completion modes disabled'
  launch(s,sp);first=check_role(s,'web');result['snapshots'].append(first);result['checks']['ssh_web']=True
  # Keep a variable in the remote shell; later output must prove it survived switching.
  s.command('export STUDY_KEEP=web-session-alive')
  for cmd in sp.get('before_second',[]):
   emacs_keys(s);s.mx(cmd)
  launch(s,sp,True);second=check_role(s,'db');result['snapshots'].append(second);result['checks']['ssh_db']=True
  assert first['name']!=second['name'],'Second launch reused the first buffer'
  result['checks']['distinct_buffers']=True
  emacs_keys(s)
  if sp.get('back_key'):s.key(sp['back_key'],'native previous key',1)
  elif sp['back']:s.mx(sp['back'])
  else:
   s.key(b'\x18b','C-x b: switch-to-buffer');s.key(first['name'],first['name']);s.key(b'\r','RET')
  assert s.snapshot()['name']==first['name'],'Return command did not select first buffer'
  input_mode(s);s.command('printenv STUDY_KEEP',.7)
  snap=s.snapshot();result['snapshots'].append(snap)
  assert re.search(r'^web-session-alive\s*$',snap['text'],re.M),'Remote shell state not recovered'
  result['checks']['return_preserves_shell']=True
  if sp['tui']:
   s.command('less service.log',.7);snap=s.snapshot();result['snapshots'].append(snap)
   assert 'INFO web boot complete' in snap['text'],'Pager content not visible'
   s.key('q','q: leave less',.5);s.command("printf 'PAGER_%s\\n' RETURNED",.7)
   snap=s.snapshot();result['snapshots'].append(snap)
   assert re.search(r'^PAGER_RETURNED\s*$',snap['text'],re.M),'Pager did not return to shell'
   result['checks']['pager_roundtrip']=True
  result['status']='passed'
 except Exception as e:
  result['status']='failed';result['error']=str(e);result['traceback']=traceback.format_exc()
  if s:
   try:
    result['snapshots'].append(s.snapshot());result['messages']=s.eval('(with-current-buffer "*Messages*" (buffer-string))')
   except Exception:pass
 finally:
  if s:
   s.close()
   if name=='term-sessions':
    for target in ['web','db']:subprocess.run(['zmx','kill',target],env=s.env,capture_output=True)
 (ROOT/'results'/(name+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(name,result['status'],result.get('error','')[:180],flush=True)
 return result
if __name__=='__main__':
 names=sys.argv[1:] or list(SCENARIOS)
 rows=[run(n) for n in names]
 sys.exit(any(r['status']!='passed' for r in rows))
