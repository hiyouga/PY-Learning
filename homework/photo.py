n = int(input())
m = int(input())
cnt = {}
ans = []

for i in range(n):
    k = input()
    if k in cnt.keys():
        cnt[k] += 1
    else:
        cnt[k] = 1
    if cnt[k] <= m:
        ans.append(k)

for i in ans:
    print(i)
    
