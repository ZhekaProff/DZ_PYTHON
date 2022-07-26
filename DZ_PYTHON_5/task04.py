
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    for char in data:
        # Если предыдущие и текущие символы
        # не совпадают...
        if char != prev_char:
            # ...затем добавьте количество и символ
            # к нашей кодировке
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Или увеличьте наш счетчик
            # если символы действительно совпадают
            count += 1
    else:
        # Завершите кодировку
        encoding += str(count) + prev_char
        return encoding
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # Если символ является числовым...
        if char.isdigit():
            # ...добавьте его к нашему счету
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # характер и необходимость расширить его для
            # расшифровка
            decode += char * int(count)
            count = ''
    return decode
# print(rle_decode('6a1f5s1r'))
path = r'data\task04.txt'
with open (path,'r') as text:
    in_text = str(text.readline())

path = r'data\task04_1.txt'
with open (path,'r+') as text2:
    text2.write(f"{rle_encode(in_text)}")
    in_text2 = str(text2.readline())
print(in_text2)
print(rle_decode(in_text2))

path = r'data\task04.txt'
with open (path,'a') as text:
    text.write(f"{rle_decode(in_text2)}")