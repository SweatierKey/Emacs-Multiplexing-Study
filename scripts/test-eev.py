#!/usr/bin/env python3
from record import Session,ROOT
import json,traceback,re,sys
s=None;r={'id':'eev','scenario':'eepitch-two-ssh','status':'failed','checks':{},'snapshots':[]}
try:
 s=Session('eev',"(require 'eev-load) (eev-mode 1)")
 s.key(b'\x18\x06','C-x C-f');s.command(str(ROOT/'lab/eev-demo.e'));s.key(b'\x1b<','M-<')
 for i in range(9):s.key(b'\x1b[19~','F8: eepitch line '+str(i+1),1.2)
 for buf,role in [('*shell*','web'),('*shell 2*','db')]:
  s.key(b'\x18b','C-x b');s.command(buf)
  snap=s.snapshot();r['snapshots'].append(snap)
  assert snap['vertico'] and snap['marginalia']
  assert re.search(r'^role='+role+r'\s*$',snap['text'],re.M)
  r['checks']['ssh_'+role]=True
  if role=='web':
   assert re.search(r'^web-session-alive\s*$',snap['text'],re.M);r['checks']['return_preserves_shell']=True
 r['status']='passed'
except Exception as e:
 r['error']=str(e);r['traceback']=traceback.format_exc()
 if s:
  try:r['snapshots'].append(s.snapshot());r['messages']=s.eval('(with-current-buffer "*Messages*" (buffer-string))')
  except Exception:pass
finally:
 if s:s.close()
 (ROOT/'results/eev.json').write_text(json.dumps(r,indent=2)+'\n');print(r['status'],r.get('error',''))
sys.exit(r['status']!='passed')
