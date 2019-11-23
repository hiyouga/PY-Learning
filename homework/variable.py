vn = input()
out = []
i = True
for c in vn:
    if i == True:
        out.append(c.lower())
        i = False
    else:
        if c.isupper():
            out.append('_' + c.lower())
        else:
            out.append(c)
print(''.join(out))
