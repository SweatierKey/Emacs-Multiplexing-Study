#!/usr/bin/env python3
"""Controllers differ from emulators: pre-existing isolated tmux is an explicit fixture."""
from record import Session,ROOT
import subprocess,json,re,traceback,sys,time

def run(name):
 s=None;r={'id':name,'scenario':'external-tmux-controller','status':'failed','checks':{},'snapshots':[], 'fixture':'Two pre-existing tmux windows run actual lab SSH connections. For tmux-view only, status output is seeded before the read-only demonstration.'}
 try:
  s=Session(name,"(require '"+name+") (require 'vterm)");env=s.env
  def tm(*args):return subprocess.run(['tmux',*args],env=env,capture_output=True,text=True,check=True).stdout
  tm('-f','/dev/null','new-session','-d','-s','ops','-n','web','lab-ssh lab-web');tm('set-option','-g','automatic-rename','off')
  tm('new-window','-t','ops','-n','db','lab-ssh lab-db');time.sleep(.5);tm('rename-window','-t','ops:0','web')
  r['checks']['completion_enabled']=s.eval('(and vertico-mode marginalia-mode)')=='t'
  for idx,role in enumerate(['web','db']):
   command='cat status.txt; tail -n 3 service.log'
   if name=='emamux':
    s.mx('emamux:send-command',prefix=bool(idx));s.command(str(idx)+': '+role);s.key(b'\x01\x0b','C-a C-k: clear previous command');s.command(command,1)
    captured=tm('capture-pane','-p','-t','ops:'+str(idx))
    assert re.search(r'^role='+role+r'\s*$',captured,re.M),captured
    r['checks']['remote_'+role+'_command_executed']=True
    # Display output through a genuine terminal; the controller itself does not render it.
    s.mx('vterm',prefix=bool(idx));s.command('tmux attach -t ops:'+str(idx),1)
    snap=s.snapshot();r['snapshots'].append(snap)
    assert 'role='+role in snap['text']
    s.key(b'\x02d','C-b d: detach tmux to return to controller',.8)
   else:
    tm('send-keys','-t','ops:'+str(idx),command,'Enter');time.sleep(.4)
    s.mx('tmux-view');s.command('ops/'+role+'/0:',1)
    snap=s.snapshot();r['snapshots'].append(snap)
    assert re.search(r'^role='+role+r'\s*$',snap['text'],re.M),snap
    r['checks']['remote_'+role+'_capture_visible']=True
  r['status']='passed'
 except Exception as e:
  r['error']=str(e);r['traceback']=traceback.format_exc()
  if s:
   try:r['snapshots'].append(s.snapshot());r['messages']=s.eval('(with-current-buffer "*Messages*" (buffer-string))')
   except Exception:pass
 finally:
  if s:
   s.close();subprocess.run(['tmux','kill-server'],env=s.env,capture_output=True)
  (ROOT/'results'/(name+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(name,r['status'],r.get('error','')[:160],flush=True)
 return r['status']=='passed'
if __name__=='__main__':sys.exit(not all([run(n) for n in sys.argv[1:]]))
