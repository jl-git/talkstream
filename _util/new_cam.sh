#!/bin/sh

cat > tmp.md <<EOF
---
title:
speaker:
date: 15:30:00
series: cornell-cam
---

EOF

vi tmp.md
DATE=`awk '/date:/ { print $2 }' tmp.md`
mv tmp.md _talks/$DATE-cornell.md
