---
title: Bounds on the Energy Consumption of Computational Kernels
speaker: Andrew Gearhart
speaker-url: http://www.eecs.berkeley.edu/~agearh/
affil: UC Berkeley
date: 2014-09-17 12:10:00
talk-url: http://math.berkeley.edu/~mgu/Seminar/Fall2014/SCaMCS_2014-09-17.pdf
series: ucb-lapack
---

Motivated by the large and increasingly growing dominant cost (in time and
energy) of moving data, algorithmic improvements have been attained by proving
lower bounds on the data movement required to solve a computational problem,
and then developing communication-optimal algorithms that attain these bounds.
This thesis extends previous research on communication bounds by presenting
bounds on the energy consumption of a large class of algorithms. These bounds
apply to sequential, distributed parallel and heterogeneous machine models and
are extensible to larger classes of machines.  We argue that the energy
consumption of many algorithms is predictable and can be modeled via linear
models with a handful of terms. Given energy bounds, we analyze the
implications of such results under additional constraints, such as an upper
bound on runtime, and also suggest directions for future research that may aid
future development of a hardware/software co-tuning process. We believe that
combining our bounds with other models of energy consumption may provide a
useful method for such co-tuning; i.e. to enable algorithm and hardware
architects to develop provably energy-optimal algorithms on customized hardware
platforms. 

