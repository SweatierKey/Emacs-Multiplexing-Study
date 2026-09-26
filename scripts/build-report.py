#!/usr/bin/env python3
"""Build offline HTML gallery and evidence-linked per-project Markdown dossiers."""
import pathlib,json,csv,html,collections,sys,hashlib
R=pathlib.Path(__file__).resolve().parents[1]
for p in (R/'wheels').glob('markdown*.whl'):sys.path.insert(0,str(p))
import markdown
notes={r['id']:r for r in csv.DictReader((R/'report/review-notes.tsv').open(),delimiter='\t')}
projects=json.loads((R/'research/projects.json').read_text());loads={r['id']:r for r in json.loads((R/'results/load.json').read_text())}
results={}
for p in (R/'results').glob('*.json'):
 try:r=json.loads(p.read_text())
 except Exception:continue
 if isinstance(r,dict) and r.get('status') in ['passed','failed'] and 'id' in r:results[r['id']]=r
aliases={'term':['term','ansi-term'],'eat':['eat','eat-eshell'],'vterm':['vterm','tmux-nested'],'term-sessions':['term-sessions','term-sessions-persistence']}
stats=collections.Counter(r['status'] for r in results.values())
summary={'date':'2026-09-26','source_entries':len(json.loads((R/'research/source-lock.json').read_text())),'catalogue_entries':len(projects),'scenarios':len(results),'passed':stats['passed'],'failed':stats['failed'],'recordings':len(list((R/'recordings').glob('*.cast'))),'categories':dict(collections.Counter(notes.get(x['id'],{}).get('categoria','da-classificare') for x in projects))}
(R/'report/summary.json').write_text(json.dumps(summary,indent=2)+'\n')
css='''body{margin:0;background:#f4f5f2;color:#18242a;font:17px/1.55 system-ui,sans-serif}main{max-width:1120px;margin:auto;padding:36px 24px}h1{font-size:2.3rem;line-height:1.15}h2{margin-top:2.2em}a{color:#076b73}header{border-bottom:3px solid #147b72;padding-bottom:26px}.stats{display:flex;gap:12px;flex-wrap:wrap;margin:24px 0}.stat,details{background:white;border:1px solid #ced8d4;border-radius:8px;padding:16px}.stat strong{display:block;font-size:1.6rem}.small{font-size:.88rem;color:#526367}input,select,button{font:inherit;padding:9px;border:1px solid #8ba5a0;border-radius:5px;background:white;margin:4px}input{min-width:260px}details{margin:10px 0}summary{cursor:pointer;font-weight:650}.tag{font-size:.8rem;display:inline-block;padding:2px 8px;background:#edf1ef;border-radius:10px;margin-left:8px}.passed{color:#165f31}.failed{color:#a22923}.video{margin-top:16px}pre{overflow:auto;background:#e9eeeb;padding:16px}code{font-size:.88em}table{border-collapse:collapse;display:block;overflow:auto}td,th{border:1px solid #cad4d0;padding:7px;text-align:left}blockquote{border-left:4px solid #ba8a22;margin-left:0;padding:10px 18px;background:#fff7df}.notice{background:#fff7df;padding:15px;border-left:4px solid #b78a19}footer{margin:35px 0;color:#526367} .ap-wrapper{font-size:15px!important}'''
(R/'report/style.css').write_text(css)
cat=['# Catalogo dei progetti\n','Data dello snapshot: 26 settembre 2026. Le schede distinguono revisione architetturale, caricamento e prove end-to-end. Un indice automatico dei simboli non è una revisione completa di ogni riga.\n']
cards=[];catalog=[]
for p in sorted(projects,key=lambda x:x['id']):
 n=p['id'];note=notes.get(n,{'categoria':'da-classificare','architettura':'Sorgente acquisito; nessuna conclusione architetturale formulata.','uso_e_limiti':'Nessuna prova end-to-end.'});ls=loads.get(n,{})
 rs=[results[x] for x in aliases.get(n,[n]) if x in results];status='passed' if rs and all(r['status']=='passed' for r in rs) else 'failed' if rs else 'not-run'
 rev=p.get('commit',p.get('version','non acquisita'));url=p['url'];up=url.removesuffix('.git')
 text=f"# {n}\n\nCategoria: **{note['categoria']}**. [Sorgente upstream]({up}). Revisione: `{rev}`.\n\n## Funzionamento\n\n{note['architettura']}\n\n## Utilizzo umano e limiti\n\n{note['uso_e_limiti']}\n\n## Evidenza\n\n- Acquisizione: `{p.get('status')}`.\n- Caricamento isolato: `{ls.get('status','non eseguito')}`.\n- [Indice dei simboli e riferimenti alle righe](../code-index/{n}.md).\n- [Log del caricamento](../../results/load/{n}.log).\n"
 if ls.get('error'):text+='\nErrore di caricamento osservato (non necessariamente difetto del progetto):\n\n```text\n'+ls['error']+'\n```\n'
 if not rs:text+='\n**Nessuna dimostrazione end-to-end prodotta per questo progetto.** La descrizione del comportamento deriva dal codice/documentazione, non da una prova eseguita.\n'
 videos=[]
 for r in rs:
  rid=r['id'];cast=R/'recordings'/(rid+'.cast');ks=R/'results'/(rid+'-keys.json')
  text+=f"\n### Scenario {rid}: {r['status']}\n\n[Esito e snapshot](../../results/{rid}.json) · [Traccia dei tasti](../../results/{rid}-keys.json)"
  if cast.exists():text+=f' · [Registrazione asciinema](../../recordings/{rid}.cast) · [Player](../../index.html#{n})';videos.append((rid,r['status']))
  text+='\n\n'
  for k,v in r.get('checks',{}).items():text+=f'- `{k}`: `{v}`\n'
  if r.get('error') is not None:text+='\nErrore finale: '+(r['error'] or 'asserzione non soddisfatta; leggere traceback e snapshot')+'\n'
  if ks.exists():
   steps=json.loads(ks.read_text());text+='\nSequenza realmente inviata (secondi dall’avvio, incluso RET):\n\n| t | Tasto / input |\n|---:|---|\n'
   for step in steps:text+=f"| {step['at']:.2f} | `{step['keys'].replace('|','/').replace('`','')}` |\n"
  if r.get('resume_recording'):text+=f"\n[Registrazione della riconnessione](../../recordings/{r['resume_recording']}).\n";videos.append((r['resume_recording'].removesuffix('.cast'),r['status']))
 d=R/'report/projects';d.mkdir(exist_ok=True);(d/(n+'.md')).write_text(text)
 cat.append(f"- [{n}](projects/{n}.md) — {note['categoria']}; caricamento `{ls.get('status','non eseguito')}`; scenario `{status}`. {note['architettura']}")
 h=html.escape
 videohtml=''.join(f'<div class="video"><button data-cast="recordings/{h(vid)}.cast">Riproduci {h(vid)} — {h(st)}</button><a href="recordings/{h(vid)}.cast"> scarica .cast</a><div class="player"></div></div>' for vid,st in videos)
 cards.append(f'<details id="{h(n)}" data-category="{h(note["categoria"])}" data-status="{status}"><summary>{h(n)} <span class="tag">{h(note["categoria"])}</span><span class="tag {status}">{status}</span></summary><p>{h(note["architettura"])}</p><p>{h(note["uso_e_limiti"])}</p><p class="small">Snapshot {h(rev)} · caricamento {h(ls.get("status","non eseguito"))}</p><p><a href="report/projects/{h(n)}.html">Scheda completa, tasti e risultati</a> · <a href="{h(up)}">upstream</a></p>{videohtml or "<p><strong>Nessuna registrazione end-to-end per questa voce.</strong></p>"}</details>')
 catalog.append(dict(id=n,category=note['categoria'],source=url,revision=rev,acquisition=p.get('status'),load=ls.get('status'),scenario=status,scenario_ids=[r['id'] for r in rs]))
(R/'report/CATALOGUE.md').write_text('\n'.join(cat)+'\n');(R/'report/catalogue.json').write_text(json.dumps(catalog,indent=2)+'\n')
catopts=''.join(f'<option>{html.escape(c)}</option>' for c in sorted(summary['categories']))
page=f'''<!doctype html><html lang="it"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Emacs Multiplexing Study</title><link rel="stylesheet" href="report/style.css"><link rel="stylesheet" href="player/asciinema-player.css"><main><header><p class="small">RICERCA E LABORATORIO · 26 SETTEMBRE 2026</p><h1>Terminali e multiplexer in Emacs</h1><p>Codice, workflow da amministratore di sistema e registrazioni riproducibili con Vertico e Marginalia.</p><p><a href="report/REPORT.html">Leggi il report</a> · <a href="report/MULTISERVER.html">Nuovo: lavoro multiserver</a> · <a href="report/REPRODUCE.html">Riproduci le prove</a> · <a href="https://github.com/SweatierKey/Emacs-Multiplexing-Study/releases/tag/study-2026-09-26">Archivio completo</a> · <a href="report/SEARCH.html">Metodo di ricerca</a></p></header><div class="stats"><div class="stat"><strong>{len(projects)}</strong>voci nel catalogo, incluse adiacenti</div><div class="stat"><strong>{stats['passed']}</strong>scenari riusciti</div><div class="stat"><strong>{stats['failed']}</strong>scenari incompleti/falliti</div><div class="stat"><strong>{len(results)}</strong>scenari eseguiti</div></div><p class="notice">Il censimento non dimostra di contenere tutti i progetti mai esistiti. Una voce senza video è analisi/probe, non un test end-to-end. I due server SSH sono fixture locali sullo stesso kernel. “passed” vale solo per i controlli descritti nella scheda.</p><h2>Esplora il catalogo</h2><label>Cerca <input id="query" type="search" placeholder="Nome, backend, comportamento"></label><label>Categoria <select id="category"><option value="">Tutte</option>{catopts}</select></label><label>Scenario <select id="status"><option value="">Tutti</option><option>passed</option><option>failed</option><option>not-run</option></select></label><p id="count" class="small"></p>{''.join(cards)}<footer>I video sono catture della PTY reale di Emacs. Nessun output shell è stato disegnato per simulare il risultato. I tasti sono consultabili nelle schede. Sorgenti e binari sono nell'archivio della release, con hash e licenze originali.</footer></main><script src="player/asciinema-player.js"></script><script>
const cards=[...document.querySelectorAll('details')];function filter(){{let n=0;for(const c of cards){{c.hidden=!(c.textContent.toLowerCase().includes(document.querySelector('#query').value.toLowerCase())&&(!category.value||c.dataset.category===category.value)&&(!status.value||c.dataset.status===status.value));if(!c.hidden)n++}}document.querySelector('#count').textContent=n+' voci visibili'}}
const category=document.querySelector('#category'),status=document.querySelector('#status');document.querySelector('#query').oninput=filter;category.onchange=filter;status.onchange=filter;filter();
for(const b of document.querySelectorAll('[data-cast]'))b.onclick=()=>{{AsciinemaPlayer.create(b.dataset.cast,b.parentElement.querySelector('.player'),{{autoPlay:true,idleTimeLimit:2,fit:'width',theme:'asciinema'}});b.disabled=true}};
function target(){{let c=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(c&&c.tagName==='DETAILS'){{c.open=true;c.scrollIntoView()}}}}addEventListener('hashchange',target);target();
</script></html>'''
(R/'index.html').write_text(page)
# Render links to Markdown dossiers as navigable HTML; code index Markdown stays available.
for p in (R/'report').glob('*.md'):
 body=markdown.markdown(p.read_text(),extensions=['tables','fenced_code']);body=body.replace('.md"','.html"')
 p.with_suffix('.html').write_text('<!doctype html><html lang="it"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><link rel="stylesheet" href="style.css"><main><a href="../index.html">← Catalogo e video</a>'+body+'</main></html>')
for folder in ['projects','code-index']:
 for p in (R/'report'/folder).glob('*.md'):
  body=markdown.markdown(p.read_text(),extensions=['tables','fenced_code']);body=body.replace('.md"','.html"')
  p.with_suffix('.html').write_text('<!doctype html><html lang="it"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><link rel="stylesheet" href="../style.css"><main><a href="../../index.html">← Catalogo e video</a>'+body+'</main></html>')
print(summary)
