"""Вспомогательные функции (проверка ввода)."""


def input_int(prompt: str) -> int:
    """Запрос целого числа с проверкой корректности ввода."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Введите целое число.")


def input_non_zero_int(prompt: str) -> int:
    """Запрос ненулевого целого числа."""
    while True:
        value = input_int(prompt)
        if value != 0:
            return value
        print("Ошибка! Число не может быть равно нулю.")
