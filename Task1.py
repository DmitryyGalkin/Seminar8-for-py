"""Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()),который должен принимать данные (список списков) для
формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, *args):
        self.new_list = list(args)

    def __str__(self):
        result = '\n'.join(map(str, self.new_list))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range(len(self.new_list)):
            for y in range(len(self.new_list[x])):
                line_sum.append(self.new_list[x][y] + other.new_list[x][y])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))


matrix1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix1)
matrix2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix2)

print(f'Сумма матриц : \n {matrix1 + matrix2}')
