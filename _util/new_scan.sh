#!/bin/sh

cat > tmp.md <<EOF
---
title:
speaker:
date: 13:25:00
series: cornell-scan
---

EOF

vi tmp.md
DATE=`awk '/date:/ { print $2 }' tmp.md`
mv tmp.md _talks/$DATE-cornell.md
