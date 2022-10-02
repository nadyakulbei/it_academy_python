s = input("Введите строку, а я выведу нужное ")
i = ""
for c in s:
    if c in i or c == ' ':
        continue
    i = i + c
print(i)