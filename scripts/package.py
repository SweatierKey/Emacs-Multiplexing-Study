#!/usr/bin/env python3
"""Deterministic file ordering; exclude runtime keys, caches and VCS internals."""
import pathlib,tarfile,gzip,hashlib,json,os
R=pathlib.Path(__file__).resolve().parents[1];target=R.parent/'Emacs-Multiplexing-Study-2026-09-26.tar.gz'
skip={'.git','.runtime','__pycache__','.zig-cache','zig-out','target','node_modules'}
files=[]
for p in sorted(R.rglob('*')):
 rel=p.relative_to(R)
 if any(x in skip for x in rel.parts) or not p.is_file():continue
 if p.is_symlink() and not p.resolve().is_relative_to(R):continue
 if p.name=='MANIFEST.sha256' or p.suffix in ['.pyc','.elc']:continue
 if p.name.endswith('.tar.gz') and rel.parts[0] not in ['native','vendor']:continue
 files.append(p)
(R/'MANIFEST.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(R))+'\n' for p in files))
files.append(R/'MANIFEST.sha256')
with open(target,'wb') as raw,gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as gz,tarfile.open(fileobj=gz,mode='w|') as tar:
 for p in files:
  info=tar.gettarinfo(str(p),arcname='Emacs-Multiplexing-Study/'+str(p.relative_to(R)));info.uid=info.gid=0;info.uname=info.gname='';info.mtime=0
  if p.is_symlink():tar.addfile(info)
  else:
   with p.open('rb') as f:tar.addfile(info,f)
sha=hashlib.sha256(target.read_bytes()).hexdigest();target.with_name(target.name+'.sha256').write_text(sha+'  '+target.name+'\n')
print(json.dumps({'archive':str(target),'bytes':target.stat().st_size,'sha256':sha,'files':len(files)},indent=2))
