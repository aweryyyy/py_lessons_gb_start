# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


# write data to file:
def init_file(file_name):
    with open(file_name, 'w') as fw:

        employee_salary = {
            "Hardy": 20000,
            "Tompson": 150000,
            "Garett": 12500,
            "Lisben": 13340,
            "Li": 100000,
            "Einhart": 68000
        }

        for key, value in employee_salary.items():
            fw.write(f'{key} - {str(value)}\n')


def read_file(file_name, encoding):
    with open(file_name, 'r', encoding=encoding) as fr:
        data = fr.read()
    return data


def parse(user_data):
    work_dict = {}
    for row in user_data.split('\n'):
        try:
            work_dict[row.split(' - ')[0]] = float(row.split(' - ')[1])
        except:
            pass
    return work_dict


def analyze(data_dict):
    shape = 20000.0
    salary_less_20k = []
    avg_salary = sum(data_dict.values()) / len(data_dict)

    for key, value in data_dict.items():
        try:
            if float(value) < shape:
                salary_less_20k.append(key)
        except:
            print('В файле обнаружены нечисловые значения в области зарплаты!')

    return f'Сотрудники, с зп менее {shape}: {salary_less_20k}, среднее значение зп: {avg_salary})'


if __name__ == '__main__':
    file_name = 'task_3.txt'
    encoding = 'UTF-8'

    # если лень создавать файлик
    init_file(file_name)

    print(analyze(parse(read_file(file_name, encoding))))
