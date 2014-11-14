---
title: Physics-inspired algorithms and phase transitions in community detection
speaker: Cris Moore
speaker-url: http://tuvalu.santafe.edu/~moore/
affil: Santa Fe Institute
date: 2014-10-13 16:30:00
talk-url: http://www.pacm.princeton.edu/node/355
series: princeton-pacm
---

Detecting communities, and labeling nodes, is a ubiquitous problem in the study
of networks.  Recently, we developed scalable Belief Propagation algorithms
that update probability distributions of node labels until they reach a fixed
point.  In addition to being of practical use, these algorithms can be studied
analytically, revealing phase transitions in the ability of any algorithm to
solve this problem.  Specifically, there is a detectability transition in the
stochastic block model, below which no algorithm can label nodes better than
chance.  This transition was subsequently established rigorously by Mossel,
Neeman, and Sly, and Massoulie.

I'll explain this transition, and give an accessible introduction to Belief
Propagation and the analogy with free energy and the cavity method of
statistical physics.  We'll see that the consensus of many good solutions is a
better labeling than the "best" solution --- something that is true for many
real-world optimization problems.  While many algorithms overfit, and find
"communities" even in random graphs where none exist, our method lets us focus
on statistically-significant communities.  In physical terms, we focus on the
free energy rather than the ground state energy.

I'll then turn to spectral methods.  It's popular to classify nodes according
to the first few eigenvectors of the adjacency matrix or the graph Laplacian.
However, in the sparse case these operators get confused by localized
eigenvectors, focusing on high-degree nodes or dangling trees rather than
large-scale communities. As a result, they fail significantly above the
detectability transition.  I will describe a new spectral algorithm based on
the non-backtracking matrix, which avoids these localized eigenvectors: it
appears to be optimal in the sense that it succeeds all the way down to the
transition.  Making this rigorous will require us to prove an interesting
conjecture in the theory of random matrices and random graphs.
 
This is joint work with Aurelien Decelle, Florent Krzakala, Elchanan Mossel,
Joe Neeman, Allan Sly, Lenka Zdeborova, and Pan Zhang.
 
