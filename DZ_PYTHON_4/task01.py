# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$

import math

def get_count(number: float): # считает сколько цифр после "." формата 0.001
    count = 0
    while number != 1:
        number *= 10
        count += 1
    return count

d = float(input('Введите точность математически: '))
c = get_count(d) 
pi_str = str(math.pi)
e = 2 + c
print(f'- при d = {d}, π = ', pi_str[0:e])
