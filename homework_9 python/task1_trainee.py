class Trainee:
    def __init__(
        self,
        name: str,
        surname: str,
        score: int = 0,
        passing_grade: int = 10
    ) -> None:
        self.name: str = name
        self.surname: str = surname
        self.passing_grade: int = passing_grade
        self.__score: int = score

    @property
    def score(self) -> int:
        """Returns current trainee score."""
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """Validates and updates trainee score."""
        if not isinstance(value, int):
            raise ValueError(
                f"Expected value of type int, got {type(value)}"
            )

        if value < 0:
            raise ValueError(
                "The score shouldn't be less than 0!"
            )

        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1."""
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1."""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1."""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1."""
        self.score -= 1

    def is_passing(self) -> bool:
        """Checks whether trainee passed the course."""
        return self.score >= self.passing_grade


# Проверка работы класса.

print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")

# Создаем стажера с начальным баллом 9
# и проходным баллом 10.
trainee = Trainee(
    name="Иван",
    surname="Иванов",
    score=9,
    passing_grade=10
)

# Выполняем домашнее задание.
trainee.do_homework()

print(
    f"Баллы: {trainee.score}, "
    f"Прошел курс: {trainee.is_passing()}"
)

# Пропускаем лекцию.
trainee.miss_lecture()

print(
    f"Баллы: {trainee.score}, "
    f"Прошел курс: {trainee.is_passing()}"
)

# Проверяем валидацию отрицательного значения.
try:
    trainee.score = -5
except ValueError as error:
    print(f"Ошибка: {error}")