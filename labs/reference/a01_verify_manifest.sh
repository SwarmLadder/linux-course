#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -f $1 ]] || exit 2
dir=$(dirname -- "$1")
file=$(basename -- "$1")
if (cd -- "$dir" && sha256sum --quiet -c -- "$file") >/dev/null 2>&1; then
 printf 'OK\n'
else
 printf 'FAIL\n'
 exit 1
fi
