# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


n = 45

# Решение рекурсией
def decimalToBinary(n):
 
    if(n > 1):
        decimalToBinary(n//2)
    print(n%2, end='')

decimalToBinary(n)
print()

# Обычное решение через цикл
b = ''
while n > 0:
    b += str(n % 2)
    n = n // 2
print(b)

# встроенная функция bin
print(bin(45))

