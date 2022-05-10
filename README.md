# MATH5543 HW2

![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)

## Final Project, MATH5543 Course Spring 2022, Oklahoma State University
### Instructor: Dr. Xu Zhang
### Textbook: Randall J. LeVeque. Finite Difference Methods for Ordinary and Partial Differential Equations. SIAM, 2007

To run the project locally:
<!-- Code Blocks -->
```bash
  git clone https://github.com/zomorodiyan/MATH5543
  cd MATH5543
  pip install -r requirements.txt
  pip install -r requirements_dev.txt
  pip install .
  mypy src
  flake8 src
```
### problem_1 (1D IBVP)
#### a)
    u = e^(-(x-2t-0.5)**2)
    ut = 2*(x-2t-0.5)*e^(-(x-2t-0.5)**2)
    uxx = (4*(x-2t-0.5)**2 -2)*e^(-(x-2t-0.5)**2)
    f(x,t) = ut - uxx
    bl(t) = u(0,t)
    bl(t) = u(1,t)
#### b)
    Method          u(0.5,0.5)    e_inf(0.5,0.5)
    Backward-Euler: 0.3675        3.23e-4
    Crank-Nicolson: 0.3681        1.38e-4
#### c)
    Method      e_inf_Backward-Euler    e_inf_Crank-Nicolson
    k=1/10      3.92e-2                 1.63e-2
    k=1/20      8.40e-3                 3.45e-3
    k=1/30      3.50e-3                 1.53e-3
    k=1/40      2.02e-3                 8.62e-4
    k=1/50      1.32e-3                 5.80e-4
    k=1/60      9.01e-4                 3.83e-4
    k=1/70      6.98e-4                 2.61e-4
    k=1/80      5.04e-4                 1.92e-4
    k=1/90      3.91e-4                 1.53e-4
    k=1/100     3.23e-4                 1.38e-4

    from the data above we can conclude:
    r_Backward-Euler = 1.97
    r_Crank-Nicolson = 2.12

### problem_2 (2D IBVP) <skiped>
### problem_3 (1D Advection) <skiped>

#### project structure template: https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject
