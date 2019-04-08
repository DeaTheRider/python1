"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
# Python 3.7.2  x64
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string
import sys
from pympler import asizeof


# Алгоритм №1
# @profile
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
#@profile
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
"""if __name__ == "__main__":
    binary_search(my_list,b)
    
    Line #    Mem usage    Increment   Line Contents
================================================
    14   51.344 MiB   51.344 MiB   @profile
    15                             def binary_search(list, item):
    16   51.344 MiB    0.000 MiB       min = 0
    17   51.344 MiB    0.000 MiB       max = len(list) - 1
    18   51.344 MiB    0.000 MiB       while min <= max:
    19   51.344 MiB    0.000 MiB           mid = (min + max)
    20   51.344 MiB    0.000 MiB           guess = list[mid]
    21   51.344 MiB    0.000 MiB           if mid == item:
    22   51.344 MiB    0.000 MiB               return guess
    23   51.344 MiB    0.000 MiB           elif mid > item:
    24   51.344 MiB    0.000 MiB               max = mid - 1
    25                                     else:
    26                                         min = mid + 1
    27                                 return None
"""
"""if __name__ == "__main__":
    search(my_list,b)
    
Line #    Mem usage    Increment   Line Contents
================================================
    31   51.531 MiB   51.531 MiB   @profile
    32                             def search(list, item):
    33   51.531 MiB    0.000 MiB       for i, j in enumerate(list):
    34   51.531 MiB    0.000 MiB           if i == item:
    35   51.531 MiB    0.000 MiB               return j
    36                                     else:
    37                                         continue
    38                                 return None """

# print(sys.getrefcount(a))
# 3
# print(asizeof.asizeof(a))
# 80
# print(id(a))
# 4538378880

# print(sys.getrefcount(my_list))
# 2
# print(asizeof.asizeof(my_list))
# 1800
# print(id(my_list))
# 4502936392


# print(sys.getrefcount(b))
# 39
# print(asizeof.asizeof(b))
# 32
# print(id(b))
# 4502936392


