#!/usr/bin/env python3
"""Run all recorded scenarios, keep negative outcomes; --smoke is the short path."""
import pathlib,subprocess,sys,json
R=pathlib.Path(__file__).resolve().parents[1]
smoke='--smoke' in sys.argv
names=['ansi-term','eat','vterm','multi-vterm','ghostel-mux'] if smoke else json.loads((R/'config/suite.json').read_text())['generic']
rc=0
try:
 subprocess.run([sys.executable,str(R/'scripts/lab.py'),'start'],check=True)
 for cmd in [ ['test-scenarios.py',*names],['test-special.py',*(['tmux-nested'] if smoke else ['tmux-nested','tmux-control','tmux-control-mode','tab-bar','elscreen','eyebrowse'])],*([] if smoke else [['test-zmx.py'],['test-eev.py'],['test-controllers.py','emamux','tmux-view']]) ]:
  p=subprocess.run([sys.executable,str(R/'scripts'/cmd[0]),*cmd[1:]],cwd=R);rc=max(rc,p.returncode)
finally:subprocess.run([sys.executable,str(R/'scripts/lab.py'),'stop'])
sys.exit(rc)
