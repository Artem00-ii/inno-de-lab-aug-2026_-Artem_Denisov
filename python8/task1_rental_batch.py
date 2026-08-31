# Константа с максимальной суммой партии,
# которая может быть автоматически одобрена.
MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(
    quantity: int,
    rental_rate: float,
    discount: float = 0.0
) -> tuple[float, bool]:
    """Рассчитывает стоимость оптовой партии аренды фильмов.

    Args:
        quantity: Количество дисков в партии.
        rental_rate: Стоимость аренды одного диска.
        discount: Скидка в виде десятичной дроби. По умолчанию 0.0.

    Returns:
        Кортеж из итоговой суммы и признака превышения лимита.
        Первый элемент — итоговая сумма.
        Второй элемент — True, если сумма превышает лимит,
        иначе False.
    """
    # Рассчитываем итоговую стоимость партии
    # с учётом указанной скидки.
    final_sum = round(
        quantity * rental_rate * (1 - discount),
        2
    )

    # Проверяем, превышает ли итоговая сумма
    # установленный лимит.
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    # Возвращаем сумму и результат проверки лимита.
    return final_sum, is_limit_exceeded


# Заголовок отчёта.
print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

# Вызов функции с позиционными аргументами.
batch_1_sum, batch_1_limit = calculate_rental_batch(30, 2.99)

print(
    f"Партия 1 (Academy Dinosaur): "
    f"Сумма {batch_1_sum}$. "
    f"Превышение лимита: {batch_1_limit}"
)

# Вызов функции с именованными аргументами.
batch_2_sum, batch_2_limit = calculate_rental_batch(
    quantity=40,
    rental_rate=4.99,
    discount=0.10
)

print(
    f"Партия 2 (Affair Prejudice): "
    f"Сумма {batch_2_sum}$. "
    f"Превышение лимита: {batch_2_limit}"
)

# Партия 3 без скидки.
batch_3_sum, batch_3_limit = calculate_rental_batch(10, 1.99)

print(
    f"Партия 3 (Agent Truman): "
    f"Сумма {batch_3_sum}$. "
    f"Превышение лимита: {batch_3_limit}"
)

# Партия 4 со скидкой 20%.
batch_4_sum, batch_4_limit = calculate_rental_batch(
    50,
    3.50,
    0.20
)

print(
    f"Партия 4 (African Egg): "
    f"Сумма {batch_4_sum}$. "
    f"Превышение лимита: {batch_4_limit}"
)