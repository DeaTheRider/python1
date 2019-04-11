"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random
import timeit
import cProfile


def buble_sort(array):
    a = array
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] < a[j + 1]:
                f = a[j]
                a[j] = a[j + 1]
                a[j + 1] = f
    return a


def create_list(x):
    array = []
    for i in range(x):
        number = random.randint(-100, 100)
        array.append(number)
    return array

#@profile
def main():
    b = create_list(15)
    print(b)
    print()
    b = buble_sort(b)
    print(b)


if __name__ == "__main__":
    main()

"""
Line #    Mem usage    Increment   Line Contents
================================================
    30   36.523 MiB   36.523 MiB   @profile
    31                             def main():
    32   36.523 MiB    0.000 MiB       b = create_list(15)
    33                                 #print(b)
    34                                 #print()
    35   36.523 MiB    0.000 MiB       b = buble_sort(b)

"""
#cProfile.run('main()')
"""
105 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 7.1.py:13(buble_sort)
        1    0.000    0.000    0.000    0.000 7.1.py:24(create_list)
        1    0.000    0.000    0.000    0.000 7.1.py:32(main)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       15    0.000    0.000    0.000    0.000 random.py:174(randrange)
       15    0.000    0.000    0.000    0.000 random.py:218(randint)
       15    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       15    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       15    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       20    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
#print(timeit.timeit("main()", setup="from __main__ import main", number=1000000))
#38.234186851
