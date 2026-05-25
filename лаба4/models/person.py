"""Задание 1.2 — Человек (имя-строка + рост)."""

from __future__ import annotations


class Person:
    """Сущность Человек с именем (строка) и ростом (целое число)."""

    def __init__(self, name: str, height: int) -> None:
        self._name = name
        self._height = height

    @property
    def name(self) -> str:
        """Имя человека."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def height(self) -> int:
        """Рост человека."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value

    def __str__(self) -> str:
        return f"{self._name}, рост: {self._height}"
