# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = ''
    surname = ''
    position = ''
    __income = {
        'wage': 0.0,
        'bonus': 0.0,
    }

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_income(self) -> dict:
        return self.__income

    def set_income(self, income: dict):
        self.__income = income


class Position(Worker):
    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'


    def get_total_income(self):
        return sum(map(float, self.get_income().values()))


hr = Position('Ann', 'Snow', 'HR', {'wage': 30, 'bonus': 4})
print(hr.get_full_name())
print(hr.get_total_income())
print(hr.position, hr.surname, hr.name, hr._Worker__income, hr.get_income())
