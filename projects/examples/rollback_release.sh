#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 || ! -d $1 || -L $1 ]]; then
  echo "usage: rollback_release.sh ROOT EXISTING_VERSION" >&2
  exit 2
fi
root=$1
version=$2
if [[ ! $version =~ ^[A-Za-z0-9][A-Za-z0-9._-]{0,39}$ || $version == *..* || ! -f $root/releases/$version/app.txt ]]; then
  echo "unknown release" >&2
  exit 2
fi
next_link="$root/.rollback-link.$$"
trap '[[ -L $next_link ]] && rm -- "$next_link"; :' EXIT
ln -s -- "releases/$version" "$next_link"
mv -Tf -- "$next_link" "$root/current"
printf 'active=%s\n' "$version"
