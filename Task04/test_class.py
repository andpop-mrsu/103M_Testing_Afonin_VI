"""Набор pytest-тестов для класса Triangle."""

from __future__ import annotations

import pytest

from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides


@pytest.mark.parametrize(
    ("sides", "expected_type"),
    [
        ((3, 4, 5), "nonequilateral"),
        ((3, 3, 2), "isosceles"),
        ((5, 5, 5), "equilateral"),
        ((2.5, 2.5, 3), "isosceles"),
    ],
)
def test_triangle_type_returns_expected_value(sides: tuple[float, float, float], expected_type: str) -> None:
    triangle = Triangle(*sides)
    assert triangle.triangle_type() == expected_type


@pytest.mark.parametrize(
    ("sides", "expected_perimeter"),
    [
        ((3, 4, 5), 12.0),
        ((3, 3, 2), 8.0),
        ((2.5, 2.5, 3), 8.0),
    ],
)
def test_perimeter_returns_sum_of_sides(
    sides: tuple[float, float, float], expected_perimeter: float
) -> None:
    triangle = Triangle(*sides)
    assert triangle.perimeter() == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "invalid_sides",
    [
        (0, 2, 2),
        (-1, 2, 2),
        (1, 2, 3),
        (1, 1, 3),
        ("3", 4, 5),
        (True, 2, 2),
    ],
)
def test_invalid_sides_raise_exception(invalid_sides: tuple[object, object, object]) -> None:
    with pytest.raises(IncorrectTriangleSides):
        Triangle(*invalid_sides)
