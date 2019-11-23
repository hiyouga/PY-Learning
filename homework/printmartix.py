n = int(input())

for i in range(n):
    row = ['0'] * n
    row[i] = '1'
    print(' '.join(row))
