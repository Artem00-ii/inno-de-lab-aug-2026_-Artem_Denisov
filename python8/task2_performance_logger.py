import time
from typing import Any, Callable


# Префикс для сообщений о производительности.
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"

# Количество знаков после запятой для времени выполнения.
TIME_DECIMALS = 8


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Измеряет и выводит время выполнения функции.

    Args:
        func: Функция, выполнение которой необходимо измерить.

    Returns:
        Обёрнутую функцию с измерением времени выполнения.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Запоминаем время начала выполнения функции.
        start_time = time.perf_counter()

        # Выполняем оригинальную функцию
        # с любыми позиционными и именованными аргументами.
        result = func(*args, **kwargs)

        # Вычисляем продолжительность выполнения.
        execution_time = time.perf_counter() - start_time

        # Выводим информацию о производительности.
        print(
            f"{PERFORMANCE_LOG_PREFIX} "
            f"Функция '{func.__name__}' выполнена "
            f"за {execution_time:.{TIME_DECIMALS}f} сек."
        )

        # Возвращаем результат оригинальной функции.
        return result

    return wrapper


@performance_logger
def get_sorted_report(
    revenue_data: list[dict[str, str | float]]
) -> list[dict[str, str | float]]:
    """Сортирует категории по убыванию выручки.

    Args:
        revenue_data: Список словарей с названием категории
            и общей выручкой.

    Returns:
        Список категорий, отсортированный по убыванию
        значения total_sales.
    """

    # Сортируем список по ключу total_sales
    # от большего значения к меньшему.
    return sorted(
        revenue_data,
        key=lambda item: item["total_sales"],
        reverse=True
    )


# Набор 1 — стандартный.
report_1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]

# Набор 2 — две категории имеют одинаковую выручку.
report_2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]

# Набор 3 — только одна категория.
report_3 = [
    {"category": "Drama", "total_sales": 500.00}
]


print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")


print("--- ТЕСТ 1 ---")

sorted_report_1 = get_sorted_report(report_1)

print("Топ категорий по выручке:")

for index, item in enumerate(sorted_report_1, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")


print("--- ТЕСТ 2 ---")

sorted_report_2 = get_sorted_report(report_2)

print("Топ категорий по выручке:")

for index, item in enumerate(sorted_report_2, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")


print("--- ТЕСТ 3 ---")

sorted_report_3 = get_sorted_report(report_3)

print("Топ категорий по выручке:")

for index, item in enumerate(sorted_report_3, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")