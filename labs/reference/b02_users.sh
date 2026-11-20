#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -f $1 ]] || exit 2
awk '{for(i=1;i<=NF;i++)if($i~/^user=/){split($i,a,"=");if(length(a[2]))print a[2]}}' "$1" | LC_ALL=C sort -u
