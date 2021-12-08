# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

from json import dump


def read_file(source_file_name: str, encoding='UTF-8') -> list:
    with open(source_file_name, 'r', encoding=encoding) as fr:
        result = fr.readlines()
    return result


def write_json(list_to_write: list, file_name: str, encoding='UTF-8'):
    with open(file_name, 'w', encoding=encoding) as fw:
        dump(list_to_write, fw)


def calc_data(input_data: str) -> tuple:
    revenue, costs, counter, firm = 0, 0, 0, ''
    for element in input_data.split(' '):
        if counter == 0:
            firm = element
        elif counter == 2:
            revenue = int(element)
        elif counter == 3:
            costs = int(element)
        counter += 1

    return revenue, costs, counter, firm


def parse(source_data: list) -> list:
    profit_dict = {}
    loss_dict = {}
    avg_profit = {}

    for firm in source_data:
        work_firm_row = firm.replace('\n', '')
        revenue, costs, counter, firm = calc_data(work_firm_row)

        if revenue - costs > 0:
            profit_dict[firm] = revenue - costs
        else:
            loss_dict[firm] = revenue - costs

    avg_profit['average_profit'] = round(sum(profit_dict.values()) / len(profit_dict), 2)

    profit_dict.update(loss_dict)

    return [profit_dict, avg_profit]


def main():
    file_name_read = 'task_7.txt'
    json_result = 'task_7.json'

    write_json(parse(read_file(file_name_read)), json_result)


if __name__ == '__main__':
    main()
