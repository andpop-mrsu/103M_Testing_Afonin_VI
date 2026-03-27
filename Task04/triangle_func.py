"""Вспомогательные функции для классификации треугольников.

>>> get_triangle_type(3, 4, 5)
'nonequilateral'
>>> get_triangle_type(3, 3, 2)
'isosceles'
>>> get_triangle_type(5, 5, 5)
'equilateral'
>>> get_triangle_type(1, 1, 3)
Traceback (most recent call last):
...
triangle_func.IncorrectTriangleSides: Стороны треугольника должны быть конечными положительными числами и удовлетворять неравенству треугольника.
"""

from __future__ import annotations

import math
from numbers import Real

ERROR_MESSAGE = (
    "Стороны треугольника должны быть конечными положительными числами "
    "и удовлетворять неравенству треугольника."
)


class IncorrectTriangleSides(ValueError):
    """Исключение для набора сторон, который не образует корректный треугольник."""


def validate_triangle_sides(a: Real, b: Real, c: Real) -> tuple[float, float, float]:
    """Проверить стороны треугольника и вернуть их как значения float."""
    sides = []
    for side in (a, b, c):
        if isinstance(side, bool) or not isinstance(side, Real) or not math.isfinite(side):
            raise IncorrectTriangleSides(ERROR_MESSAGE)
        side_value = float(side)
        if side_value <= 0.0:
            raise IncorrectTriangleSides(ERROR_MESSAGE)
        sides.append(side_value)

    first, second, third = sides
    if first + second <= third or first + third <= second or second + third <= first:
        raise IncorrectTriangleSides(ERROR_MESSAGE)

    return first, second, third


def get_triangle_type(a: Real, b: Real, c: Real) -> str:
    """Определить тип треугольника по длинам его сторон."""
    first, second, third = validate_triangle_sides(a, b, c)
    unique_side_count = len({first, second, third})

    if unique_side_count == 1:
        return "equilateral"
    if unique_side_count == 2:
        return "isosceles"
    return "nonequilateral"
