# Список транзакций, полученных от платёжного шлюза.
# Каждая строка имеет формат: СТАТУС:СУММА.
raw_transactions = [
    "SUCCESS:100",
    "FAILED:50",
    "SUCCESS:-10",
    "SUCCESS:0",
    "SUCCESS:250",
    "ERROR:200"
]

# С помощью одного List Comprehension:
# 1. Разделяем каждую строку на статус и сумму.
# 2. Оставляем только транзакции со статусом SUCCESS.
# 3. Проверяем, что сумма положительная.
# 4. Преобразуем сумму в целое число.
clean_transactions = [
    int(transaction.split(":")[1])
    for transaction in raw_transactions
    if transaction.split(":")[0] == "SUCCESS"
    and int(transaction.split(":")[1]) > 0
]

# Выводим очищенный список транзакций.
print(f"Очищенные транзакции: {clean_transactions}")