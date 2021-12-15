# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(value: float, power: int) -> float:
    """
    Функция возведения в степень power числа value
    value - float, для value = 0 и power < 0 value = 1
    power - int, может быть положительным и отрицательным, но не может быть дробным
    """
    local_power = power * -1 if power < 0 else power
    if power < 0:
        result = 1 / value if value != 0 else 1
    else:
        result = value
    while local_power > 1:
        if power < 0:
            result /= value if value != 0 else 1
        else:
            result *= value
        local_power -= 1
    return result


print(my_func(0.2, -5))
print(0.2 ** -5)
# не работает:
#     print(my_func(2, -0.5))
#     print(2 ** -0.5)
print(my_func(0.2, 5))
print(0.2 ** 5)
