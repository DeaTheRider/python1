"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random
import timeit
import cProfile


def create_list(x):
    array = []
    for i in range(x):
        number = random.uniform(0, 50)
        number = round(number, 3)
        array.append(number)
    return array


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)

    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)
#@profile
def main():
    a = create_list(10)
    print(a)
    b = mergesort(a)
    print(b)

if __name__ == "__main__":
    main()
"""
Line #    Mem usage    Increment   Line Contents
================================================
    41   36.609 MiB   36.609 MiB   @profile
    42                             def main():
    43   36.617 MiB    0.008 MiB       a = create_list(10)
    44                                 #print(a)
    45   36.617 MiB    0.000 MiB       b = mergesort(a)

"""
#cProfile.run('main()')
"""
186 function calls (168 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 7.2.py:10(create_list)
        9    0.000    0.000    0.000    0.000 7.2.py:19(merge)
     19/1    0.000    0.000    0.000    0.000 7.2.py:34(mergesort)
        1    0.000    0.000    0.000    0.000 7.2.py:43(main)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       10    0.000    0.000    0.000    0.000 random.py:372(uniform)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       88    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.round}
       33    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
"""
#print(timeit.timeit("main()", setup="from __main__ import main", number=1000000))
#27.321382374000002