s1, s2 = (input('Введите автора или название, время выхода книги: ').split(' ',1))
sp = []
import csv
with open('library.csv') as file:
    csvfile = csv.DictReader(file,  delimiter=' ', quotechar='|', fieldnames=['names', 'books', 'years', 'theme'])
    for row in csvfile:
        if s1 in row['names'] and s2 == row['years']:
            print(row['names'], row['books'], row['years'], row['theme'])
        elif s1 in row['names'] and s2 == row['books']:
            print(row['names'], row['books'], row['years'], row['theme'])
        elif s1 in row['names'] and s2 =='First' or s2 == 'Last':
            sp.append(row)
    if s2=='First':
        m = min(sp, key=lambda row: row['years'])
        print(m['years'], m['books'])
    elif s2=='Last':
        m = max(sp, key=lambda row: row['years'])
        print(m['years'], m['books'])
    elif s1 not in row['names']:
        print('Проверь корректность введенных данных')

    # row[0] - строка вида "Фамилия, Имя" или "Имя"
    # row[1] - строка вида "Название произведения"
    # row[2] - строка вида "1850" или "-50"
    # row[3] - строка вида "Тема,Тема,Тема"
    # Andersen Andersen's Fairy Tales
    # Falkner First
    # Falkner Last