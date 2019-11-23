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
    def kruskal(self):
        reps = [i for i in range(self._vnum)]
        mst, edges = [], []
        for vi in range(self._vnum):
            for v, w in self.out_edges(vi):
                edges.append((w, vi, v))
        edges.sort()
        for w, vi, vj in edges:
            if reps[vi] != reps[vj]:
                mst.append(w)
                if len(mst) == self._vnum - 1:
                    break
                rep, orep = reps[vi], reps[vj]
                for i in range(self._vnum):
                    if reps[i] == orep:
                        reps[i] = rep
        return sum(mst)
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
    graph = Graph(matrix, -1)
    print(graph.kruskal())
    
main()