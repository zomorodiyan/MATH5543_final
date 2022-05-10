import unittest
import numpy as np
from fdm.crank_nicolson import three_diagonal
from fdm.crank_nicolson import left_hand_side
from fdm.crank_nicolson import right_hand_side


class Test_Crank_Nicolson(unittest.TestCase):
    def setUp(self):
        # content of this optional method runs before each test in this class
        self.k = 1
        self.h = 1
        self.r = self.k / 2 / self.h ** 2
        self.bl = 1  # boundary condition x=0 t=tn
        self.blp = 1  # leboundary condition x=0 t=tn+1
        self.br = 1  # right boundary condition t=tn
        self.brp = 1  # right boundary condition t=tn+1

    def test_three_diagonal(self):
        np.testing.assert_array_almost_equal(
            three_diagonal(main=1, super=2, size=3),
            np.array([[1, 2, 0], [2, 1, 2], [0, 2, 1]]),
        )

    def test_left_hand_side(self):
        np.testing.assert_array_almost_equal(
            left_hand_side(r=self.r, size=3),
            np.array([[2, -0.5, 0], [-0.5, 2, -0.5], [0, -0.5, 2]]),
        )

    def test_right_hand_side(self):
        u1, u2, u3 = 1, 1, 1
        field = [u1, u2, u3]
        boundaryConditions = [self.bl, self.blp, self.br, self.brp]
        np.testing.assert_array_almost_equal(
            right_hand_side(self.r, field, boundaryConditions, size=3),
            np.array(
                [
                    self.r * (self.bl + self.blp) + (1 - 2 * self.r) * u1 + self.r * u2,
                    self.r * u1 + (1 - 2 * self.r) * u2 + self.r * u3,
                    self.r * u2 + (1 - 2 * self.r) * u3 + self.r * (self.br + self.brp),
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
