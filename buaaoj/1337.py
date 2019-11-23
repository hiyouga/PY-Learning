def check(i, j, k):
    for p in range(k):
        for q in range(p+1):
            if mat[i-p][j-q] != '-':
                return False
    return True

n = int(input())
s = 0
mat = []

mat.append('*' * (n+2))

for i in range(1, n+1):
    mat.append('*' + input() + '*')

mat.append('*' * (n+2))

for i in range(n, 0, -1):
    for j in range(n, i-1, -1):
        for k in range(1, i+1):
            if check(i, j, k):
                s = max(s, k)

print(s)
