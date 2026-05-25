"""Задание 1.3 — Имя (Фамилия, Личное имя, Отчество)."""

from __future__ import annotations


class Name:
    """Сущность Имя: Фамилия, Личное имя, Отчество.

    Любой из параметров может быть не задан (None).
    При приведении к строке незаданные параметры пропускаются.
    """

    def __init__(
        self,
        last_name: str | None = None,
        first_name: str | None = None,
        patronymic: str | None = None,
    ) -> None:
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic

    @property
    def last_name(self) -> str | None:
        """Фамилия."""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str | None) -> None:
        self._last_name = value

    @property
    def first_name(self) -> str | None:
        """Личное имя."""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str | None) -> None:
        self._first_name = value

    @property
    def patronymic(self) -> str | None:
        """Отчество."""
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value: str | None) -> None:
        self._patronymic = value

    def __str__(self) -> str:
        parts = [
            p for p in (
                self._last_name,
                self._first_name,
                self._patronymic,
            )
            if p
        ]
        return " ".join(parts)
