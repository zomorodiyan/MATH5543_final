import unittest
from area.circle import circle_area
import numpy as np
import pytest


class TestCircleAre(unittest.TestCase):
    def test_area(self):  # function's name have to start with "test_"
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), np.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), np.pi * 2.1 ** 2)

    @pytest.mark.skip(reason="how to skip test")
    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -3)
        # another way to write the line above:
        with self.assertRaises(ValueError):
            circle_area(-3)

    def test_types(self):
        # Make sure type error raised when necessary
        self.assertRaises(TypeError, circle_area, 3 + 5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
        # another way to write the 3 lines above:
        with self.assertRaises(TypeError):
            circle_area(3 + 5j)
        with self.assertRaises(TypeError):
            circle_area(True)
        with self.assertRaises(TypeError):
            circle_area("radius")


# list of all asserts:
# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIs(a, b)
# assertIsNot(a, b)
# assertIsNone(x)
# assertIsNotNone(x)
# assertIn(a, b)
# assertNotIn(a, b)
# assertIsInstance(a, b)
# assertNotIsInstance(a, b)

# to be able to run unittests using $ python test_file.py
# instead of $ python -m unittest test_file.py
if __name__ == "__main__":
    unittest.main()
