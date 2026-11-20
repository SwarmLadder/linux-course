#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 || ! -f $1 || -L $1 || ! -d $3 || -L $3 ]]; then
  echo "usage: release_simulator.sh SOURCE_FILE VERSION EXISTING_ROOT" >&2
  exit 2
fi
source=$1
version=$2
root=$3
if [[ ! $version =~ ^[A-Za-z0-9][A-Za-z0-9._-]{0,39}$ || $version == *..* ]]; then
  echo "invalid release name" >&2
  exit 2
fi
mkdir -p -- "$root/releases"
destination="$root/releases/$version"
if [[ -e $destination || -L $destination ]]; then
  echo "release already exists" >&2
  exit 3
fi
stage=$(mktemp -d -- "$root/releases/.stage.XXXXXXXX")
next_link="$root/.next-link.$$"
cleanup() {
  [[ -d $stage ]] && rm -r -- "$stage"
  [[ -L $next_link ]] && rm -- "$next_link"
  :
}
trap cleanup EXIT
cp -- "$source" "$stage/app.txt"
cmp -- "$source" "$stage/app.txt" >/dev/null
mv -T -- "$stage" "$destination"
ln -s -- "releases/$version" "$next_link"
mv -Tf -- "$next_link" "$root/current"
printf 'deployed=%s\n' "$version"
