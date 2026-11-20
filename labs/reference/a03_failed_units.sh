#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -f $1 ]] || exit 2
matches=$(awk -F '\t' '$2=="failed"{print $1}' "$1" | LC_ALL=C sort)
if [[ -n $matches ]]; then printf '%s\n' "$matches"; else printf 'NO_FAILURES\n'; fi
