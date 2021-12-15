# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.




def read_file(file_name, encoding):
    with open(file_name, 'r', encoding=encoding) as o_file:
        data = o_file.read()
    return data


def main():
    file_name = 'task_2.txt'
    encoding = 'UTF-8'
    new_line_sym = "\n"

    file_data = read_file(file_name, encoding)

    print(f'Количество строк: {len(file_data.split(new_line_sym)) - 1}, количество слов: {len(file_data.replace(new_line_sym, " ").split(" ")) - 1}')


if __name__ == '__main__':
    main()
