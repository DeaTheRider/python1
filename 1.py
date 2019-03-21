# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = input("Введите трехзначное число:")

first_number = int(number[0])
second_number = int(number[1])
thirt_number = int(number[2])

sum = first_number + second_number + thirt_number
com = first_number * second_number * thirt_number

print("Сумма цифр трехзначного числа = ", sum)
print("Произведение цифр трехзначного числа", com)