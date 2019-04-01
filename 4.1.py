"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных
в рамках домашнего задания первых трех уроков.
"""
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string
import timeit
import cProfile


# Алгоритм №1
def binary_search(list, item):
    min = 0
    max = len(list) - 1
    while min <= max:
        mid = (min + max)
        guess = list[mid]
        if mid == item:
            return guess
        elif mid > item:
            max = mid - 1
        else:
            min = mid + 1
    return None


# Алгоритм №2
def search(list, item):
    for i, j in enumerate(list):
        if i == item:
            return j
        else:
            continue
    return None


a = string.ascii_uppercase
my_list = list(a)
b = 24
"""print(binary_search(my_list, b))
print(search(my_list, b))"""

print(timeit.timeit("binary_search(my_list, b)", setup="from __main__ import binary_search,my_list,b", number=10000000))
# Время 3.6585515689999997, O(log n) – логарифмическая сложность

print(timeit.timeit("search(my_list, b)", setup="from __main__ import search,my_list,b", number=10000000))
# Время 12.559837981000001, O(n) – линейная сложность
# cProfile.run('search(my_list,b)')
"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 4.1.py:28(search)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('binary_search(my_list,b)')

"""
5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 4.1.py:12(binary_search)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
