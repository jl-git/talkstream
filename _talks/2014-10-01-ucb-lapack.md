---
title: Finding the sparse representation of a dense matrix
speaker: Lin Lin
speaker-url: http://math.berkeley.edu/~linlin/
affil: UC Berkeley and LBNL
date: 2014-10-01 12:10:00
talk-url: http://math.berkeley.edu/~mgu/Seminar/Fall2014/MCaSC_2014-10-01.pdf
series: ucb-lapack
---

Let $\Psi$ be a unitary, dense matrix of size m*n (m>>n).  The
$\varepsilon$-sparse representation of $\Psi$ means that there is a matrix
$\Phi$ of size m*n such that each column of $\Phi$ is sparse, $C$ is an n*n
invertible matrix, and $||\Psi-\Phi C||<\varepsilon$.  In quantum physics, the
existence of such sparse representation explains why many chemical systems
exhibit local characters.  In this talk we discuss some existing numerical
techniques for finding such functions which originate from quantum physics
literature.  From a numerical linear algebra perspective, we introduce a new
technique called the selected columns of the density matrix (SCDM), which finds
such representation efficiently through a rank revealing QR procedure.
Generalization for the case when $\Psi$ is not unitary will also be discussed.

