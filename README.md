# Dual-matroid-non-algebraic
This file contains code to accompany the paper "Duals of algebraic matroids need not be algebraic" by Matt Larson and Tuong Le. 

Using Zvi Rosen's code available [here](https://github.com/zvihr/algebraic-matroids), which is based on the paper ["Computing algebraic matroids"](https://arxiv.org/abs/1403.8148), one can verify the description of the algebraic matroid $\mathrm{N}$ in the paper. If one runs
```
M2 computebases.M2
```
in this directory on a machine in Macaulay2 installed, then it will essentially instantaneously output a list of nonbases of algebraic matroid $\mathrm{N}$. 
```
nonbases: 20
{X , X , X , X , X , X }
  1   2   3   4   6   7
{X , X , X , X , X , X }
  1   3   4   5   6   7
{X , X , X , X , X , X }
  1   2   3   5   7   8
{X , X , X , X , X , X }
  1   3   4   6   7   8
{X , X , X , X , X , X }
  1   2   3   4   5   9
{X , X , X , X , X , X }
  1   3   4   6   7   9
{X , X , X , X , X , X }
  1   2   3   6   8   9
{X , X , X , X , X , X  }
  1   2   3   5   6   10
{X , X , X , X , X , X  }
  1   3   4   6   7   10
{X , X , X , X , X , X  }
  1   2   3   4   8   10
{X , X , X , X , X , X  }
  1   2   3   7   9   10
{X , X , X , X , X , X  }
  1   2   4   7   9   10
{X , X , X , X , X , X  }
  1   2   5   7   9   10
{X , X , X , X , X , X  }
  1   2   6   7   9   10
{X , X , X , X , X , X  }
  1   3   5   8   9   10
{X , X , X , X , X , X  }
  2   4   5   8   9   10
{X , X , X , X , X , X  }
  1   4   6   8   9   10
{X , X , X , X , X , X  }
  1   2   7   8   9   10
{X , X , X , X , X , X  }
  3   4   7   8   9   10
{X , X , X , X , X , X  }
  5   6   7   8   9   10
```
We now describe how to check that $\mathrm{N}^*$ fails the Ingleton-Main extension property at depth 7. For this, we use [code](https://github.com/bmilosh/algebraic-matroids-extensions) written by Bamiloshin and Farràs, based on the paper [Optimizing extension techniques for discovering non-algebraic matroids](https://arxiv.org/abs/2406.18359v2). Running
```
sage check_DL.py
```
in this directory on a machine with Sage installed checks that $\mathrm{N}^*$ fails the Ingleton-Main extension property at depth 7. This took 2 hours and 25 minutes on a laptop with a 12th Gen Intel Core i7-1250U chip. 

The code written by Bamiloshin and Farràs is highly optimized. This makes it somewhat involved to inspect and verify the correctness. As part of his [thesis](https://pure.tue.nl/ws/files/110949529/20181207_Bollen.pdf), Bollen wrote very simple [code](https://github.com/gpbollen/Algebraicity-of-Matroids-and-Frobenius-Flocks) to check the Ingleton-Main extension property. However, it is not practical to use his code to check that $\mathrm{N}^*$ fails the Ingleton-Main condition at depth 7. 

We have written a short program which, as described in the paper, does the first three steps of the proof that $\mathrm{N}^*$ does not satisfy the Ingleton-Main extension property. This reduces the verification to checking that three matroids $\mathrm{C}_1$, $\mathrm{C}_2$, and $\mathrm{C}_3$ on $[13]$ do not satisfies the Ingleton-Main extension property at depth 4. We use a version of Bollen's code to check this; this takes 1 hour and 51 minutes for $\mathrm{C}_1$, 1 hour and 36 minutes for $\mathrm{C}_2$, and 1 hours and 11 minutes for $\mathrm{C}_2$. This code can be run using

```
sage bollenIM.py
```
in this directory on a machine with Sage installed. 