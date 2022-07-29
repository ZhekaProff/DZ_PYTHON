# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции вводит пользователь через пробел. 

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

n = int(input('Введите числа: ') )

# numbers = get_numbers(n)
f = lambda numbers: list(range(-n , n + 1)) # заменил этой строкой функцию создания списка от -n до n
coords = enter_coords()
print(f(n))
print(multiply_elements(f(n), coords))


#=================================================================================+
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# ================================= РЕШЕНИЕ ======================================+

list = [2, 3, 5, 9, 3]
# list2 = []
# for i in range(1, len(list), 2):
#     list2.append(list[i])
list2 = [ list[i] for i in range(1, len(list), 2)] # стало 
print(f'- {list} -> на нечетных позициях элементы {list2}, сумма =', sum(list2))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6, 6]
# list2 = []
# for i in range((len(list)+1)//2):
#     list2.append(list[i]*list[len(list)-1-i])
list2 = [list[i]*list[-i-1] for i in range((len(list)+1)//2)]
print(list2)
