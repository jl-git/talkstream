#!/bin/sh

if [ "$#" -ne 1 ]; then
  echo "new_job tag"
  exit 1
fi

cat > tmp.md <<EOF
---
title:
date:
expires:
source:
---

EOF

vi tmp.md
DATE=`awk '/date:/ { print $2 }' tmp.md`
mv tmp.md _jobs/$DATE-$1.md
