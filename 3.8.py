"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных
 элементов каждой строки и записывать ее в последнюю ячейку строки.
 В конце следует вывести полученную матрицу.
"""
import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

for line in matrix:
    print(line)

for j, line in enumerate(matrix):
    sum_element = 0
    for i, item in enumerate(line):
        if i != 4:
            a = int(input("Введите элемент строки"))
            matrix[j][i] = a
            sum_element += a
        else:
            matrix[j][i] = sum_element

for line in matrix:
    print(line)
