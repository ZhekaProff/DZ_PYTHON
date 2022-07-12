# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sum_of_digits(a):
    result = 0
    while a > 0:
        result += a % 10
        a //= 10
    return result
''' Функция по работе с int

'''

# разделим введённое (тип данных строка) на две части
def float_namber(num: any):
    x = num.split(".") 
    a = int(x[0]) # целая часть
    b = int(x[1]) # дробная часть
    mult = 0
    while (a > 0): # перемножаем числа целой части
        mult = mult + (a % 10)
        a = a // 10
    while (b > 0): 
        mult = mult + (b % 10)
        b = b // 10
    return mult
''' Функция по работе с float

'''
# Я хотел сделать две функции для int и float, и потом определять число и направлять в нужную функцию, но реализовать не смог. Возмодно ли это? 

# Решеие задачи через строку

def sum_of_namber(number: any):
    summa = 0
    num = str(number).replace(".", "")
    for index in num:
        summa += int(index)
    return summa

number = input("Enter your number? ")
print(f'{number} ->', sum_of_namber(number))

