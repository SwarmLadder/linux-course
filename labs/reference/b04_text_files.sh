#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -d $1 ]] || exit 2
find "$1" -type f -name '*.txt' -printf '%P\n' | LC_ALL=C sort
