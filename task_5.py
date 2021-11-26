# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# raiting_score = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
raiting_score = [7, 5, 3, 3, 2]
# будем спрашивать у юзера - закончен ли ввод
user_answer = 0


while user_answer == 0:
    print(f'Текущий Рейтинг: {raiting_score}')
    user_score_input = int(input('Введите новое значение: '))
    raiting_score.append(user_score_input)
    raiting_score.sort(reverse=True)
            # # проверим, есть ли аналогичные значения
            # if raiting_score.count(user_score_input) > 0:
            #     # найдём место аналогичного значения, которое уже есть в списке рейтинга и запишем правее от этого значения
            #     raiting_score.insert(raiting_score.index(user_score_input), user_score_input)
            # else:
            #     raiting_score.append(user_score_input)
            #     raiting_score.sort(reverse=True)
    print(f'Текущий Рейтинг: {raiting_score}')

    user_answer = int(input('Ввод завершён? 1 - да, 0 - нет: '))
else:
    print(f'Итоговый Рейтинг: {raiting_score}')
