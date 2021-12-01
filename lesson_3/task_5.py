# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def user_input(num_spacer: str) -> str:
    """
    Чисто ввод данных юзером, получаем строку, преобразуем в список
    Возвращаем список
    """
    data = input('Введите числа, разделяя пробелами: ')
    return data.split(num_spacer)


def summarize(data_list: list, spec_symb: str) -> int:
    """
    Суммируем все похожие на числа значения из data_list.
    Если натыкаемся на spec_symb - суммируем всё, что было до spec_symb, но не после
    Возвращаем число - сумму.
    """
    data_numbers = []
    total_sum = 0
    for num in data_list:
        if num.isdigit():
            data_numbers.append(int(num))
            total_sum += int(num)
        elif num == spec_symb:
            break
    return total_sum


def main():
    """
    Основная функция программы.
    конфиг:
    special_symbol - символ выхода из программы
    num_spacer - разделитель для ввода данных
    storage - хранилище ваще всех данных, что ввёл юзер

    логика:
    крутим цикл, пока в списке, введённом юзером не увидим special_symbol
    выводим сумму всех чисел до special_symbol
    выводим весь storage
    """
    special_symbol = 'q'
    num_spacer = ' '
    storage = []
    while special_symbol not in storage:
        storage.extend(user_input(num_spacer))
        # print(storage)
        print(summarize(storage, special_symbol))
    print('\n' * 2, ', '.join(storage))


main()
