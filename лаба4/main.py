"""Лабораторная работа №2 — ООП. Вариант 2.

Задания: 1(2,3), 2(2), 3(3), 4(8), 5(5).
Точка входа: демонстрация работы всех классов.
"""

import os
import sys

# Гарантируем, что Python ищет модули относительно папки скрипта,
# а не относительно текущего рабочего каталога.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import (  # noqa: E402
    City,
    CityV2,
    Fraction,
    Name,
    Person,
    PersonWithName,
)
from utils import input_int, input_non_zero_int

SEP = "=" * 60


# ---- демонстрационные функции ----


def demo_task_1_2() -> None:
    """Задание 1.2 — Человек."""
    print(SEP)
    print("ЗАДАНИЕ 1.2 — Человек")
    print(SEP)

    people = [
        Person("Клеопатра", 152),
        Person("Пушкин", 167),
        Person("Владимир", 189),
    ]
    for person in people:
        print(person)


def demo_task_1_3() -> list[Name]:
    """Задание 1.3 — Имена."""
    print(f"\n{SEP}")
    print("ЗАДАНИЕ 1.3 — Имена")
    print(SEP)

    names = [
        Name(first_name="Клеопатра"),
        Name(
            last_name="Пушкин",
            first_name="Александр",
            patronymic="Сергеевич",
        ),
        Name(last_name="Маяковский", first_name="Владимир"),
    ]
    for name in names:
        print(name)

    return names


def demo_task_2_2(names: list[Name]) -> None:
    """Задание 2.2 — Человек с именем."""
    print(f"\n{SEP}")
    print("ЗАДАНИЕ 2.2 — Человек с именем")
    print(SEP)

    heights = [152, 167, 189]
    for name, height in zip(names, heights):
        print(PersonWithName(name, height))


def demo_task_3_3() -> None:
    """Задание 3.3 — Города (по схеме рис. 2)."""
    print(f"\n{SEP}")
    print("ЗАДАНИЕ 3.3 — Города")
    print(SEP)

    a, b, c, d, e, f = (City(ch) for ch in "ABCDEF")

    a.add_route(f, 1)
    a.add_route(b, 5)
    f.add_route(b, 1)
    f.add_route(e, 6)
    f.add_route(c, 2)
    b.add_route(c, 3)
    e.add_route(d, 2)
    c.add_route(d, 4)

    for city in (a, b, c, d, e, f):
        print(city)


def demo_task_4_8() -> None:
    """Задание 4.8 — Создаём Города (CityV2)."""
    print(f"\n{SEP}")
    print("ЗАДАНИЕ 4.8 — Создаём Города (улучшенная версия)")
    print(SEP)

    a, b, c, d, e, f = (CityV2(ch) for ch in "ABCDEF")

    a.add_route(f, 1)
    a.add_route(b, 5)
    f.add_route(b, 1)
    f.add_route(e, 6)
    f.add_route(c, 2)
    b.add_route(c, 3)
    e.add_route(d, 2)
    c.add_route(d, 4)

    print("Города с добавлением путей после создания:")
    for city in (a, b, c, d, e, f):
        print(city)

    print("\nСоздание города с путями через конструктор:")
    test = CityV2("TestCity", (a, 10), (b, 20))
    print(test)


def demo_task_5_5() -> None:
    """Задание 5.5 — Дроби."""
    print(f"\n{SEP}")
    print("ЗАДАНИЕ 5.5 — Дроби")
    print(SEP)

    f1 = Fraction(1, 3)
    f2 = Fraction(2, 3)
    f3 = Fraction(3, 4)

    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f3 = {f3}")

    # Примеры каждой операции
    print(f"\n{f1} + {f2} = {f1.sum(f2)}")
    print(f"{f2} - {f1} = {f2.minus(f1)}")
    print(f"{f1} * {f2} = {f1.mul(f2)}")
    print(f"{f1} / {f2} = {f1.div(f2)}")

    # Операции с целым числом
    print(f"\n{f1} + 5 = {f1.sum(5)}")
    print(f"{f2} * 3 = {f2.mul(3)}")

    # Цепочка: f1.sum(f2).div(f3).minus(5)
    chain = f1.sum(f2).div(f3).minus(5)
    print(f"\nЦепочка: ({f1} + {f2}) / {f3} - 5 = {chain}")

    step1 = f1.sum(f2)
    step2 = step1.div(f3)
    step3 = step2.minus(5)
    print("Пошагово:")
    print(f"  {f1} + {f2} = {step1}")
    print(f"  {step1} / {f3} = {step2}")
    print(f"  {step2} - 5 = {step3}")


def demo_interactive() -> None:
    """Интерактивный ввод с проверкой."""
    print(f"\n{SEP}")
    print("ИНТЕРАКТИВНЫЙ ВВОД")
    print(SEP)

    print("\nСоздание Человека с клавиатуры:")
    name = input("Введите имя: ").strip()
    height = input_int("Введите рост (целое число): ")
    print(f"Создан: {Person(name, height)}")

    print("\nСоздание Дроби с клавиатуры:")
    num = input_int("Введите числитель: ")
    den = input_non_zero_int("Введите знаменатель (не 0): ")
    print(f"Создана дробь: {Fraction(num, den)}")


def main() -> None:
    """Главная функция — запуск всех демонстраций."""
    demo_task_1_2()
    names = demo_task_1_3()
    demo_task_2_2(names)
    demo_task_3_3()
    demo_task_4_8()
    demo_task_5_5()
    demo_interactive()


if __name__ == "__main__":
    main()
