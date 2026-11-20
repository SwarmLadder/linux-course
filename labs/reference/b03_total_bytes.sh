#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -d $1 ]] || exit 2
total=0
while IFS= read -r -d '' file; do
  size=$(stat -c '%s' -- "$file")
  ((total+=size)) || :
done < <(find "$1" -type f -print0)
printf '%d\n' "$total"
