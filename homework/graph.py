def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi, vj, w))
            if len(mst) == vnum-1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst

def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = PrioQueue([(0, 0, 0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w, v, vi))
    return mst

def Dijkstra(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    count = 0
    cands = PrioQueue([(0, v0, v0)])
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths

def Floyd(graph):
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j) for j in range(vnum)] for i in range(vnum)]
    nvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)] for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]
    return (a, nvertex)