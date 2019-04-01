"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Используя алгоритм «Решето Эратосфена»
"""
import timeit
import cProfile


def main():
    n = 70
    a = [0] * n  # создание массива с n колличсеством элемантов
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a


# print(timeit.timeit("main()", setup="from __main__ import main", number=1000000))

# Время 19.184488545,O(n) – линейная сложность, (но я не уверен)

# cProfile.run('main()')
"""
 23 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       19    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 эрастофен.py:7(main)
"""
if __name__ == "__main__":
    main()
