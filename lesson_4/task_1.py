# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    total_work_hours = float(argv[1])
    salary_hour = float(argv[2])
    salary_bonus = float(argv[3])
except:
    print('Ошибка!\nСледует запускать скрипт из терминала.\nДоступно 3 параметра для ввода:\n  всего отработано часов\n  сумма зарплаты в час\n  сумма премии\nДанные вводятся в формате чисел: [0-9].[0-9]',
          '\nПример: python3 task_1.py 160 399.98 10000')

def annual_salary(total_work_hours: float, salary_hour: float, salary_bonus: float):
    return total_work_hours * salary_hour + salary_bonus

if __name__ == '__main__':
    print(annual_salary(total_work_hours, salary_hour, salary_bonus))
