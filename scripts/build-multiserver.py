#!/usr/bin/env python3
"""Build the focused report with offline asciinema players, without recataloguing."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
for wheel in (root / 'wheels').glob('markdown*.whl'):
    sys.path.insert(0, str(wheel))
import markdown

source = (root / 'report/MULTISERVER.md').read_text()
players = ''.join(
    '<div class="video"><button data-cast="../recordings/multiserver-' + name +
    '.cast">Riproduci ' + name + '</button><div class="player"></div></div>'
    for name in ['clush', 'term-sessions', 'multi-run'])
body = markdown.markdown(source.replace('<!-- MULTISERVER_VIDEOS -->', players),
                         extensions=['tables', 'fenced_code'])
page = '''<!doctype html><html lang="it"><meta charset="utf-8">
<meta name="viewport" content="width=device-width"><title>Emacs: lavoro multiserver</title>
<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="../player/asciinema-player.css">
<main>''' + body + '''</main><script src="../player/asciinema-player.js"></script>
<script>for(const b of document.querySelectorAll('[data-cast]'))b.onclick=()=>{
AsciinemaPlayer.create(b.dataset.cast,b.parentElement.querySelector('.player'),
{autoPlay:true,idleTimeLimit:2,fit:'width',theme:'asciinema'});b.disabled=true};</script></html>'''
(root / 'report/MULTISERVER.html').write_text(page)
print('Built report/MULTISERVER.html with three offline players')
