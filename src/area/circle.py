import numpy as np


def circle_area(r):
    if type(r) not in [list, np.ndarray, int, float]:
        raise TypeError("input data (x and y) must be and array of numbers")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return np.pi * (r ** 2)
