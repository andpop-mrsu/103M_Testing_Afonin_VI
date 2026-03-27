"""Модульные тесты для get_triangle_type."""

from __future__ import annotations

import unittest

from triangle_func import IncorrectTriangleSides, get_triangle_type


class GetTriangleTypeTestCase(unittest.TestCase):
    def test_returns_nonequilateral_for_scalene_triangle(self) -> None:
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_returns_isosceles_for_two_equal_sides(self) -> None:
        self.assertEqual(get_triangle_type(3, 3, 2), "isosceles")

    def test_returns_equilateral_for_three_equal_sides(self) -> None:
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")

    def test_accepts_float_values(self) -> None:
        self.assertEqual(get_triangle_type(2.5, 2.5, 3), "isosceles")

    def test_raises_for_zero_or_negative_sides(self) -> None:
        for invalid_sides in ((0, 2, 2), (-1, 2, 2), (2, -1, 2)):
            with self.subTest(invalid_sides=invalid_sides):
                with self.assertRaises(IncorrectTriangleSides):
                    get_triangle_type(*invalid_sides)

    def test_raises_for_triangle_inequality_violation(self) -> None:
        for invalid_sides in ((1, 2, 3), (1, 1, 3), (10, 1, 1)):
            with self.subTest(invalid_sides=invalid_sides):
                with self.assertRaises(IncorrectTriangleSides):
                    get_triangle_type(*invalid_sides)

    def test_raises_for_non_numeric_values(self) -> None:
        for invalid_sides in (("3", 4, 5), (True, 2, 2), (3, None, 4)):
            with self.subTest(invalid_sides=invalid_sides):
                with self.assertRaises(IncorrectTriangleSides):
                    get_triangle_type(*invalid_sides)


if __name__ == "__main__":
    unittest.main()
