t = 0
f = 0
n = int(input())
while n != -1:
    if n == 1:
        t += 1
    else:
        f += 1
    n = int(input())

if t >= f:
    print('Yes')
else:
    print('No')
