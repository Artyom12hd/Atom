a=int(input('Введите число a: '))
b=int(input('Введите число b: '))
c=int(input('Введите число c: '))
d=int(input('Введите число d: '))
for i in range(c, d+1):
	print('\t',i, end='')
print()
for j in range(a, b+1):
    print(j,end='')
    for t in range(c, d+1):
        print('\t',j*t,end='')
    print()
