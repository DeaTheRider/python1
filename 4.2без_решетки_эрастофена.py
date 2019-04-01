"""
Написать два алгоритма нахождения i-го по счёту простого числа.

Без использования «Решета Эратосфена»;
"""
import timeit
import cProfile


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return n == d


def main():
    n = 70  # до какого числа нужно найти
    a = [0] * n  # создание массива с n колличсеством элемантов
    for i in range(n):
        a[i] = i
    a[1] = 0
    for i in a:
        if IsPrime(i) != True:
            a[i] = 0
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a


# print(timeit.timeit("main()", setup="from __main__ import main", number=1000000))
# Время 50.576026234, Сложность O(n) – линейная сложность

# cProfile.run('main()')
"""
93 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       70    0.000    0.000    0.000    0.000 4.2без_решетки_эрастофена.py:10(IsPrime)
        1    0.000    0.000    0.000    0.000 4.2без_решетки_эрастофена.py:17(main)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       19    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

if __name__ == "__main__":
    main()
