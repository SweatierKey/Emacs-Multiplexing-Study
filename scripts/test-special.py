#!/usr/bin/env python3
"""Native multiplexer workflows including server persistence after Emacs exits."""
from record import Session,ROOT
from importlib.machinery import SourceFileLoader
import subprocess,json,re,sys,traceback,os,time
common=SourceFileLoader('scenarios_runner',str(ROOT/'scripts/test-scenarios.py')).load_module()

def save(name,result,s):
 if s:
  try:result.setdefault('snapshots',[]).append(s.snapshot())
  except Exception:pass
  s.close()
 (ROOT/'results'/(name+'.json')).write_text(json.dumps(dict(id=name,**result),indent=2)+'\n')
 print(name,result['status'],result.get('error','')[:160],flush=True)

def tmux_demo(kind):
 name=kind;s=None;r={'scenario':'tmux-two-ssh-and-persistence','status':'failed','checks':{},'snapshots':[]};sock='ems-'+kind
 feature={'tmux-nested':'vterm','tmux-control':'tmux-control','tmux-control-mode':'tmux-cc'}[kind]
 setup=f"(let ((p (expand-file-name \"sources/{kind}\" study-root))) (setq load-path (cons p (delete p load-path))))\n(require '{feature})"
 env=None
 try:
  s=Session(name,setup);env=s.env
  subprocess.run(['tmux','-L',sock,'kill-server'],env=env,capture_output=True)
  if kind=='tmux-nested':
   s.mx('vterm');s.command(f'tmux -L {sock} -f /dev/null new-session -s ops',1)
  elif kind=='tmux-control':
   s.mx('tmux-control-connect');s.command('');s.command(sock);s.command('ops',1.5)
  else:
   s.mx('tmux-cc-start');s.key(b'\x01\x0b','C-a C-k');s.command(f'tmux -L {sock} -f /dev/null -CC new-session -A -s ops',1.5)
  
  if kind=='tmux-control-mode':s.key(b'\x1b<\x13%0\r\r','M-< C-s %0 RET RET: visit first pane',1)
  r['snapshots'].append(common.check_role(s,'web'));r['checks']['ssh_web']=True
  s.command('export STUDY_KEEP=web-session-alive')
  if kind=='tmux-nested':s.key(b'\x02c','C-b c: tmux new-window',1)
  elif kind=='tmux-control':s.mx('tmux-control-new-window');s.command('db',1)
  else:s.key(b'\x14c','C-t c: tmux-cc new-window',1);s.command('db',1)
  r['snapshots'].append(common.check_role(s,'db'));r['checks']['ssh_db']=True
  if kind=='tmux-nested':s.key(b'\x02p','C-b p: tmux previous-window',1)
  elif kind=='tmux-control':s.key(b'\x03\x10','C-c C-p: previous-window',1)
  else:
   s.mx('tmux-cc-switch-window');s.command('ops:ssh',1)
   s.key(b'\x18b','C-x b: select rendered pane');s.command('tmux-pane %0',1)
  s.command('printenv STUDY_KEEP');snap=s.snapshot();r['snapshots'].append(snap)
  assert re.search(r'^web-session-alive\s*$',snap['text'],re.M)
  r['checks']['return_preserves_shell']=True
  s.close();s=None
  p=subprocess.run(['tmux','-L',sock,'has-session','-t','ops'],env=env,capture_output=True)
  assert p.returncode==0,'Session did not survive Emacs exit'
  r['checks']['survives_emacs_exit']=True
  s=Session(name+'-resume',setup,env_override={'TMUX_TMPDIR':env['TMUX_TMPDIR']})
  if kind=='tmux-nested':s.mx('vterm');s.command(f'tmux -L {sock} attach -t ops',1)
  elif kind=='tmux-control':s.mx('tmux-control-connect');s.command('');s.command(sock);s.command('ops',1.5)
  else:s.mx('tmux-cc-start');s.key(b'\x01\x0b','C-a C-k');s.command(f'tmux -L {sock} -CC attach -t ops',1.5)
  if kind=='tmux-control-mode':s.key(b'\x1b<\x13%0\r\r','M-< C-s %0 RET RET: visit first pane',1)
  s.command('printenv STUDY_KEEP');snap=s.snapshot();r['snapshots'].append(snap)
  assert re.search(r'^web-session-alive\s*$',snap['text'],re.M),'State lost on reconnect'
  r['checks']['restart_reconnect']=True;r['status']='passed';r['resume_recording']=name+'-resume.cast'
 except Exception as e:
  r['error']=str(e);r['traceback']=traceback.format_exc()
  if s:
   try:r['messages']=s.eval('(with-current-buffer "*Messages*" (buffer-string))')
   except Exception:pass
 finally:
  save(name,r,s)
  if env:subprocess.run(['tmux','-L',sock,'kill-server'],env=env,capture_output=True)

def workspace(name):
 features={'tab-bar':"(tab-bar-mode 1)",'elscreen':"(require 'elscreen) (elscreen-start)",'eyebrowse':"(require 'eyebrowse) (eyebrowse-mode 1)"}
 s=None;r={'scenario':'workspace-two-ssh','status':'failed','checks':{},'snapshots':[]}
 try:
  s=Session(name,"(require 'term) "+features[name]);s.mx('ansi-term');s.command('')
  first=common.check_role(s,'web');r['snapshots'].append(first);r['checks']['ssh_web']=True;s.command('export STUDY_KEEP=web-session-alive')
  common.emacs_keys(s)
  if name=='tab-bar':s.key(b'\x18t2','C-x t 2: new tab')
  elif name=='elscreen':s.key(b'\x1ac','C-z c: create screen')
  else:s.mx('eyebrowse-switch-to-window-config-2')
  s.mx('ansi-term');s.command('');second=common.check_role(s,'db');r['snapshots'].append(second);r['checks']['ssh_db']=True
  common.emacs_keys(s)
  if name=='tab-bar':s.key(b'\x18tO','C-x t O: previous tab')
  elif name=='elscreen':s.key(b'\x1ap','C-z p: previous screen')
  else:s.mx('eyebrowse-switch-to-window-config-1')
  assert s.snapshot()['name']==first['name']
  common.input_mode(s);s.command('printenv STUDY_KEEP');snap=s.snapshot();r['snapshots'].append(snap)
  assert re.search(r'^web-session-alive\s*$',snap['text'],re.M)
  r['checks']['layout_restores_shell']=True;r['status']='passed'
 except Exception as e:r['error']=str(e);r['traceback']=traceback.format_exc()
 finally:save(name,r,s)
if __name__=='__main__':
 for name in sys.argv[1:]:
  if name in ['tab-bar','elscreen','eyebrowse']:workspace(name)
  else:tmux_demo(name)

 if any(json.loads((ROOT/"results"/(n+".json")).read_text())["status"]!="passed" for n in sys.argv[1:]):sys.exit(1)
