#!/usr/bin/env python3
"""Prepare only private study paths. Debian 13 / x86_64; no package downloads."""
import pathlib,subprocess,tarfile,shutil,os,json
R=pathlib.Path(__file__).resolve().parents[1];rt=R/'.runtime';rt.mkdir(exist_ok=True)
for name in ['emacs','emacsclient','ssh','sshd','ssh-keygen','tic','cmake','gcc','make','tmux','less']:
 if not shutil.which(name) and not pathlib.Path('/usr/sbin/'+name).exists():raise SystemExit('Missing dependency: '+name+' (see report/REPRODUCE.md)')
for d in ['results','recordings','report','sources','native']:(R/d).mkdir(exist_ok=True)
assert (R/'sources/vertico/vertico.el').exists(),'Extract the full release archive first'
subprocess.run(['emacs','-Q','--batch','-L',str(R/'sources/compat'),'-f','batch-byte-compile',*map(str,(R/'sources/compat').glob('compat*.el'))],check=True)
subprocess.run(['cmake','-S',str(R/'sources/vterm'),'-B',str(rt/'build-vterm')],check=True)
subprocess.run(['cmake','--build',str(rt/'build-vterm'),'-j','2'],check=True)
terminfo=rt/'terminfo';terminfo.mkdir(exist_ok=True)
os.environ['TERMINFO_DIRS']=str(terminfo)+':/usr/share/terminfo:/lib/terminfo'
for root in ['term','eat','ghostel','cooked','el-be-back','eterm-256color']:
 for p in (R/'sources'/root).rglob('*'):
  if p.suffix in ['.ti','.terminfo']:
   subprocess.run(['tic','-x','-o',str(terminfo),str(p)],check=True)
bindir=rt/'bin';bindir.mkdir(exist_ok=True)
archive=R/'native/zmx-0.8.1-linux-x86_64.tar.gz'
with tarfile.open(archive) as t:
 for m in t:
  if pathlib.Path(m.name).name=='zmx' and m.isfile():
   tmp=bindir/'zmx.new';tmp.write_bytes(t.extractfile(m).read());tmp.chmod(0o755);tmp.replace(bindir/'zmx')
if (R/'native/herdr-linux-x86_64').exists():shutil.copy2(R/'native/herdr-linux-x86_64',bindir/'herdr.new');(bindir/'herdr.new').chmod(0o755);(bindir/'herdr.new').replace(bindir/'herdr')
for p in [R/'lab/bash',R/'lab/remote-shell.sh']:p.chmod(0o755)
# Record actual host versions; this does not pretend to pin an arbitrary host.
versions={}
for name,args in {'emacs':['--version'],'tmux':['-V'],'ssh':['-V'],'cmake':['--version'],'gcc':['--version'],'python3':['--version']}.items():
 p=subprocess.run([name]+args,capture_output=True,text=True);versions[name]=(p.stdout+p.stderr).splitlines()[0]
(R/'results/environment-current.json').write_text(json.dumps(versions,indent=2)+'\n')
print('Prepared. Run python3 scripts/lab.py start, then the selected tests.')
