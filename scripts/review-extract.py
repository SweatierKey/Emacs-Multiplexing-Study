#!/usr/bin/env python3
"""Extract implementation excerpts with line numbers for manual architecture review."""
import pathlib,re,json,sys
R=pathlib.Path(__file__).resolve().parents[1]
for name in sys.argv[1:]:
 print('\n###',name)
 paths=sorted((R/'sources'/name).glob('*.el'))
 if not paths:paths=sorted((R/'sources'/name/'lisp').glob('*.el'))
 budget=45
 for p in paths:
  lines=p.read_text(errors='replace').splitlines()
  matches=[]
  for i,l in enumerate(lines):
   if re.search(r'\((?:start-process|make-process|make-term|term-exec|term-ansi-make-term|vterm|ghostel|eat|shell|eshell|process-send-string|call-process|process-file|make-network-process|window-state-put|set-window-configuration|completing-read)\b',l) and not l.lstrip().startswith(';'):
    matches.append(i)
  if matches:
   print(p.relative_to(R))
   shown=set()
   for i in matches[:5]:
    for j in range(max(0,i-2),min(len(lines),i+4)):
     if j in shown:continue
     print(str(j+1)+': '+lines[j]);shown.add(j);budget-=1
     if budget<=0:break
    if budget<=0:break
  if budget<=0:break
