# Конфигурационный словарь, полученный от сервиса инициализации.
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# Получаем вложенный словарь с параметрами подключения.
connection = db_config.get("connection", {})

# Безопасно получаем host и port.
# Если ключ отсутствует, используются резервные значения.
host = connection.get("host", "localhost")
port = connection.get("port", 5432)

# Получаем настройки SSL.
# Если ключ ssl_settings отсутствует, используется пустой словарь.
ssl_settings = connection.get("ssl_settings", {})

# Получаем режим SSL.
# Если ssl_mode отсутствует, используется значение verify-full.
ssl_mode = ssl_settings.get("ssl_mode", "verify-full")

# Изменяем пользователя базы данных на admin.
connection["user"] = "admin"

# Добавляем максимальное количество соединений.
connection["max_connections"] = 100

# Выводим режим SSL.
print(f"SSL Mode: {ssl_mode}")

# Выводим параметры подключения.
print("Параметры соединения:")

# Перебираем обновлённый словарь через .items().
for key, value in connection.items():
    print(f"* {key}: {value}")