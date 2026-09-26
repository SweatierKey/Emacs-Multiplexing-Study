#!/usr/bin/env python3
"""Check archive integrity when present, evidence consistency, links and casts."""
import pathlib,json,hashlib,sys,urllib.parse,html.parser
R=pathlib.Path(__file__).resolve().parents[1];errors=[];checked=0
for w in (R/'wheels').glob('*.whl'):sys.path.insert(0,str(w))
try:import pyte
except ImportError:pyte=None
for p in (R/'recordings').glob('*.cast'):
 rows=[json.loads(l) for l in p.read_text().splitlines()];h=rows[0]
 assert h['version']==2 and h['width']>0 and h['height']>0
 last=0
 screen=pyte.Screen(h['width'],h['height']) if pyte else None
 stream=pyte.Stream(screen) if screen else None;sample=''
 for t,kind,data in rows[1:]:
  if t<last:errors.append(str(p)+': non-monotonic event')
  last=t
  if stream and kind=='o':
   stream.feed(data)
   frame='\n'.join(screen.display)
   if 'role=web' in frame and 'web-session-alive' in frame:sample=frame
 if sample and p.stem in ['vterm','ghostel-mux','tmux-control','term-sessions-persistence-resume']:
  out=R/'results/rendered';out.mkdir(exist_ok=True);(out/(p.stem+'.txt')).write_text(sample)
 checked+=1
for p in (R/'results').glob('*.json'):
 if p.name=='verification.json':continue
 r=json.loads(p.read_text())
 if not isinstance(r,dict) or r.get('status')!='passed' or 'id' not in r:continue
 if not (R/'recordings'/(r['id']+'.cast')).exists():errors.append(r['id']+': passed without recording')
 if any(v is not True for v in r.get('checks',{}).values()):errors.append(r['id']+': passed with false check')
 for s in r.get('snapshots',[]):
  if not (s.get('vertico') is True and s.get('marginalia') is True):errors.append(r['id']+': missing required modes')
class Links(html.parser.HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['href','src'] and v:
    u=urllib.parse.urlparse(v)
    if not u.scheme and u.path:
     dest=self.path.parent/urllib.parse.unquote(u.path)
     if not dest.exists():errors.append(str(self.path.relative_to(R))+': broken link '+v)
for p in [R/'index.html',*(R/'report').rglob('*.html')]:
 parser=Links();parser.path=p;parser.feed(p.read_text())
manifest=R/'MANIFEST.sha256'
if manifest.exists():
 for l in manifest.read_text().splitlines():
  sha,name=l.split('  ',1);p=R/name
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha:errors.append('Hash mismatch: '+name)
print(json.dumps({'casts_checked':checked,'terminal_replay':bool(pyte),'errors':errors},indent=2))
sys.exit(bool(errors))
