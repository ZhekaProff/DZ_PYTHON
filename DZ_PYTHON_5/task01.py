# 1 Напишите программу, удаляющую из текста все слова, содержащие "абв".

def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

path = r'data\task01.txt'
with open (path,'r+', encoding='utf-8') as text:
    in_text = str(text.readline())
    text.write(f"\n{del_some_words(in_text)}")



