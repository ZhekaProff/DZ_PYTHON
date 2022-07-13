# Реализуйте алгоритм перемешивания списка. 

import random

lst = [1, 2, 3, 4, 5]
print(lst, ' - Исходный')
random.shuffle(lst) 
print(lst, ' - Перемешанный')

res = random.sample(lst, len(lst))
print(res, ' - Перемешанный, но сохранен изначальный')