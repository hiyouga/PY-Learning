class PrioQue:
    def __init__(self, elems = []):
        self._elems = list(elems)
        self._elems.sort(reverse = True)
    def is_empty(self):
        return not self._elems
    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue!")
        return self._elems.pop()
    def peek(self):
        if self.is_empty():
            raise Exception("Empty Queue!")
        return self._elems[-1]

class Graph:
    def __init__(self, mat, unconn):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Not Graph!")
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum
    def vertex_num(self):
        return self._vnum
    def _invalid(self, v):
        return 0 > v or v >= self._vnum
    def add_edge(self, vi, vj, val = 1):
        if self._invalid(vi) or self._invalid(vj):
            raise Exception("not valid vertex!")
        self._mat[vi][vj] = val
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise Exception("not valid vertex!")
        return self._mat[vi][vj]
    def out_edges(self, vi):
        if self._invalid(vi):
            raise Exception("not valid vertex!")
        return self._out_edges(self._mat[vi], self._unconn)
    def dijkstra(self, v0):
        paths = [None] * self._vnum
        cnt = 0
        cands = PrioQue([(0, v0, v0)])
        while cnt < self._vnum and not cands.is_empty():
            plen, u, vmin = cands.dequeue()
            if paths[vmin]:
                continue
            paths[vmin] = (u, plen)
            for v, w in self.out_edges(vmin):
                if not paths[v]:
                    cands.enqueue((plen + w, vmin, v))
            cnt += 1
        return paths
    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

def main():
    matrix = []
    init_row = input().split()
    matrix.append(list(map(int, init_row)))
    for i in range(len(matrix[0])-1):
        row = input().split()
        matrix.append(list(map(int, row)))
    vEnd = ord(input()) - ord('A')
    graph = Graph(matrix, -1)
    min_pos = 'A'
    min_dist = 1e9
    for vStart in range(graph.vertex_num()):
        if vStart == vEnd:
            continue
        paths = graph.dijkstra(vStart)
        if paths[vEnd][1] < min_dist:
            min_dist = paths[vEnd][1]
            min_pos = chr(vStart + ord('A'))
    print(min_pos)
    
main()