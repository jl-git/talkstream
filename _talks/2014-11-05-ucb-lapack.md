---
title: Improved Column-Based Matrix Reconstruction
speaker: Chris Melgaard
affil: UC Berkeley
date: 2014-11-05 12:10:00
talk-url: http://math.berkeley.edu/~mgu/Seminar/Fall2014/MCaSCS_2014-11-05.pdf
series: ucb-lapack
---

Column-based matrix reconstruction, or the CX decomposition, has become a
popular tool in large-scale data analysis for constructing low-rank matrix
approximations built using the features (or columns) of the data. In this work,
we present a modiﬁed deterministic algorithm for column selection, based on the
seminal work of Boutsidis, Drineas and Magdon-Ismail. Our modiﬁed algorithm
enjoys improved computational complexity, less memory usage and stronger error
bounds. We also provide a randomized version for further computational
efficiency. Our algorithms offer stronger controls on the spectral and
Frobenius norm errors. Additionally, we provide novel rank revealing lower
bounds on the individual singular values in the CX decomposition. For matrices
with decaying singular values (the typical case with real-world data), our
bounds surprisingly suggest that the CX decomposition is capable of accurately
retaining the leading singular values almost at the same accuracy as the
truncated SVD. Using synthetic and real data matrices, we report numerical
tests to reaffirm the efficiency and accuracy of our algorithms.

