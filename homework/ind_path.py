def bfs(points, check, vi, trace):
    if check[vi]:
        return
    if vi == len(points) - 1:
        print(' '.join(list(map(str, trace))))
    for e, vi, vj in points[vi]:
        ntrace = trace[:]
        ntrace.append(e)
        ncheck = check[:]
        ncheck[vi] = True
        bfs(points, ncheck, vj, ntrace)

def main():
    n, e = map(int, input().split())
    points = [[] for i in range(n)]
    for i in range(e):
        e, vi, vj = map(int, input().split())
        points[vi].append((e, vi, vj))
        points[vj].append((e, vj, vi))
    bfs(points, [False] * n, 0, [])
main()