# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def user_input(input_placeholder):
    data_input = []
    while '' not in data_input:
        data_input.append(input(input_placeholder))
    return data_input



def file_writer(filename, file_data):
    with open(filename, 'w') as file:
        file.write('\n'.join(file_data))


def main():
    # config
    file_name = 'task_1.txt'
    input_placeholder = 'Введите данные для записи в файл: '
    # work here
    user_data = user_input(input_placeholder)
    file_writer(file_name, user_data)

    print(f'Done! Check file - {file_name}')


if __name__ == '__main__':
    main()
