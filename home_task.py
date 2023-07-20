# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения

import random


class Matrix:

    def __init__(self, rows, columns):
        self.matrix = []
        self.rows = rows
        self.columns = columns
        for _ in range(self.rows * self.columns):
            self.matrix.append(random.randint(1, 9))

    def print_matrix(self):
        for i in range(0, self.columns * self.rows):
            print(self.matrix[i], end=" ")
            if (i + 1) % self.columns == 0:
                print()

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            return self.matrix + other.matrix
        else:
            print("Невозможно сложить матрицы.")

    def __eq__(self, other):
        if self.rows == other.rows and self.columns == other.columns and self.matrix == other.matrix:
            return True
        else:
            return False


m_1 = Matrix(3, 4)
m_2 = Matrix(4, 3)
m_1.print_matrix()
print()
m_2.print_matrix()
print()
m_3 = m_1 + m_2
print()
print(m_1 == m_2)
