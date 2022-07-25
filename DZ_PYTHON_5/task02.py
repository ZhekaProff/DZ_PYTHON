# 2 Создайте программу для игры с конфетами человек против человека.

from random import randint
import os
os.system('cls' if os.name == 'nt' else 'clear')


def proverka(n):
    while True:
        num = int(input("Игрок_1 введите число от 1 - 28: "))
        if 1 <= num <= 28:
            break
        else:
            print('Нужно ВВЕСТИ от 1 до 28')        
    return num
def proverka2(n):
    while True:
        num = int(input("Игрок_2 введите число от 1 - 28: "))
        if 1 <= num <= 28:
            break
        else:
            print('Нужно ВВЕСТИ от 1 до 28')        
    return num
def proverka3(n):
    num = randint(1,28)
    print(f'ИИ вводит {num}')
    return num
def proverka4(n, count):
    if count > 300:
            num = randint(1,28)
            print(f'ИИ вводит {num}')
            return num
    elif count > 29:
        count = count - 29
        num = count % 28
        if num == 0:
            num = 28
        print(f'ИИ вводит {num}')
        return num
    elif count == 29:
        num = 28
        print(f'ИИ вводит {num} и говорит: Что ты такое?')
        return num
    elif count < 29:
        count = count * 1
        num = count
        print(f'ИИ вводит {num}')
        return num
def game_start(check):
    if check == 0:
        print(f'Игру начинает ИГРОК_1. У нас {count} конфет')
    elif check == 1:
        print(f'Игру начинает ИГРОК_2. У нас {count} конфет') 
def game_start2(check):
    if check == 0:
        print(f'Игру начинает ИГРОК_1. У нас {count} конфет')
    elif check == 1:
        print(f'Игру начинает ИИ. У нас {count} конфет')
def game_over(check):
        if check == 0:
            print(f'GAME OVER\nWin ИГРОК_2')
        if check == 1:
            print(f'GAME OVER\nWin ИГРОК_1')
def game_over2(check):
        if check == 0:
            print(f'GAME OVER\nWin ИГРОК_2')
        if check == 1:
            print(f'GAME OVER\nWin ИИ')

count = 300
player_one = 0
player_two = 0

pp_ii = int(input('Выбирите против кого играть: \n- Игрок против игрока = 0:\n- Играть с ИИ = 1:\nВведите число: '))

#  =======================-Игрок против Игрока-===============================
if pp_ii == 0: 
    check = randint(0,1)
    game_start(check)
    while count >= 1:
        while check == 0: 
            player_one = int(proverka(player_one))
            count -= player_one
            check += 1
            print(f'У нас осталось {count} конфет')
            if count <= 0:
                break        
        else:
            check == 1
            player_two = int(proverka2(player_two))
            count -= player_two
            check -= 1
            print(f'У нас осталось {count} конфет')
    if count <=0:
        game_over(check)

elif pp_ii == 1: 
    dif = int(input('Выбирите уровень сложности:\n- тупая машина = 0\n- уровень бог = 1\nВведите число: '))

 #  =======================-Игрок против ИИ(тупого)-===============================

    if dif == 0:
        check = randint(0,1)
        game_start2(check)  
        while count >= 1:
            while check == 0: 
                player_one = int(proverka(player_one))
                count -= player_one
                check += 1
                print(f'У нас осталось {count} конфет')
                if count <= 0:
                    break
            else:
                check == 1
                player_two = int(proverka3(player_two))
                count -= player_two
                check -= 1
                print(f'У нас осталось {count} конфет')
        if count <=0:
            game_over2(check)

 #  =======================-Игрок против ИИ(тупого)-===============================

    if dif == 1:
        check = randint(0,1)
        game_start2(check)  
        while count >= 1:
            while check == 0: 
                player_one = int(proverka(player_one))
                count -= player_one
                check += 1
                print(f'У нас осталось {count} конфет')
                if count <= 0:
                    break
            else:
                check == 1
                player_two = int(proverka4(player_two, count))
                count -= player_two
                check -= 1
                print(f'У нас осталось {count} конфет')
        if count <=0:
            game_over2(check)