# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции вводит пользователь через пробел. 

from array import array

def get_numbers(n):                 # Заполняем список целыми числами от -n до n
    array = list(range(-n , n + 1))
    return array

def enter_coords():
    while True:
        try:
            coord = input("Введите позиции через пробел: ")
            coords = coord.split(" ")
            break
        except ValueError:
            print("Введите целые числа через пробел")
    return coords
    
def multiply_elements(list: list, coords: list):
    multiply = 1
    for element in coords:
        multiply *= list[int(element)]
    return multiply
# ===========================================================+

n = int(input('Введите числа: ') )

numbers = get_numbers(n)
coords = enter_coords()
print(numbers)
print(multiply_elements(numbers, coords))

