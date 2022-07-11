# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sum_of_digits(a):
    result = 0
    while a > 0:
        result += a % 10
        a //= 10
    return result
 
print(sum_of_digits(123))