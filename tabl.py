a=int(input('Введите число a, от 1 до 10: '))
b=int(input('Введите число b, от 1 до 10: '))
c=int(input('Введите число c, от 1 до 10: '))
d=int(input('Введите число d, от 1 до 10: '))
if ((a and b<=10) and (c and d<=10)) and ((a<=b) and (c<=d)):
    for i in range(c, d+1):
        print('\t',i, end='')
    print()
    for j in range(a, b+1):
        print(j,end='')
        for t in range(c, d+1):
            print('\t',j*t,end='')
        print()
else:
    print('Программа не может считать умножение больше 10')