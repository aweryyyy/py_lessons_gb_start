# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# создадим список для ввода:
user_list = []
# будем спрашивать у юзера - закончен ли ввод
user_answer = 0

# создадим конечный список
return_list = []

while user_answer == 0:
    user_list.append(input('Введите значение: '))
    user_answer = int(input('Ввод завершён? 1 - да, 0 - нет: '))
else:
    for index, element in enumerate(user_list):
        # если элемент в списке нечётный
        if index % 2 != 0:
            # если всего в списке нечётное кол-во эл-тов и мы попадаем в последний элемент
            if len(user_list) % 2 != 0 and len(user_list) - 1 == index:
                # тащим в список в изначальной позиции
                return_list.insert(index, element)
            else:
                # переставляем на позицию чётную, предыдущию
                return_list.insert(index - 1, element)
        else:
            # четные - тащим на позицию нечётного (двигаем вправо)
            return_list.insert(index + 1, element)
        # print(f'{index} - {element}')
print(f'Введен список: {user_list}')
print(f'Итоговый список: {return_list}')
