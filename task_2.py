# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def set_user_data_short(**kwargs) -> dict:
    """
    Принимает именованые аргументы, пример example_key=example_value
    Возвращает все значения как текст.
    """
    result = ''
    for key, value in kwargs.items():
        result += str(key) + ' - ' + str(value) + '\n'
    return result


print(set_user_data_short(first_name='Вася', last_name='Петров', birtday_year=1980, city='Астрахань',
                          email='va_pet@not_exist.ru', phone=88005553535))
