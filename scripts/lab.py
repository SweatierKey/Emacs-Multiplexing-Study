#!/usr/bin/env python3
"""Start/stop two unprivileged loopback SSH endpoints. Keys remain in .runtime."""
import pathlib,subprocess,os,sys,json,time,signal,shlex
root=pathlib.Path(__file__).resolve().parents[1]; runtime=root/'.runtime'; runtime.mkdir(exist_ok=True)
state=runtime/'lab-state.json'
if len(sys.argv)>1 and sys.argv[1]=='stop':
 if state.exists():
  for row in json.loads(state.read_text()):
   try:os.kill(row['pid'],signal.SIGTERM)
   except ProcessLookupError:pass
  state.unlink()
 sys.exit()
if state.exists():print('Lab state already exists:',state);sys.exit(0)
user=subprocess.check_output(['id','-un'],text=True).strip()
for name in ['host','client']:
 p=runtime/name
 if not p.exists():subprocess.run(['ssh-keygen','-q','-t','ed25519','-N','','-f',str(p)],check=True)
rows=[];client=[]
for role,port in [('web',22461),('db',22462)]:
 d=root/'lab'/'fixtures'/role;d.mkdir(parents=True,exist_ok=True)
 (d/'service.log').write_text(f'INFO {role} boot complete\nINFO {role} health=ok\nWARN {role} disk threshold=75\nINFO {role} requests=42\n')
 (d/'status.txt').write_text(f'role={role}\nservice=active\nversion=1.0\n')
 authorized=runtime/(role+'-authorized_keys');authorized.write_text((runtime/'client.pub').read_text())
 config=runtime/(role+'-sshd_config')
 config.write_text(f'''Port {port}
ListenAddress 127.0.0.1
HostKey {runtime}/host
PidFile {runtime}/{role}.pid
AuthorizedKeysFile {authorized}
StrictModes no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
UsePAM no
AllowUsers {user}
AllowTcpForwarding no
X11Forwarding no
ForceCommand {root}/lab/remote-shell.sh {role}
LogLevel ERROR
''')
 log=open(runtime/(role+'-sshd.log'),'w')
 p=subprocess.Popen(['/usr/sbin/sshd','-D','-e','-f',str(config)],stdout=log,stderr=log,start_new_session=True)
 rows.append({'role':role,'port':port,'pid':p.pid})
 client.append(f'''Host lab-{role}
  HostName 127.0.0.1
  Port {port}
  User {user}
  IdentityFile {runtime}/client
  IdentitiesOnly yes
  UserKnownHostsFile {runtime}/known_hosts
  StrictHostKeyChecking yes
  LogLevel ERROR
''')
(runtime/'ssh_config').write_text('\n'.join(client))
pub=(runtime/'host.pub').read_text().split();(runtime/'known_hosts').write_text(''.join(f'[127.0.0.1]:{r["port"]} {pub[0]} {pub[1]}\n' for r in rows))
state.write_text(json.dumps(rows,indent=2));time.sleep(.5)
for r in rows:
 p=subprocess.run(['ssh','-F',str(runtime/'ssh_config'),'lab-'+r['role'],'cat status.txt'],capture_output=True,text=True,timeout=10)
 print(r['role'],p.returncode,p.stdout,p.stderr)
 if p.returncode:sys.exit(p.returncode)
