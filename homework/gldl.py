def max_pre(a, b):
    i = 0
    res = ''
    while i < len(a) and i < len(b):
        if a[i] == b[i]:
            res += a[i]
        else:
            return res
        i += 1
    return res

n = int(input())

out = input()

for i in range(n-1):
    s = input()
    out = max_pre(s, out)

if out == '':
    print('No')
else:
    print(out)
