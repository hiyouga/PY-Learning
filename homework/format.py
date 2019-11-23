s = input()
ns = []
ups = True
for i in range(len(s)):
    if ups == True or (s[i].lower() == 'i' and (i == 0 or s[i-1].isalpha() == False) and (i == len(s)-1 or s[i+1].isalpha() == False)):
        ns.append(s[i].upper())
    elif s[i].isalpha():
        ns.append(s[i].lower())
    else:
        ns.append(s[i])
    if s[i] == '.':
        ups = True
    elif s[i].isalpha():
        ups = False
    
print(''.join(ns))
