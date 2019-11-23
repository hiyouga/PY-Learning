n = int(input())
d = {}
for i in range(n):
    name, cnt = input().split()
    cnt = int(cnt)
    d[name] = cnt

m = int(input())
for i in range(m):
    name, cnt = input().split()
    cnt = int(cnt)
    if name in d.keys():
        d[name] += cnt
    else:
        d[name] = cnt

query = input()
print(d[query])
