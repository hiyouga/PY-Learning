n = int(input())
dic = {}

for i in range(n):
    c = input()
    if c == "Q":
        n = input()
        if n in dic.keys():
            print(dic[n])
        else:
            print("NONE")
    elif c == "A":
        n, p = input().split(" ")
        dic[n] = p
