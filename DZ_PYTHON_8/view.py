# тут функции для работы с файлом csv
import csv


path = r'data\phone book.csv'
def show():
    with open(path, mode="r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        res = ["Фамилия Имя | Телефон\n"]
        for row in reader:
            res.append(f"\n{row['Surname']} {row['Name']} | {row['Telephone']}")
        return res
        

def add_contact(line: list):    
    with open(path, mode="a", encoding='utf-8') as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ";", lineterminator="\n")
        file_writer.writerow(line)
    

print(show())