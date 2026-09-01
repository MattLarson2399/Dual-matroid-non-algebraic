# Dual-matroid-non-algebraic
This file contains code to accompany the paper "Duals of algebraic matroids need not be algebraic" by Matt Larson and Tuong Le. 

Using Zvi Rosen's code available [here](), which is based on the paper ["Computing algebraic matroids"](https://arxiv.org/abs/1403.8148), one can verify the description of the algebraic matroid N in the paper. If one runs
```
M2 computebases.M2
```
in this directory on a machine in Macaulay2 installed, then it will essentially instantaneously output a list of nonbases of algebraic matroid N. 
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
We now describe how to check that the matroid dual of N fails the Ingleton-Main extension property at depth 7. For this, we use [code](https://github.com/bmilosh/algebraic-matroids-extensions) written by Bamiloshin and Farràs, based on the paper [Optimizing extension techniques for discovering non-algebraic matroids](https://arxiv.org/abs/2406.18359v2). Running
```
sage check_DL.py
```
in this directory on a machine with Sage installed checks that the dual of N fails the Ingleton-Main extension property at depth 7. This took 2 hours and 25 minutes on a laptop with a 12th Gen Intel Core i7-1250U chip. 