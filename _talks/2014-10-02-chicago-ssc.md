---
title: High-Performance Computation of Pseudospectra
speaker: Jack Poulson
speaker-url: http://www.cc.gatech.edu/~jpoulson/
affil: Stanford
date: 2014-10-02 16:30:00
talk-url: https://galton.uchicago.edu/seminars/scientific_and_statistical_computing/aut14/Poulson_Jack_100214.pdf
series: chicago-ssc
---

Evaluating the norm of a resolvent over a window in the complex plane provides
an illuminating generalization of a scatter-plot of eigenvalues and is of
obvious interest for analyzing preconditioners. Unfortunately the common
perception is that such a computation is embarrassingly parallel, and so
little effort has been expended towards reproducing the functionality of the
premier tool for pseudospectral computation, EigTool (Wright et al.), for
distributed-memory architectures in order to enable the analysis of matrices
too large for workstations. This talk introduces several high-performance
variations of Lui’s triangularization followed by inverse iteration approach
which involve parallel reduction to (quasi-)triangular or Hessenberg form
followed by interleaved Implicitly Restarted Arnoldi iterations driven by
multi-shift (quasi-)triangular or Hessenberg solves with many right-hand
sides. Since multi-shift (quasi-)triangular solves can achieve a very high
percentage of peak performance on both sequential and parallel architectures,
such an approach both improves the efficiency of sequential pseudospectral
computations and provides a high-performance distributed-memory scheme. Results
from recent implementations within Elemental (P. et al.) will be presented
for a variety of large matrices and practical convergence-monitoring schemes
will be discussed.

This is joint work with Greg Henry (Intel).
