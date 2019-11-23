import re

def main():
    n = int(input())
    matrix = [(['0'] * n) for i in range(n)]
    namedic = {}
    vallist = []
    for i in range(n):
        line = input()
        pattern = re.compile(r'([A-Z])\: \{(.*)\}', re.I)
        m = pattern.match(line)
        namedic[m.group(1)] = i
        vallist.append(m.group(2))
    for i in range(len(vallist)):
        for p in vallist[i].split(', '):
            pattern = re.compile(r'([A-Z])\:([0-9])', re.I)
            m = pattern.match(p)
            matrix[i][namedic[m.group(1)]] = m.group(2)
            
    for i in range(n):
        print(' '.join(matrix[i]))
    
main()

'''
3
A: {B:1, C:2}
B: {C:3}
C: {A:1}
'''