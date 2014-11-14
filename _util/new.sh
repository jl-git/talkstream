#!/bin/sh

cat > tmp.md <<EOF
---
title:
speaker:
date:
series:
---

EOF

vi tmp.md
DATE=`awk '/date:/ { print $2 }' tmp.md`
mv tmp.md _talks/$DATE-$1.md
