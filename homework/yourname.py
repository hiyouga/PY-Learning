name = input()
tname = []
words = name.split(' ')
tname.append(words[0].capitalize())
if len(words) > 2:
    for w in words[1:-1]:
        tname.append(w[0].upper() + '.')
if len(words) >= 2:
    tname.append(words[-1].capitalize())
print(' '.join(tname))
        
