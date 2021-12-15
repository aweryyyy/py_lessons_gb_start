# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# вариант решения без reduce
print(sum((number for number in range(100, 1000 + 1) if number % 2 == 0)), ' вариант решения без reduce, в одну строчку')


# вариант 1 решения с помощью reduce()
from functools import reduce
gen_list = (number for number in range(100, 1000 + 1) if number % 2 == 0)
print(reduce(lambda x, y: x + y, gen_list), ' вариант решения с помощью reduce(), в две строчки')

# вариант 2 решения с помощью reduce()
print(reduce(lambda x, y: x + y, (number for number in range(100, 1000 + 1) if number % 2 == 0)), ' вариант решения с помощью reduce(), в одну строчку')
