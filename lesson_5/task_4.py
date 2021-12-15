# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.






def write_file(file_name: str, file_data: dict, encoding: str):
    with open(file_name, 'w', encoding=encoding) as wf:
        for key, value in file_data.items():
            wf.write(f'{key}: {value}\n')


def file_read(file_name: str, encoding: str) -> str:
    with open(file_name, 'r', encoding=encoding) as fr:
        data = fr.read()
    return data


def parce(input_string: str) -> dict:
    work_str = input_string.split('\n')
    result_dict = {}
    for row in work_str:
        try:
            result_dict[row.split(': ')[0]] = row.split(': ')[1]
        except:
            pass
    return result_dict



def key_replace(source_dict: dict, compare_dict: dict) -> dict:
    result_dict = {}
    for key, value in source_dict.items():
        try:
            result_dict[compare_dict[key]] = value
        except:
            print('В словаре агл-рус числительных не найдено такого слова!')
    return result_dict


def main():
    example_dict = {
        'One': '1',
        'Two': '2',
        'Three': '3',
        'Four': '4',
    }

    compare_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
    }

    source_file_name = 'task_4.txt'
    encoding = 'UTF-8'
    result_file_name = 'task_4_result.txt'

    # если лень делать файлик:
    write_file(source_file_name, example_dict, encoding)

    write_file(result_file_name, key_replace(parce(file_read(source_file_name, encoding)), compare_dict), encoding)


if __name__ == '__main__':
    main()
