rom = input()
dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
res = 0
tmp = pre = dic[rom[0]]
for cur in rom[1:]:
    if dic[cur] == pre:
        tmp += dic[cur]
    elif dic[cur] > pre:
        tmp = dic[cur] - tmp
    elif dic[cur] < pre:
        res += tmp
        tmp = dic[cur]
    pre = dic[cur]
res += tmp
print(res)
