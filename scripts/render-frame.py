#!/usr/bin/env python3
"""Optional still from a pyte replay. Requires ffmpeg; not used to fake a demo."""
import pathlib,subprocess
R=pathlib.Path(__file__).resolve().parents[1]
subprocess.run(['python3',str(R/'scripts/verify.py')],check=True)
subprocess.run(['ffmpeg','-y','-f','lavfi','-i','color=c=0x101820:s=1340x750','-vf','drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf:textfile=results/rendered/vterm.txt:fontsize=18:fontcolor=white:x=10:y=12:line_spacing=3:expansion=none','-frames:v','1','-update','1','report/vterm-replayed.png'],cwd=R,check=True)
