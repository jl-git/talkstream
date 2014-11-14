#!/bin/sh

cat > tmp.md <<EOF
---
title:
speaker:
date: 12:10:00
series: ucb-lapack
---

EOF

vi tmp.md
DATE=`awk '/date:/ { print $2 }' tmp.md`
mv tmp.md _talks/$DATE-ucb.md
