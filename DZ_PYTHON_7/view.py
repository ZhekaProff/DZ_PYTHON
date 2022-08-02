# тут функции для работы с файлом csv
import csv

path = r'data\phone book.csv'
def show():
    with open(path, mode="r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        print("\nФамилия Имя | Телефон")
        for row in reader:
            print(row['Surname'], row['Name'],'|', row['Telephone'])
        

def add_contact():
    line = []
    surname = input('Фамилия: ')
    line.append(surname)
    name = input('Имя: ')
    line.append(name)
    telephone = input('Телефон: ')
    line.append(telephone)
    with open(path, mode="a", encoding='utf-8') as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ";", lineterminator="\r")
        file_writer.writerow(line)
    

