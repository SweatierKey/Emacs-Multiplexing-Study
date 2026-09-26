#!/usr/bin/env python3
"""Produce an auditable symbol/require/key-binding index, not a substitute for review."""
import pathlib,re,json,hashlib
root=pathlib.Path(__file__).resolve().parents[1];rows={}
for p in sorted((root/'research').glob('acquisition*.json')):
 for r in json.loads(p.read_text()):
  if r['id'] not in rows or r['status']=='fetched':rows[r['id']]=r
for name in ['term','shell','eshell','tab-bar','terminal','ob-screen']:
 rows[name]={'id':name,'url':'https://git.savannah.gnu.org/cgit/emacs.git','version':'30.1','status':'builtin'}
(root/'research'/'source-lock.json').write_text(json.dumps(list(rows.values()),indent=2)+'\n')
out=root/'report'/'code-index';out.mkdir(exist_ok=True)
for name,r in sorted(rows.items()):
 d=root/'sources'/name; files=[]; lines=[f'# Indice del codice: {name}',f"\nFonte: {r['url']}\n\nRevisione: `{r.get('commit',r.get('version','non acquisito'))}`.\n"]
 for p in sorted(d.rglob('*.el')):
  if any(s in p.parts for s in ['vendor','test','tests','bench']):continue
  s=p.read_text(errors='replace');rel=p.relative_to(root).as_posix();files.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'lines':s.count('\n')})
  lines.append(f'\n## {p.relative_to(d)}\n')
  for i,l in enumerate(s.splitlines(),1):
   if re.match(r'^\((?:defun|cl-defun|defmacro|define-derived-mode|define-minor-mode|defcustom|defvar-keymap|defvar .*map|require|provide)\b',l) or re.search(r'\((?:define-key|keymap-set|keymap-global-set|global-set-key) ',l):lines.append(f'- L{i}: `{l.strip().replace(chr(96),chr(39))}`')
 r['files']=files
 (out/(name+'.md')).write_text('\n'.join(lines)+'\n')
(root/'research'/'source-index.json').write_text(json.dumps(list(rows.values()),indent=2)+'\n')
print(len(rows),'repositories/builtins; generated code indices')
