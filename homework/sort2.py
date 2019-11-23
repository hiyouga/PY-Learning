n = int(input())
dic = {}

for i in range(n):
    name = input()
    tall = float(input())
    dic[name] = tall

lst = sorted(dic.items(), key = lambda x:x[1], reverse = True)

for n, t in lst:
    print("{}, {:.2f}".format(n, t))
