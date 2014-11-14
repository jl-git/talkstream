#!/bin/sh

cat > tmp.md <<EOF
---
title:
speaker:
date: 16:15:00
series: stanford-la-opt
---

EOF

vi tmp.md
DATE=`awk '/date:/ { print $2 }' tmp.md`
mv tmp.md _talks/$DATE-stanford.md
