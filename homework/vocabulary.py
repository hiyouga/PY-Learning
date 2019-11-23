n = int(input())
dic = {}

for i in range(n):
    words = input().lower().split()
    for w in words:
        if w in dic.keys():
            dic[w] += 1
        else:
            dic[w] = 1

m = max(dic.values())
print(m)
for w, k in dic.items():
    if k == m:
        print(w)
