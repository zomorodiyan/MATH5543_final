import numpy as np


def three_diagonal(main, super, size):
    A = np.zeros((size, size))
    for i in range(size):
        A[i, i] = main
    for i in range(size - 1):
        A[i, i + 1] = super
        A[i + 1, i] = super
    return A


def left_hand_side(r, size):
    return three_diagonal(1 + 2 * r, -r, size)


def right_hand_side(r, field, boundaryConditions, t, h, k, size):
    # page 183 of "FDM for ODE and PDE, by Randall J."
    def exact(x, t):
        return np.exp(-((x - 2 * t - 0.5) ** 2))

    def f(x, t):
        term = x - 2 * t - 0.5
        ut = 4 * term * exact(x, t)
        uxx = -2 * exact(x, t) + 4 * term ** 2 * exact(x, t)
        return ut - uxx

    [bl, blp, br, brp] = boundaryConditions
    B = np.zeros(size)
    B[0] = r * (bl + blp) + (1 - 2 * r) * field[0] + r * field[1] + k * f(h, t)
    for i in range(1, size - 1):
        B[i] = (
            r * field[i - 1]
            + (1 - 2 * r) * field[i]
            + r * field[i + 1]
            + k * f((i + 1) * h, t)
        )
    B[-1] = (
        r * field[-2] + (1 - 2 * r) * field[-1] + r * (br + brp) + k * f(size * h, t)
    )
    return B
