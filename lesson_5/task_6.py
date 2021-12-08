# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
#
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def read_file(file_name: str, encoding='UTF-8'):
    with open(file_name, 'r', encoding=encoding) as fr:
        result = fr.read()
    return result


def parse(source_data: str, skip_value='—', in_row_delimeter=': ', in_row_value_delimeter='('):
    result = {}
    for row in source_data.split('\n'):
        try:
            work_list = []
            for row_value in row.split(in_row_delimeter)[1].split(' '):
                if skip_value in row_value:
                    work_list.append(0)
                elif row_value.find(in_row_value_delimeter) != -1:
                    work_list.append(int(row_value[0:row_value.find(in_row_value_delimeter)]))
                else:
                    work_list.append(row_value)
            result[row.split(in_row_delimeter)[0]] = work_list
        except:
            print('Исключение в данных!')
    return result


def make_sum(source_data: dict):
    result = {}
    for key, value in source_data.items():
        result[key] = sum(value)
    return result


def main():
    file_name = 'task_6.txt'

    print(parse(read_file(file_name)), ' - данные до суммирования')
    print(make_sum(parse(read_file(file_name))), ' - данные после суммирования')


if __name__ == '__main__':
    main()
