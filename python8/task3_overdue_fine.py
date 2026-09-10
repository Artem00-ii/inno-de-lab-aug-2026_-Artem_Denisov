from typing import Any


# Базовое значение для расчёта индекса возврата.
DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
    film_title: str,
    days_overdue: Any,
    fine_rate: float
) -> tuple[float, float] | None:
    """Рассчитывает штраф за просрочку и индекс оборачиваемости.

    Args:
        film_title: Название фильма.
        days_overdue: Количество дней просрочки.
        fine_rate: Размер штрафа за один день.

    Returns:
        Кортеж из итогового штрафа и индекса оборачиваемости.
        Возвращает None, если входные данные некорректны.

    Обрабатываемые ошибки:
        TypeError: если days_overdue имеет неподходящий тип.
        ValueError: если days_overdue нельзя преобразовать в число.
        ZeroDivisionError: если количество дней просрочки равно нулю.
    """
    try:
        numeric_days = float(days_overdue)

        total_fine = numeric_days * fine_rate

        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        # Выводим успешный результат до выполнения finally.
        print(
            f"Фильм: '{film_title}' | "
            f"Итоговый штраф: {round(total_fine, 2)}$ | "
            f"Индекс: {round(return_index, 2)}"
        )

        return round(total_fine, 2), round(return_index, 2)

    except TypeError as error:
        print(
            f"[ОШИБКА ТИПА] Некорректный тип данных "
            f"для '{film_title}': {error}"
        )
        return None

    except ValueError as error:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать "
            f"дни в число для '{film_title}': {error}"
        )
        return None

    except ZeroDivisionError as error:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без "
            f"просрочки для '{film_title}': {error}"
        )
        return None

    finally:
        print("--- Проверка транзакции возврата завершена ---")


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")


# Успешный расчёт.
calculate_overdue_fine("Matrix", 5, 1.5)


# Ошибка ValueError.
calculate_overdue_fine("Inception", "пять", 2.0)


# Ошибка ZeroDivisionError.
calculate_overdue_fine("Avatar", 0, 2.5)


# Ошибка TypeError.
calculate_overdue_fine("Interstellar", [3], 3.0)