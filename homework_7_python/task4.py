# Список ролей, переданный в запросе на авторизацию.
# В списке есть повторяющиеся роли.
requested_roles = [
    "guest",
    "developer",
    "guest",
    "admin",
    "developer",
    "guest"
]

# Набор обязательных ролей для выполнения
# административных функций.
required_admin_roles = {
    "admin",
    "security_officer",
    "audit_manager"
}

# Преобразуем список в множество.
# Множество автоматически удаляет все дубликаты.
unique_requested_roles = set(requested_roles)

# Находим роли, которые одновременно присутствуют
# среди запрошенных и обязательных административных ролей.
common_admin_roles = unique_requested_roles & required_admin_roles

# Находим обязательные административные роли,
# которые пользователь не запросил.
missing_admin_roles = required_admin_roles - unique_requested_roles

# Проверяем наличие security_officer в множестве
# с помощью оператора in.
has_security_officer = "security_officer" in unique_requested_roles

# Выводим результаты аудита.
print(f"Уникальные запрошенные роли: {unique_requested_roles}")
print(f"Общие административные роли: {common_admin_roles}")
print(f"Недостающие административные роли: {missing_admin_roles}")
print(
    f"Наличие роли security_officer в запросе: "
    f"{has_security_officer}"
)