#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 || ! -f $1 || ! -f $2 || ! $3 =~ ^[0-9]+$ ]]; then
  echo "usage: operations_report.sh LATENCY_NUMBERS SERVICE_TSV LIMIT_MS" >&2
  exit 2
fi
latencies=$1
services=$2
limit=$3
p90=$(LC_ALL=C sort -n -- "$latencies" | awk '/^[0-9]+$/ {a[++n]=$1} END{if(n)print a[int((9*n+9)/10)];else print 0}')
failed=$(awk -F '\t' '$2=="failed"{n++}END{print n+0}' "$services")
status=OK
if (( p90>limit || failed>0 )); then status=DEGRADED; fi
printf 'status=%s\np90_ms=%s\nfailed_units=%s\n' "$status" "$p90" "$failed"
