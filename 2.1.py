"""Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя."""
s = 0
while True:
    operand = input("Введите операнд или введите 0 если хотите выйти ")
    if operand == "0":
        break
    elif operand == '-' or operand == '+' or operand == '/' or operand == '*':
        num1 = int(input("Введите первое число "))
        num2 = int(input("Введите второе число "))
        if operand == "+":
            s = num1 + num2
            print(s)
        elif operand == "-":
            s = num1 - num2
            print(s)
        elif operand == "*":
            s = num1 * num2
            print(s)

        elif operand == "/":
            if num2 == 0:
                print("На ноль делить нельзя")
            else:
                s = num1 / num2
                print(s)

    else:
        print("Ошибка")
        continue







