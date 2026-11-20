#!/usr/bin/env bash
set -euo pipefail
[[ $# == 1 && -f $1 ]] || exit 2
awk '$2=="ERROR"{n++} END{print n+0}' "$1"
