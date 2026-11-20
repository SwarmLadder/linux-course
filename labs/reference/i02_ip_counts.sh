#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -f $1 ]] || exit 2
awk 'NF>=4{counts[$1]++} END{for(ip in counts)print ip,counts[ip]}' "$1" |
 LC_ALL=C sort -k2,2nr -k1,1
