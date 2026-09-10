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

# Безопасно получаем host и port из словаря connection.
host = connection.get("host", "localhost")
port = connection.get("port", 5432)

# Безопасно получаем настройки SSL непосредственно
# из основного словаря db_config.
# Если ключ ssl_settings отсутствует,
# используем пустой словарь.
ssl_settings = db_config.get("ssl_settings", {})

# Получаем режим SSL из словаря ssl_settings.
# Если параметр ssl_mode отсутствует,
# используем значение verify-full.
ssl_mode = ssl_settings.get("ssl_mode", "verify-full")

# Изменяем пользователя базы данных на admin.
connection["user"] = "admin"

# Добавляем максимальное количество соединений.
connection["max_connections"] = 100

# Выводим режим SSL.
print(f"SSL Mode: {ssl_mode}")

# Выводим параметры подключения.
print("Параметры соединения:")

# Перебираем обновлённый словарь через метод .items().
for key, value in connection.items():
    print(f"* {key}: {value}")