#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -f $1 ]] || exit 2
LC_ALL=C sort -n -- "$1" | awk '/^[0-9]+$/ {a[++n]=$1} END{if(!n){print 0;exit} rank=int((9*n+9)/10);print a[rank]}'
