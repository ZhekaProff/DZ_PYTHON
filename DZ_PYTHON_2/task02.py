# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
        print(fact, end=" ")
n = int(input('Введите целое число: '))
factorial(n)
