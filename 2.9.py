"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
max = 0
c = 0

while True:
    m = 0
    number = input("Введите натуральное число ")
    if number.isdigit():
        for i in number:
            m += int(i)
        if m > max:
            max = m
            c = int(number)

    else:
        break

print("Наибольшая сумма цифр ", max)
print("Число с наибольшой суммой цифр ", c)
