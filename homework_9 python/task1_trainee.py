class Trainee:
    def __init__(
        self,
        name: str,
        surname: str,
        score: int = 0,
        passing_grade: int = 10
    ) -> None:
        self.name = name
        self.surname = surname
        self.passing_grade = passing_grade
        self.__score = 0
        self.score = score

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        if type(value) is not int:
            raise ValueError(
                f"Expected value of type int, got {type(value)}"
            )

        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")

        self.__score = value

    def do_homework(self) -> None:
        self.score += 1

    def miss_homework(self) -> None:
        self.score -= 1

    def visit_lecture(self) -> None:
        self.score += 1

    def miss_lecture(self) -> None:
        self.score -= 1

    @property
    def is_passing(self) -> bool:
        return self.score >= self.passing_grade


# Проверка работы класса
trainee = Trainee("Иван", "Иванов")

print(f"Студент: {trainee.name} {trainee.surname}")
print(f"Начальный балл: {trainee.score}")
print(f"Проходной балл: {trainee.passing_grade}")
print(f"Сдал: {trainee.is_passing}")

trainee.do_homework()
print(f"После выполнения домашнего задания: {trainee.score}")

trainee.visit_lecture()
print(f"После посещения лекции: {trainee.score}")

trainee.miss_homework()
print(f"После пропуска домашнего задания: {trainee.score}")

trainee.miss_lecture()
print(f"После пропуска лекции: {trainee.score}")

print(f"Итоговый балл: {trainee.score}")
print(f"Сдал: {trainee.is_passing}")