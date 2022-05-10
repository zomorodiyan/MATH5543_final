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


def right_hand_side(r, field, boundaryConditions, size):
    # page 183 of "FDM for ODE and PDE, by Randall J."
    [bl, blp, br, brp] = boundaryConditions
    B = np.zeros(size)
    B[0] = r * (bl + blp) + (1 - 2 * r) * field[0] + r * field[1]
    for i in range(1, size - 1):
        B[i] = r * field[i - 1] + (1 - 2 * r) * field[i] + r * field[i + 1]
    B[-1] = r * field[-2] + (1 - 2 * r) * field[-1] + r * (br + brp)
    return B
