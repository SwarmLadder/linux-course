#!/usr/bin/env bash
set -euo pipefail
if [[ $# == 1 && $1 =~ ^[0-9]{1,5}$ ]]; then
  port=$((10#$1))
  if ((port>=1 && port<=65535)); then printf 'VALID\n'; exit 0; fi
fi
printf 'INVALID\n'
exit 1
