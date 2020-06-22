a = [int(i) for i in input().split()]
n = len(a)
if n > 1:
    for i in range(n):
        print(a[i-1]+a[i+1-n], end=' ')
else:
    print(a[i+1])
