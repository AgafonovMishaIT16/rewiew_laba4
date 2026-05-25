"""Задание 3.3 — Город / Задание 4.8 — Создаём Города."""

from __future__ import annotations


class City:
    """Город с названием и набором путей к другим городам.

    Путь — пара (город, стоимость).
    """

    def __init__(self, name: str) -> None:
        self._name = name
        self._routes: list[tuple[City, int]] = []

    @property
    def name(self) -> str:
        """Название города."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def routes(self) -> list[tuple[City, int]]:
        """Список путей (город, стоимость)."""
        return self._routes

    def add_route(self, city: City, cost: int) -> None:
        """Добавить путь к городу с указанной стоимостью."""
        self._routes.append((city, cost))

    def __str__(self) -> str:
        if not self._routes:
            return f"{self._name}: нет путей"
        routes_str = ", ".join(
            f"{city.name}:{cost}"
            for city, cost in self._routes
        )
        return f"{self._name}: [{routes_str}]"


class CityV2:
    """Улучшенная версия города.

    Можно создать указав только название,
    либо название + набор путей.
    """

    def __init__(
        self,
        name: str,
        *routes: tuple[CityV2, int],
    ) -> None:
        self._name = name
        self._routes: list[tuple[CityV2, int]] = list(routes)

    @property
    def name(self) -> str:
        """Название города."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def routes(self) -> list[tuple[CityV2, int]]:
        """Список путей (город, стоимость)."""
        return self._routes

    def add_route(self, city: CityV2, cost: int) -> None:
        """Добавить путь к городу с указанной стоимостью."""
        self._routes.append((city, cost))

    def __str__(self) -> str:
        if not self._routes:
            return f"{self._name}: нет путей"
        routes_str = ", ".join(
            f"{city.name}:{cost}"
            for city, cost in self._routes
        )
        return f"{self._name}: [{routes_str}]"
