"""Задание 5.5 — Дробь (числитель / знаменатель)."""

from __future__ import annotations


class Fraction:
    """Дробь с числителем и знаменателем.

    Поддерживает сложение, вычитание, умножение, деление
    с другой дробью или целым числом.
    Результат каждой операции — новая дробь.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self._numerator = numerator
        self._denominator = denominator
        self._reduce()

    @property
    def numerator(self) -> int:
        """Числитель дроби."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Знаменатель дроби."""
        return self._denominator

    # ---- внутренние методы ----

    @staticmethod
    def _gcd(a: int, b: int) -> int:
        """Наибольший общий делитель (алгоритм Евклида)."""
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a

    def _reduce(self) -> None:
        """Сокращение дроби и нормализация знака."""
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator
        g = self._gcd(self._numerator, self._denominator)
        if g > 1:
            self._numerator //= g
            self._denominator //= g

    def _to_fraction(self, other: Fraction | int) -> Fraction:
        """Преобразовать целое число в дробь, если нужно."""
        if isinstance(other, int):
            return Fraction(other, 1)
        if isinstance(other, Fraction):
            return other
        raise TypeError(
            f"Неподдерживаемый тип: {type(other)}"
        )

    # ---- арифметика ----

    def sum(self, other: Fraction | int) -> Fraction:
        """Сложение: возвращает новую дробь."""
        other = self._to_fraction(other)
        num = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        den = self._denominator * other._denominator
        return Fraction(num, den)

    def minus(self, other: Fraction | int) -> Fraction:
        """Вычитание: возвращает новую дробь."""
        other = self._to_fraction(other)
        num = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        den = self._denominator * other._denominator
        return Fraction(num, den)

    def mul(self, other: Fraction | int) -> Fraction:
        """Умножение: возвращает новую дробь."""
        other = self._to_fraction(other)
        return Fraction(
            self._numerator * other._numerator,
            self._denominator * other._denominator,
        )

    def div(self, other: Fraction | int) -> Fraction:
        """Деление: возвращает новую дробь."""
        other = self._to_fraction(other)
        if other._numerator == 0:
            raise ValueError("Деление на ноль")
        return Fraction(
            self._numerator * other._denominator,
            self._denominator * other._numerator,
        )

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"
