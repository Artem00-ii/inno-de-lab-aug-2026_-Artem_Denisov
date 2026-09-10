# Поток данных телеметрии от серверов кластера.
# Каждый кортеж содержит:
# имя сервера, загрузку CPU, использование RAM и статус.
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]

# Список имён активных серверов.
active_nodes = []

# Список загрузки CPU активных серверов.
cpu_loads = []

# Список использования RAM активных серверов.
ram_usages = []

# Перебираем телеметрию и сразу распаковываем
# каждый кортеж в отдельные переменные.
for node_name, cpu_load, ram_usage, status in system_telemetry:

    # Серверы со статусом offline не учитываем.
    if status == "offline":
        continue

    # Добавляем имя активного сервера.
    active_nodes.append(node_name)

    # Добавляем загрузку CPU.
    cpu_loads.append(cpu_load)

    # Добавляем использование RAM.
    ram_usages.append(ram_usage)

# Считаем количество работающих серверов
# с помощью встроенной функции len().
active_nodes_count = len(active_nodes)

# Рассчитываем среднюю загрузку CPU.
# Суммируем значения через sum() и делим
# на количество активных серверов.
average_cpu = round(sum(cpu_loads) / len(cpu_loads), 2)

# Находим максимальное использование RAM
# с помощью встроенной функции max().
max_ram = max(ram_usages)

# Формируем итоговый вложенный словарь
# с рассчитанными метриками.
telemetry_report = {
    "active_nodes_count": active_nodes_count,
    "metrics": {
        "average_cpu": average_cpu,
        "max_ram": max_ram
    }
}

# Выводим список активных серверов.
print(f"Активные узлы в сети: {active_nodes}")

# Выводим итоговый отчёт.
print("Итоговый отчет телеметрии:")
print(telemetry_report)