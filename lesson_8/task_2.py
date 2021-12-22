# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDivisionCustom(Exception):
    def __init__(self, *args):
        pass

    def __str__(self):
        return 'Ошибка деления на нуль'

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))

try:
    a / b
except Exception as e:
    raise ZeroDivisionCustom
finally:
    print('pass')
