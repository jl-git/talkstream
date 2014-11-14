---
title: Algorithmic Reslience for Linear Algebra
speaker: Greg Bronevetsky
speaker-url: http://greg.bronevetsky.com/
affil: Lawrence Livermore National Laboratory
date: 2014-10-30 16:15:00
series: stanford-la-opt
---

As High-Performance Computing systems approach Exascale the feature sizes of
their circuits will shrink, while their overall size will grow, all at a fixed
power budget.  As transistors are packed more tightly and hold less charge,
they are expected to grow more vulnerable to a range of faults that corrupt the
computations of the logic circuits built from them.  These faults manifest
themselves as errors in hardware computations, which can propagate to cause
applications to crash, or worse---to silently return incorrect results.  While
it is possible to make hardware more reliable in a way that is transparent to
application software, such techniques are expensive, requiring all computations
to be repeated multiple times, or circuits to be built from more reliable
transistors.  This motivates the development of algorithms that are naturally
resilient to hardware errors.
 
This talk will survey work on algorithmic resilience techniques for linear
algebra computations.  It will cover techniques for basic operations such as
matrix multiplication and factorization, as well as iterative linear solvers.
Finally, I will point out the wide range of algorithms for which no checkers
are known, and various open research opportunities in the field of resilient
algorithms, resilience-aware programming models, and approximate computing in
general.

