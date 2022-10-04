s= input('Введите строку ')
import re
new_spisok = re.split(";|,| ", g)
m = 0
for i in new_spisok:
    if len(i) > m:
        m = len(i)
        o = i
        continue
print (o)