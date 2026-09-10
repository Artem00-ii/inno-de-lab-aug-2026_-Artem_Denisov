# Исходные данные пользователя.
# В реальных данных могут встречаться лишние пробелы
# и неправильный регистр букв.
raw_name = "  artem denisov  "
raw_email = "  ARTEM.DENISOV@EXAMPLE.COM  "
raw_phone = " +375-29-123-45-67 "

# Убираем лишние пробелы в начале и конце строки.
name = raw_name.strip()
email = raw_email.strip()
phone = raw_phone.strip()

# Разделяем имя и фамилию на отдельные элементы списка.
name_parts = name.split()

# Приводим каждое слово имени к нормальному виду.
# title() делает первую букву каждого слова заглавной.
name_parts = [part.title() for part in name_parts]

# Снова объединяем имя и фамилию в одну строку.
full_name = " ".join(name_parts)

# Приводим email к нижнему регистру,
# чтобы он имел единый формат.
email = email.lower()

# Убираем дефисы из номера телефона.
phone = phone.replace("-", "")

# Получаем код страны из номера телефона.
country_code = phone[:4]

# Получаем имя пользователя из email.
username = email.split("@")[0]

# Создаём итоговую запись пользователя
# с помощью f-строки.
user_record = (
    f"Пользователь: {full_name}; "
    f"Username: {username}; "
    f"Email: {email}; "
    f"Телефон: {phone}; "
    f"Код страны: {country_code.upper()}"
)

# Выводим результат.
print(user_record)