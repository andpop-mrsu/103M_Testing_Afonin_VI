"""Реализация класса Triangle."""

from __future__ import annotations

from dataclasses import dataclass

from triangle_func import get_triangle_type, validate_triangle_sides


@dataclass(frozen=True, slots=True)
class Triangle:
    """Представление корректного треугольника."""

    a: float
    b: float
    c: float

    def __post_init__(self) -> None:
        """Проверить и нормализовать стороны после создания экземпляра."""
        first, second, third = validate_triangle_sides(self.a, self.b, self.c)
        object.__setattr__(self, "a", first)
        object.__setattr__(self, "b", second)
        object.__setattr__(self, "c", third)

    def triangle_type(self) -> str:
        """Вернуть тип треугольника."""
        return get_triangle_type(self.a, self.b, self.c)

    def perimeter(self) -> float:
        """Вернуть периметр треугольника."""
        return self.a + self.b + self.c
