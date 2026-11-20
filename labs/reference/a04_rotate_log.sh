#!/usr/bin/env bash
set -euo pipefail
[[ $# == 2 && -f $1 && ! -L $1 && ! -e $2 && ! -L $2 ]] || exit 2
source=$1
archive=$2
[[ -d $(dirname -- "$archive") ]] || exit 2
mv -n -- "$source" "$archive"
: > "$source"
