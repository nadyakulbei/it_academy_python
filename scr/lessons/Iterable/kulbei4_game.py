#n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16
#4:2 1:2 3:2 0:2 3:2 4:2 1:2 4:2 3:2 1:2 1:2 3:2 3:2 1:2 1:2 3:2 3:2 1:2 1:2 3:2 3:2 5:2 1:2 3:2 3:2 3:2 1:2 3:2 0:2 7:9
name = input('Введите название команд: ').split(' ', 16)
resultat= (input('Введите результаты: ').split(' ',29))
r = []
for i in resultat:
    f=i.split(':')
    r.append(int(f[0]))
    r.append(int(f[1]))
x=name[:8]
y = name[len(name):7:-1]
sp1 = []
sp2 = []
sp3 = []
for c, i in zip(x,y):
    if (r[0]+ r[2])>(r[1]+ r[3]):
        sp1.append(c)
    elif (r[0]+ r[2])<(r[1]+ r[3]):
        sp1.append(i)
    del r[0:4]
    r=r
    if len(sp1)==8:
        break
x1=sp1[:4]
y1 = sp1[len(sp1):1:-1]
for c, i in zip(x1,y1):
    if (r[0]+ r[2])>(r[1]+ r[3]):
        sp1.append(c)
    elif (r[0]+ r[2])<(r[1]+ r[3]):
        sp2.append(i)
    del r[0:4]
    r=r
    if len(sp2)==4:
        break
x2=sp2[:2]
y2 = sp2[len(sp2):1:-1]
for c, i in zip(x1,y1):
    if (r[0]+ r[2])>(r[1]+ r[3]):
        sp3.append(c)
    elif (r[0]+ r[2])<(r[1]+ r[3]):
        sp3.append(i)
    del r[0:4]
    r=r
    if len(sp3)==2:
        break
if r[0]>r[1]:
    print(sp3[0])
else:
    print(sp3[1])