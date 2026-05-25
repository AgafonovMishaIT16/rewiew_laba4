"""Задание 2.2 — Человек с именем (имя как объект Name)."""

from __future__ import annotations

from .name import Name


class PersonWithName:
    """Человек, чьё имя задаётся объектом Name."""

    def __init__(self, name: Name, height: int) -> None:
        self._name = name
        self._height = height

    @property
    def name(self) -> Name:
        """Имя человека (объект Name)."""
        return self._name

    @name.setter
    def name(self, value: Name) -> None:
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
