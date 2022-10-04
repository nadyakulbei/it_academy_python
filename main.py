s = input()
ol = s.split (' ')
unique = []
dupl = []
for i in ol:
    if i not in unique and i not in dupl :
        unique.append(i)
    elif i in unique :
        unique.remove(i)
        dupl.append(i)
print(dupl)