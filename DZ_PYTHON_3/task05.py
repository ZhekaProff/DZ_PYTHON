# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))

def get_fibonacci(n): # метод заполнения списка числами фибоначи
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    return fibo_nums
    
fibo = get_fibonacci(k)
fibo2 = list(reversed(fibo)) # создаем список с в обратном порядке от fibo
for i in range(len(fibo2)):  # перемножаем с первого числа если k четное, если нет то со второго
    if k % 2 ==0:
        if i % 2 == 0: 
            fibo2[i] *= -1
    else:
        if i % 2 != 0: 
            fibo2[i] *= -1
fibo2.append(0)              # добавляем 0 в центр
print(f'для k = {k} список будет выглядеть так:', fibo2 + fibo)


