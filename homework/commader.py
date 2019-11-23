n = int(input())
d = {}
for i in range(n):
    x = int(input())
    temp = []
    for k, v in d.items():
        temp.append([k, v])
    for k, v in temp:
        if v < x:
            d.pop(k)
    d[i+1] = x

print(len(d))
for k in d.keys():
    print(k)
