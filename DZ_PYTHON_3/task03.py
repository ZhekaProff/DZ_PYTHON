# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5., 10.01] => 0.19

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in(mynums)]
    # print(nums) округленный сисок до 0 до ,
    nums = [x for x in nums if type(x) == float]
    # print(nums) список без элемента int
    return max(nums) - min(nums)


list = [1.1, 1.2, 3.1, 5, 10.01]
print(list, '= >', find_diff(list))

