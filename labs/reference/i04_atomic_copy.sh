#!/usr/bin/env bash
set -euo pipefail
[[ $# == 2 && -f $1 && ! -L $1 ]] || exit 2
source=$1
destination=$2
[[ -d $(dirname -- "$destination") && ! -d $destination && ! -L $destination ]] || exit 2
tmp=$(mktemp -- "$destination.tmp.XXXXXXXX")
trap 'rm -f -- "$tmp"' EXIT
cp -- "$source" "$tmp"
mv -f -- "$tmp" "$destination"
