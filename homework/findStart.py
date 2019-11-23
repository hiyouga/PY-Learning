import re

class SStack:
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return self._elems == []
    def top(self):
        if self._elems == []:
            raise Exception('Stack is empty when using top()!')
        else:
            return self._elems[-1]
    def push(self, elem):
        self._elems.append(elem)
    def pop(self):
        if self._elems == []:
            raise Exception('Stack is empty when doing pop()!')
        else:
            return self._elems.pop()
    def size(self):
        return len(self._elems)

class Graph:
    def __init__(self, mat, unconn = 0):
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
    def exist(self, v0, vn):
        visited = [0] * self._vnum
        #visited[v0] = 1
        get = False
        st = SStack()
        st.push((0, self.out_edges(v0)))
        while not st.is_empty():
            i, edges = st.pop()
            if i < len(edges):
                v, e = edges[i]
                st.push((i+1, edges))
                if not visited[v]:
                    if v == vn:
                        get = True
                    else:
                        visited[v] = 1
                        oes = self.out_edges(v)
                        for (tempv, tempe) in oes:
                            if visited[tempv]:
                                return False
                        st.push((0, oes))
        return get
    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

def main():
    param = input().split()
    n = int(param[0])
    matrix = [([0] * n) for i in range(n)]
    ind2chr = [0] * n
    namedic = {}
    vallist = []
    for i in range(n):
        line = input()
        pattern = re.compile(r'([A-Z])\: \{(.*)\}', re.I)
        m = pattern.match(line)
        namedic[m.group(1)] = i
        ind2chr[i] = m.group(1)
        vallist.append(m.group(2))
    for i in range(len(vallist)):
        for p in vallist[i].split(', '):
            pattern = re.compile(r'([A-Z])\:([0-9])', re.I)
            m = pattern.match(p)
            matrix[i][namedic[m.group(1)]] = int(m.group(2))
    vStop = namedic[param[1]]
    graph = Graph(matrix, 0)
    output = []
    for j in range(n):
        if j != vStop and graph.exist(j, vStop):
            output.append(ind2chr[j])
    if len(output):
        print(' '.join(output))
    else:
        print("None")
    
main()
