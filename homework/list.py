lst = []
n = 1
x = input()
while x:
    lst.append(int(x))
    n += 1
    x = input()
print(max(lst))
print(min(lst))
print(lst[n//2-1])
strlst = sorted(lst, reverse = True)
strlst = list(map(str, strlst))
print(' '.join(strlst))
