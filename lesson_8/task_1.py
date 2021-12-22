# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, date_str: str):
        self.date_str = date_str


    @classmethod
    def date_to_int(cls, date_str: str) -> dict:
        day, month, year = date_str.split('-')
        return {'day': int(day),
                'month': int(month),
                'year': int(year)}

    @staticmethod
    def validate_date(kwargs: dict) -> bool:

        check_dict = {
            1: 31,
            2: 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        def check_leap_year(year: int) -> bool:
            """
            :param year: Номер месяца для проверок
            :return: boolean, является ли год високосным
            """
            return year % 4 == 0

        def check_months(month: int) -> list:
            """
            :param month: Номер месяца для проверок
            :return: список, 0 индекс - если месяц февраль,
                             1 индекс - если месяц чётный
            """
            if month not in range(1, 13):
                raise Exception('В году должно быть 12 месяцев!')
            return [True if month == 2 else False, True if month % 2 == 0 else False]

        def check_day(day: int) -> list:
            """
            :param day: Номер дня для проверок
            :return: список, 0 индекс - если день от 1 до 29 (февраль високосного года)
                             1 индекс - если день от 1 до 28 (февраль невисокосного года)
                             2 индекс - если день от 1 до 30 (чётный месяц)
                             3 индекс - если день от 1 до 31 (нечётный месяц)
            """
            if day < 1:
                raise Exception('День не может быть меньше 0!')

            result_day = [True if day in range(1, 30) else False, True if day in range(1, 29) else False,
                          True if day in range(1, 32) else False, True if day in range(1, 31) else False]

            return result_day

        if kwargs['day'] <= check_dict[kwargs['month']] and kwargs['day'] > 0:
            if check_leap_year(kwargs['year']) and kwargs['month'] == 2:
                if not kwargs['day'] <= 29:
                    raise Exception('В феврале високосного года 29 дней!')
            elif not check_leap_year(kwargs['year']) and kwargs['month'] == 2:
                if not kwargs['day'] <= 28:
                    raise Exception('В феврале не високосного года 28 дней!')
        else:
            raise Exception('Некорректная дата!')

        return True



new_date = Date('28-02-2021')
new_date_in_int = Date.date_to_int(new_date.date_str)
# print(new_date_in_int, type(new_date_in_int['day']), type(new_date_in_int['month']), type(new_date_in_int['year']))
print(new_date.validate_date(new_date_in_int))
