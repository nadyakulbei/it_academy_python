s = input("Введите строку, а я выведу количество ")
i = 0
little_i = 0
import string
#string.ascii_uppercase
#string.asccii_lowcase
for c in s:
    if c in string.ascii_uppercase:
        i = i+1
    if c in string.ascii_lowercase:
        little_i  = little_i +1
print("количество маленьких букв ", little_i)
print("количество больших букв ", i)
print('jj')

s = input()
ol = s.split(' ')
unique = []
dupl = []
for i in ol:
    if i not in unique and i not in dupl :
        unique.append(i)
    elif i in unique :
        unique.remove(i)
        dupl.append(i)
print(dupl)