#!/usr/bin/env python3
from record import Session,ROOT
from importlib.machinery import SourceFileLoader
import json,re,subprocess,traceback,sys
common=SourceFileLoader('common',str(ROOT/'scripts/test-scenarios.py')).load_module()
name='term-sessions-persistence';s=None;env=None;r={'id':name,'status':'failed','checks':{},'snapshots':[]}
zd=ROOT/'.runtime/zmx-persistence';zd.mkdir(exist_ok=True)
setup=f'''(require 'term-sessions)
(setenv "ZMX_DIR" "{zd}")
(setq term-sessions-default-command (expand-file-name "lab/bash" study-root))'''
try:
 s=Session(name,setup);env=dict(s.env,ZMX_DIR=str(zd))
 subprocess.run(['zmx','kill','ops'],env=env,capture_output=True)
 s.mx('term-sessions-open');s.command('ops',1)
 r['snapshots'].append(common.check_role(s,'web'));s.command('export STUDY_KEEP=web-session-alive')
 s.close();s=None
 p=subprocess.run(['zmx','list'],env=env,capture_output=True,text=True);r['zmx_list_after_exit']=p.stdout
 assert 'ops' in p.stdout,'No persistent session after Emacs exit'
 r['checks']['survives_emacs_exit']=True
 s=Session(name+'-resume',setup);s.mx('term-sessions-open');s.command('ops',1)
 s.command('printenv STUDY_KEEP');snap=s.snapshot();r['snapshots'].append(snap)
 assert snap['vertico'] and snap['marginalia']
 assert re.search(r'^web-session-alive\s*$',snap['text'],re.M)
 r['checks']['restart_reconnect']=True;r['status']='passed';r['resume_recording']=name+'-resume.cast'
except Exception as e:r['error']=str(e);r['traceback']=traceback.format_exc()
finally:
 if s:s.close()
 if env:subprocess.run(['zmx','kill','ops'],env=env,capture_output=True)
 (ROOT/'results'/(name+'.json')).write_text(json.dumps(r,indent=2)+'\n')
 print(r['status'],r.get('error',''))

sys.exit(r["status"]!="passed")
