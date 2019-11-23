sent = input().split(' ')
tag = input().split(' ')
pre = False
out = ''
for i in range(len(sent)):
    if tag[i] == 'O':
        if pre:
            out += '</LOC>' + sent[i]
        else:
            out += sent[i]
        pre = False
    elif tag[i] == 'B-LOC':
        if pre:
            out += '</LOC><LOC>' + sent[i]
        else:
            out += '<LOC>' + sent[i]
        pre = True
    elif tag[i] == 'I-LOC':
        out += sent[i]
        pre = True
if pre:
    out += '</LOC>'
print(out)
