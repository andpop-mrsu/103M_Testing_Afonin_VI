"""Вспомогательные функции для решения квадратных уравнений."""

from __future__ import annotations

import math
from numbers import Real

_EPSILON = 1e-12


def _ensure_real_number(value: Real, name: str) -> float:
    """Преобразовать конечное вещественное значение к float или вызвать ошибку."""
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value):
        raise TypeError(f"{name} должен быть конечным вещественным числом.")
    return float(value)


def _normalize_zero(value: float) -> float:
    """Не возвращать -0.0 для корней, математически равных нулю."""
    if math.isclose(value, 0.0, abs_tol=_EPSILON):
        return 0.0
    return value


def solve_quadratic(a: Real, b: Real, c: Real) -> tuple[float, ...]:
    """
    Вернуть действительные корни ``ax^2 + bx + c = 0`` в порядке возрастания.

    Функция возвращает:
    - пустой кортеж, если действительных корней нет;
    - кортеж из одного элемента для кратного корня;
    - кортеж из двух элементов для двух различных действительных корней.
    """
    a_value = _ensure_real_number(a, "a")
    b_value = _ensure_real_number(b, "b")
    c_value = _ensure_real_number(c, "c")

    if a_value == 0.0:
        raise ValueError("Коэффициент 'a' не должен быть равен нулю.")

    discriminant = b_value * b_value - 4.0 * a_value * c_value

    if discriminant < 0.0 and not math.isclose(discriminant, 0.0, abs_tol=_EPSILON):
        return ()

    if math.isclose(discriminant, 0.0, abs_tol=_EPSILON):
        root = _normalize_zero(-b_value / (2.0 * a_value))
        return (root,)

    sqrt_discriminant = math.sqrt(discriminant)
    first_root = _normalize_zero((-b_value - sqrt_discriminant) / (2.0 * a_value))
    second_root = _normalize_zero((-b_value + sqrt_discriminant) / (2.0 * a_value))
    return tuple(sorted((first_root, second_root)))
