lst = input().split()
h = list(map(int, lst))
v = 0
for i in range(len(h)):
    for j in range(i+1, len(h)):
        v = max(v, min(h[i], h[j]) * (j - i))

print(v)
