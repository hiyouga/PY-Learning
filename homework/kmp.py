def naive_matching(s, p):
    m, n = len(s), len(p)
    i = 0
    while i < m:
        t = i
        j = 0
        while s[t] == p[j]:
            t, j = t+1, j+1
            if j == n:
                return i
        i += 1
    return -1

def gen_pnext(p):
    m = len(p)
    pnext = [-1] * m
    i = 0
    k = -1
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def kmp_matching(s, p, pnext):
    m, n = len(s), len(p)
    i, j = 0, 0
    while i < m:
        if j == -1 or s[i] == p[j]:
            i, j = i+1, j+1
        else:
            j = pnext[j]
        if j == n:
            return i-n
    return -1

if __name__ == '__main__':
    s = 'ababcaaabcacbab'
    p = 'aacaabcaacda'
    pnext = gen_pnext(p)
    print(naive_matching(s, p))
    print(kmp_matching(s, p, pnext))
    print(''.join(map(str, pnext)))
    print(' '+p)