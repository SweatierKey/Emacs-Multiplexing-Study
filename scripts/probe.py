#!/usr/bin/env python3
"""Load each project in a fresh Emacs and record commands; loading is NOT an end-to-end test."""
import pathlib,json,re,subprocess,concurrent.futures
R=pathlib.Path(__file__).resolve().parents[1]
deps=set('ace-window avy compat consult dash f frame-local helm ht hydra loop marginalia s shackle projectile projectile-rails popup posframe transient vertico with-editor circe window-layout buffer-manage popwin with-shell-interpreter friendly-tramp-path yaxception log4e auto-complete readline-complete migemo uuid map bind-key names cl-lib emacs-async compat-assoc cooked-build herdr-runtime zmx-runtime zmx exec-path-from-shell eshell-up eshell-z esh-autosuggest'.split())
alias={'el-be-back':'ebb','libgterm':'gterm','wterm':'wterm','winterm':'emacs-winterm','emux':'emux-base','emux-rock':'emux-base','emux-shcv':'emux','emux-attic':'emux','emux-el':'emux','term-plus-mux':'term+mux','term-plus-xterm':'term+','term-plus-fork':'term+','multi-term-roman':'multi-term','eat-lucasec':'eat','eaf-terminal':'eaf-terminal','tmux-el':'tmux','tmux-tandem':'tmux-tandem','multi-eshell':'multi-eshell','multi-run':'multi-run','herdr-emacs':'herdr-emacs','emacs-herdr':'herdr','term':'term','eshell':'eshell','shell':'shell','tab-bar':'tab-bar'}
alias.update({'evil-tmux-navigator':'navigate','eev':'eev-load','vterm-manager':'vtm','tmux-control-mode':'tmux-cc','tmux-runner':'emacs-tmux-runner','deskel':'desk','emacs-tunnel':'tslime'})
deps.update('choice-program alert key-intercept eterm-fn'.split())
rows=json.loads((R/'research/source-lock.json').read_text()); projects=[dict(x,feature=alias.get(x['id'],x['id'])) for x in rows if x['id'] not in deps]
(R/'research/projects.json').write_text(json.dumps(projects,indent=2)+'\n')
(R/'results/load').mkdir(exist_ok=True)
def run(x):
 name=x['id'];feature=x['feature'];d=R/'sources'/name
 if x.get('status')=='fetch-failed':
  (R/'results/load'/(name+'.log')).write_text('Source not acquired; no load test performed.\n')
  return {'id':name,'status':'not-acquired','error':'Source acquisition failed; not tested'}
 setup=f'(let ((p "{d}")) (setq load-path (cons p (delete p load-path))))\n'
 # Do not silently require a different repository's same-named feature.
 setup+=f'''(condition-case err (progn (require '{feature})
(princ (json-encode `((status . "loaded") (feature . "{feature}") (library . ,(locate-library "{feature}"))
(commands . ,(vconcat (let (out) (mapatoms (lambda (sym) (when (and (commandp sym) (symbol-file sym 'defun) (string-prefix-p "{d}/" (symbol-file sym 'defun))) (push (symbol-name sym) out)))) (sort out #'string<))))))))
(error (princ (json-encode `((status . "error") (error . ,(error-message-string err)))))))'''
 try:
  p=subprocess.run(['emacs','-Q','--batch','-l',str(R/'config/init.el'),'--eval','(progn '+setup+')'],cwd=R,capture_output=True,text=True,timeout=20)
  (R/'results/load'/(name+'.log')).write_text(p.stdout+'\nSTDERR:\n'+p.stderr)
  try:out=json.loads(p.stdout)
  except Exception:out={'status':'error','error':(p.stdout+p.stderr)[-1500:]}
  out.update(id=name,exit_code=p.returncode)
  if out.get('status')=='loaded' and name not in ['term','shell','eshell','tab-bar','terminal','ob-screen'] and not str(out.get('library','')).startswith(str(d)+'/'):
   out.update(status='wrong-library',error='Same-named feature resolved outside this repository; not a successful load of this project')
 except subprocess.TimeoutExpired:out={'id':name,'status':'timeout','error':'20 s load deadline'}
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(run,projects))
(R/'results/load.json').write_text(json.dumps(results,indent=2)+'\n')
for x in results:print(x['id'],x['status'],x.get('error','')[:130])
