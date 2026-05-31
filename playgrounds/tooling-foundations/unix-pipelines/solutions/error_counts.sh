#!/usr/bin/env bash
set -euo pipefail

awk '$4 >= 500 { counts[$3]++ } END { for (path in counts) print counts[path], path }' \
  data/access.log |
  LC_ALL=C sort -k1,1nr -k2,2
