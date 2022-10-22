#Adventure stories,British,Impostors and imposture, Meditations,Life
s1 = input('Введите темы книг: ').split(',')
s2 =input('Введите количество книг: ')
subj = set(s1)
sp = []
dd=[]
import csv
with open('library.csv') as file:
    csvfile = csv.DictReader(file,  delimiter=' ', quotechar='|', fieldnames=['names', 'books', 'years', 'theme'])
    for row in csvfile:
        svp = len(set(row['theme'].split(',')) & subj)
        if svp>=1:
            row['svp'] = svp
            sp.append(row)
v=sorted(sp, key=lambda row: row['svp'], reverse=True)
for i in range(int(s2)):
    print(v[i])