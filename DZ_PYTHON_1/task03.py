# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

from random import randint # погуглил как вводить случайные числа =) 

x = randint(-10, 10)
y = randint(-10, 10)

# x = 0 # проверка else
# y = 0

print(x,y)

if ( x > 0 and y > 0):
    print('точка находится в 1 четверти координат')
elif (x > 0 and y < 0):
    print('точка находится во 2 четверти координат')
elif (x < 0 and y < 0):
    print('точка находится в 3 четверти координат')
elif (x < 0 and y > 0):
    print('точка находится во 4 четверти координат')
elif (x == 0 and y > 0):
    print('точка находится на оси y')
elif (x < 0 and y == 0):
    print('точка находится на оси x')
else:
    print('точка в центре')