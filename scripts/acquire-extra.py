#!/usr/bin/env python3
import pathlib,subprocess,json,concurrent.futures
R=pathlib.Path(__file__).resolve().parents[1]
specs={'emux-jcguu95':'jcguu95/emux','ob-tmux':'ahendriksen/ob-tmux','eterm-fn':'oitofelix/eterm-fn','myterminal-controls':'emacsorphanage/myterminal-controls','choice-program-complete':'emacsorphanage/choice-program-complete','key-intercept':'tarao/key-intercept-el','alert':'jwiegley/alert'}
def clone(item):
 n,r=item;u='https://github.com/'+r+'.git';d=R/'sources'/n
 p=subprocess.run(['git','clone','--depth','1',u,str(d)],capture_output=True,text=True,timeout=90)
 if p.returncode:return {'id':n,'url':u,'status':'fetch-failed','error':p.stderr}
 sha=subprocess.check_output(['git','-C',str(d),'rev-parse','HEAD'],text=True).strip()
 return {'id':n,'url':u,'status':'fetched','commit':sha}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:rows=list(p.map(clone,specs.items()))
(R/'research/acquisition-extra.json').write_text(json.dumps(rows,indent=2))
print([(r['id'],r['status']) for r in rows])
