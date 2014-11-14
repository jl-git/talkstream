---
title: How practical is fast matrix multiplication?
speaker: Grey Ballard
speaker-url: http://www.sandia.gov/~gmballa/
affil: Sandia National Lab
date: 2014-10-15 12:10:00
talk-url: http://math.berkeley.edu/~mgu/Seminar/Fall2014/MCaSCS_2014-10-15.pdf
series: ucb-lapack
---

Determining the exponent of matrix multiplication has been an exciting
theoretical pursuit for many years, and there continue to be improvements on
the best lower and upper bounds.  While “fast” algorithms for matrix
multiplication perform O(n^w) floating point operations in multiplying n-by-n
matrices with w<3, they are seldom used in practice.  The original fast
algorithm, discovered by Strassen, is known to be practical (i.e.,
outperforming the best implementation of the classical O(n^3) algorithm on
reasonably sized matrices), but most of the other advances in the field of fast
matrix multiplication have focused more on theoretical questions rather than
practical ones.  I’ll talk about how advances in communication-avoiding
algorithms have created some optimism for the practicality of fast algorithms,
show some promising practical results in parallelizing Strassen’s algorithm,
and discuss the prospects of other fast and practical matrix multiplication
algorithms.  In particular, I’ll discuss recent results in using computer-aided
search to find many different fast algorithms and then benchmarking their
performance on both sequential and shared-memory parallel architectures.
