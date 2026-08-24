import random

secret_number = random.randint(1, 20)
attempts = 5

print("Я загадал число от 1 до 20. У тебя 5 попыток!")

while attempts > 0:
    guess = int(input("Твоя догадка: "))
    attempts -= 1

    if guess == secret_number:
        print("Поздравляю! Ты угадал!")
        break
    elif guess > secret_number:
        print("Слишком много!")
    else:
        print("Слишком мало!")

    print(f"Осталось попыток: {attempts}")

if attempts == 0 and guess != secret_number:
    print(f"Попытки закончились. Я загадал число {secret_number}.")