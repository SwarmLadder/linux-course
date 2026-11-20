#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -f $1 ]] || exit 2
awk -F= '/^latency_ms=[0-9]+$/ {sum+=$2;n++} END{if(n)printf "%.1f\n",sum/n;else print "0.0"}' "$1"
