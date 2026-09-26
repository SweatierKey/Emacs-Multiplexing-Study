#!/bin/bash
# A real SSH connection, two roles on the same host: not two independent machines.
set -eu
role=$1
lab_root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)
export TERMINFO_DIRS="$lab_root/.runtime/terminfo:/usr/share/terminfo:/lib/terminfo"
export STUDY_ROLE="$role"
export PS1="${role}@lab:\\w\\$ "
export HISTFILE=/dev/null
export PROMPT_COMMAND=''
cd "$(dirname "$0")/fixtures/$role"
printf '\nSSH LAB: %s (loopback fixture, same kernel)\n' "$role"
if [ -n "${SSH_ORIGINAL_COMMAND:-}" ]; then exec /bin/bash --noprofile --norc -c "$SSH_ORIGINAL_COMMAND"; fi
exec /bin/bash --noprofile --norc -i
