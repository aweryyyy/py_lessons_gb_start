# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print(list(gen_num for gen_num in (number for number in range(20, 240 + 1) if number % 20 == 0 or number % 21 == 0)))
