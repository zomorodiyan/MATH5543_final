import numpy as np
import unittest
from fdm.crank_nicolson import left_hand_side as lhs
from fdm.crank_nicolson import right_hand_side as rhs
import matplotlib.pyplot as plt


class Test_1D_IBVP(unittest.TestCase):
    def test_(self):
        def exact(x, t):
            return np.exp(-((x - 2 * t - 0.5) ** 2))

        size = 11
        x = np.linspace(0, 1, size)
        u = exact(x, 0)
        k = 0.01
        h = 0.01
        a = 0.5  # ut = a.uxx + f
        r = a * k / 2 / h ** 2
        tn = 0.5
        t = 0
        while t <= tn:
            bl = exact(0, t)
            br = exact(1, t)
            t = t + k
            blp = exact(0, t)
            brp = exact(1, t)
            bcz = (bl, blp, br, brp)
            A = lhs(r, size=9)
            B = rhs(r, u[1:-1], bcz, t, h, k, size=9)
            u[1:-1] = np.linalg.solve(A, B)
        print("t:", t)
        plt.plot(u)
        plt.show()


if __name__ == "__main__":
    unittest.main()
