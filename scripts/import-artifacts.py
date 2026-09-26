#!/usr/bin/env python3
"""Import the existing repository workflow artifacts, preserving acquisition metadata."""
import pathlib, tarfile, sys, shutil
root=pathlib.Path(__file__).resolve().parents[1]
for p in sorted(pathlib.Path(sys.argv[1]).rglob('*.tar.gz')):
 if p.name=='lab-debs.tar.gz': continue
 print(p,flush=True)
 with tarfile.open(p) as t:
  for m in t.getmembers():
   n=m.name.removeprefix('./')
   if n.startswith('src/'): m.name='sources/'+n[4:]
   else: m.name=n
   if not m.name: continue
   t.extract(m,root,filter='data')
