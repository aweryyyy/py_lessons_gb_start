# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def write_file(file_name: str, file_data: list, encoding='UTF-8'):
    with open(file_name, 'w', encoding=encoding) as fw:
        for element in file_data:
            fw.write(f'{element} ')


def read_file(file_name: str, encoding='UTF-8') -> str:
    with open(file_name, 'r', encoding=encoding) as fw:
        data = fw.read()
    return data


def calc_sum(source_data: str) -> float:
    work_data = source_data.split(' ')
    result = 0
    for element in work_data:
        try:
            float(element)
        except:
            print(f'В файле обнаружены нечисловые данные: {element}')
        else:
            result += float(element)
    return result


def main():

    example_list = ['0', '12', '-3', '-500', '100']

    file_name = 'task_5.txt'
    encoding = 'UTF-8'

    write_file(file_name, example_list, encoding=encoding)
    print(calc_sum(read_file(file_name, encoding=encoding)))


if __name__ == '__main__':
    main()
