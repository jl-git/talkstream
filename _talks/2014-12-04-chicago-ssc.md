---
title: A General Framework for Fast Stagewise Algorithms
speaker: Ryan Tibshirani
speaker-url: http://www.stat.cmu.edu/~ryantibs/
affil: CMU
date: 2014-12-04 16:30:00
talk-url: https://galton.uchicago.edu/seminars/scientific_and_statistical_computing/aut14/Tibshirani_Ryan_120414.pdf
series: chicago-ssc
---

Forward stagewise regression follows a very simple strategy for constructing a
sequence of sparse regression estimates: starting with all coefficients equal
to zero, it iteratively updates the coefficient (by a small amount $\epsilon$)
corresponding to the variable that has maximal absolute inner product with the
current residual. This procedure has an interesting connection to the lasso:
under some conditions, it can be shown that the sequence of forward stagewise
estimates exactly coincides with the lasso path, as the step size $\epsilon$
goes to zero. Further, essentially the same equivalence holds outside of the
regression setting, for minimizing a differentiable convex loss function
subject to an $\ell$ norm constraint (and the stagewise algorithm now updating
the coefficient corresponding to the maximal absolute component of the
gradient).

Even when they do not match their $\ell$-constrained analogues, stagewise
estimates provide a useful approximation, and are computationally appealing.
Their success in sparse modeling motivates the question: can a simple,
effective strategy like forward stagewise be applied more broadly in other
regularization settings, beyond the $\ell$ norm and sparsity? This is the focus
of the talk; we present a general framework for stagewise estimation, which
yields fast algorithms for problems such as group-structured learning, matrix
completion, image denoising, and more.

