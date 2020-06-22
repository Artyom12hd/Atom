a, b, d=1, 0, 0
while 1:
    a = int(input())
    d += (a ** 2)
    b += a
    if b==0:
        break
print(d)

