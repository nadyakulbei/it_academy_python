k = input("Введите ваш текст: ")
sk = [i for i in k if i == "(" or i == ")" or i == '[' or i == ']' or i == '{' or i == "}"]
sp = []
rgt = {'()', '[]', '{}'}
for i in range(len(sk)):
    if sk[i] == '(' or sk[i] == '[' or sk[i] == '{':
         sp.append(sk[i])
         continue
    if sk[i] == ')'or  sk[i] == ']' or sk[i] == '}':
         if len(sp) >= 1 and sp[-1] + sk[i] in rgt :
             sp.pop()
         else:
             sp.append(sk[i])
             break
if sp == []:
    print('Все ок, бро')
else:
    print('Со скобками проблема')