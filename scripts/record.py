#!/usr/bin/env python3
"""PTY-based real Emacs recording (asciicast v2); input is sent as keyboard bytes.
Emacsclient is used only for assertions and snapshots, never to create demo output.
"""
import codecs,os,pty,fcntl,termios,struct,select,time,json,pathlib,subprocess,sys,signal,traceback
ROOT=pathlib.Path(__file__).resolve().parents[1]
class Session:
 def __init__(self,name,setup='',width=110,height=32,env_override=None):
  old=ROOT/'results'/(name+'.json')
  if old.exists():
   archive=ROOT/'results'/'attempts'/name/str(time.time_ns());archive.mkdir(parents=True)
   for f in [old,ROOT/'results'/(name+'-keys.json'),ROOT/'recordings'/(name+'.cast')]:
    if f.exists():f.rename(archive/f.name)
  self.name=name;self.wall_start=int(time.time());self.decoder=codecs.getincrementaldecoder("utf-8")("replace");self.start=time.monotonic();self.events=[];self.steps=[];self.width=width;self.height=height
  runtime=ROOT/'.runtime';runtime.mkdir(exist_ok=True)
  self.server=str(ROOT/'.runtime/sockets'/('study-'+name));self.spec=runtime/(name+'-setup.el');self.spec.write_text(setup)
  home=runtime/('home-'+name);home.mkdir(exist_ok=True)
  env=dict(os.environ,TERM='xterm-256color',HOME=str(home),LC_ALL='C.UTF-8',STUDY_SPEC=str(self.spec),STUDY_SERVER=self.server)
  xdg=runtime/('xdg-'+name);xdg.mkdir(exist_ok=True);xdg.chmod(0o700)
  env.update(XDG_RUNTIME_DIR=str(xdg),XDG_CONFIG_HOME=str(home/'.config'),XDG_CACHE_HOME=str(home/'.cache'),ZMX_DIR=str(xdg/'zmx'),TMUX_TMPDIR=str(xdg))
  env.pop('TMUX',None);env.pop('ZMX_SESSION',None)
  bindir=runtime/'bin';bindir.mkdir(exist_ok=True)
  (bindir/'lab-ssh').write_text('#!/bin/sh\nexec /usr/bin/ssh -F '+str(runtime/'ssh_config')+' "$@"\n');(bindir/'lab-ssh').chmod(0o755)
  env['PATH']=str(bindir)+':'+str(runtime/'sysroot/usr/bin')+':'+env['PATH']
  env['LD_LIBRARY_PATH']=str(runtime/'sysroot/usr/lib/x86_64-linux-gnu')
  if env_override:env.update(env_override)
  self.env=env
  pid,fd=pty.fork()
  if pid==0:
   os.chdir(ROOT);os.execvpe('emacs',['emacs','-Q','-nw','-l',str(ROOT/'config/init.el')],env)
  self.pid=pid;self.fd=fd
  fcntl.ioctl(fd,termios.TIOCSWINSZ,struct.pack('HHHH',height,width,0,0))
  self.pump(2)
  for _ in range(30):
   try:
    self.eval('(and vertico-mode marginalia-mode)');break
   except Exception:self.pump(.3)
  else:
   self.close();raise RuntimeError('Emacs server not ready; see recording for initialization error')
 def pump(self,seconds):
  deadline=time.monotonic()+seconds
  while time.monotonic()<deadline:
   r,_,_=select.select([self.fd],[],[],min(.05,max(0,deadline-time.monotonic())))
   if r:
    try:data=os.read(self.fd,65536)
    except OSError:return
    if not data:return
    self.events.append([round(time.monotonic()-self.start,4),'o',self.decoder.decode(data)])
 def key(self,data,label=None,wait=.4):
  if isinstance(data,str):data=data.encode()
  self.steps.append({'at':round(time.monotonic()-self.start,3),'keys':label or repr(data),'input_hex':data.hex()})
  self.events.append([round(time.monotonic()-self.start,4),'i',data.decode('utf-8',errors='replace')]);os.write(self.fd,data);self.pump(wait)
 def mx(self,command,prefix=False):
  if prefix:self.key(b'\x15','C-u')
  cooked=self.eval("(with-current-buffer (window-buffer (selected-window)) (derived-mode-p 'cooked-mode))")!='nil'
  self.key(b'\x03\x1bx' if cooked else b'\x1bx','C-c M-x' if cooked else 'M-x',.3);self.key(command,command,.5);self.key(b'\r','RET',.8)
 def command(self,command,wait=.8):
  self.key(command,command,.2);self.key(b'\r','RET',wait)
 def eval(self,form):
  p=subprocess.run(['emacsclient','-s',self.server,'--eval',form],env=self.env,text=True,capture_output=True,timeout=8)
  if p.returncode:raise RuntimeError(p.stderr)
  return p.stdout.strip()
 def snapshot(self):
  # selected-window remains the human's window even during emacsclient evaluation.
  form='(with-current-buffer (window-buffer (selected-window)) (json-encode `((name . ,(buffer-name)) (mode . ,(symbol-name major-mode)) (vertico . ,(if vertico-mode t :json-false)) (marginalia . ,(if marginalia-mode t :json-false)) (text . ,(buffer-substring-no-properties (point-min) (point-max))))))'
  return json.loads(json.loads(self.eval(form)))
 def close(self):
  try:self.eval('(kill-emacs)')
  except Exception:pass
  self.pump(.2)
  try:os.kill(self.pid,signal.SIGTERM)
  except ProcessLookupError:pass
  try:os.waitpid(self.pid,0)
  except ChildProcessError:pass
  os.close(self.fd)
  header={'version':2,'width':self.width,'height':self.height,'timestamp':self.wall_start,'title':self.name+' — real Emacs / Vertico / Marginalia','env':{'TERM':'xterm-256color','SHELL':'/bin/bash'}}
  (ROOT/'recordings'/(self.name+'.cast')).write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in [header]+self.events)+'\n')
  (ROOT/'results'/(self.name+'-keys.json')).write_text(json.dumps(self.steps,indent=2)+'\n')
if __name__=='__main__':
 s=Session('smoke',"(require 'term)")
 try:
  s.mx('ansi-term');s.key(b'\r','accept default shell',1);s.command('lab-ssh lab-web',1);s.command('cat status.txt; tail -n 3 service.log');print(s.snapshot())
 finally:s.close()
