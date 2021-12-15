# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
#     сложение (__add__()),
#     вычитание (__sub__()),
#     умножение (__mul__()),
#     деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
#     Сложение.
#         Объединение двух клеток.
#         При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#     Вычитание.
#         Участвуют две клетки.
#         Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
#             иначе выводить соответствующее сообщение.
#     Умножение.
#         Создается общая клетка из двух.
#         Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#     Деление.
#         Создается общая клетка из двух.
#         Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
#   Данный метод позволяет организовать ячейки по рядам.
#   Метод должен возвращать строку вида *****\n*****\n*****...,
#       где количество ячеек между \n равно переданному аргументу.
#   Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#   Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
#   Тогда метод make_order() вернет строку: *****\n*****\n**.
#   Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
#   Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    elements = 0

    def __init__(self, element_count: int):
        self.elements = element_count

    def __add__(self, other):
        return Cell(self.elements + other.elements)

    def __sub__(self, other):
        if self.elements - other.elements > 0:
            result = self.elements - other.elements
        else:
            raise Exception('Элементов в изначальной клетке недостаточно для вычитания!')
        return Cell(result)

    def __mul__(self, other):
        return Cell(self.elements * other.elements)

    def __truediv__(self, other):
        try:
            result = self.elements // other.elements
        except ZeroDivisionError:
            print('Деление на 0!')
            result = 0
        else:
            result = self.elements // other.elements
        return Cell(result)

    def make_order(self, el_count_in_row: int) -> str:
        result = ''.join(['*' if i % el_count_in_row != 0 or i == 0 else '\n*' for i in range(self.elements)])
        return result


init_cells = [
    Cell(12),
    Cell(5)

]

operation_with_cells = []

operation_with_cells.append([init_cells[0] + init_cells[1], '+'])

operation_with_cells.append([init_cells[0] - init_cells[1], '-'])

# operation_with_cells.append([init_cells[1] - init_cells[0], '- (error)'])

operation_with_cells.append([init_cells[0] * init_cells[1], '*'])

operation_with_cells.append([init_cells[0] / init_cells[1], '/'])

for cell in operation_with_cells:
    print(f'Клетка {init_cells[0].elements} {cell[1]} клетка {init_cells[1].elements} = {cell[0].elements}\n{cell[0].make_order(4)}')
    print('\n')
