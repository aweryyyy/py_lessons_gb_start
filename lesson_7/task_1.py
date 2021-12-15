# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

from copy import deepcopy

class Matrix:
    def __init__(self, list_of_lists: list):
        self.matrix = list_of_lists

    def __str__(self):
        result = ''
        for row in self.matrix:
            for cell in row:
                result += f'{str(cell)} '
            result += '\n'
        return result

    def __add__(self, other: list):
        if len(other.matrix) == len(self.matrix) and len(other.matrix[0]) == len(self.matrix[0]):
            result = []
            for index_row, row in enumerate(self.matrix):
                result_column = []
                for index_cell, cell in enumerate(row):
                    result_column.append(int(other.matrix[index_row][index_cell]) + int(cell))
                result.append(result_column)
        else:
            max_row_cnt_over_matrix = len(self.matrix) if len(self.matrix) >= len(other.matrix) else len(other.matrix)
            max_col_cnt_over_matrix = len(self.matrix[0]) if len(self.matrix[0]) >= len(other.matrix[0]) else len(other.matrix[0])

            reduced_foreign_matrix = self.reduce(other.matrix, max_row_cnt_over_matrix, max_col_cnt_over_matrix)
            reduced_our_matrix = self.reduce(self.matrix, max_row_cnt_over_matrix, max_col_cnt_over_matrix)

            result = []
            for index_row, row in enumerate(reduced_our_matrix):
                result_column = []
                for index_cell, cell in enumerate(row):
                    result_column.append(int(reduced_foreign_matrix[index_row][index_cell]) + int(cell))
                result.append(result_column)

        return result

    def reduce(self, in_matrix: list, max_rows: int, max_cols: int) -> list:
        reduced_matrix = deepcopy(in_matrix)

        if max_rows > len(reduced_matrix):
            row_add = []
            for row in range(max_rows):
                row_add.append(0)
            reduced_matrix.append(row_add)

        for row_ind, row in enumerate(reduced_matrix):
            if max_cols > len(row):
                reduced_matrix[row_ind].append(0)

        return reduced_matrix



# проверка матриц разной размерности:
old_matrix = Matrix(
    [
        [1, 2, 3, 1],
        [4, 5, 6, 1],
        [7, 8, 9, 1]
    ]
)
new_matrix = Matrix(
    [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [7, 8, 9]
     ]
)


# проверка матриц одной размерности:
# old_matrix = Matrix(
#     [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#     ]
# )
#
# new_matrix = Matrix(
#     [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#     ]
# )

sum_matrix = Matrix(new_matrix + old_matrix)
print('первая матрица\n', new_matrix, sep='')
print('вторая матрица\n', old_matrix, sep='')
print('результат сложения матриц\n', sum_matrix, sep='')

