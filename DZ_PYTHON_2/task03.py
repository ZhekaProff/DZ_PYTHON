# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

def metod_formula(n):
    summa = 0
    for i in range(n):
        summa += (1 + 1/n)**n
        print(round(summa), end=(" "))

n = int(input('Введите число: '))
metod_formula(n)