#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 || ! -f $1 ]]; then
  echo "usage: log_summary.sh LOG_FILE" >&2
  exit 2
fi
awk '
  {
    rows++
    if($2=="ERROR") errors++
    for(i=1;i<=NF;i++) if($i~/^user=/) {
      split($i,f,"=")
      if(length(f[2])) users[f[2]]=1
    }
  }
  END {
    for(name in users) unique++
    print "records=" rows+0
    print "errors=" errors+0
    print "unique_users=" unique+0
  }
' "$1"
