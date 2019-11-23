import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding='utf-8')

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
                raise Exception("Not Graph!")
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

def same_line(line_dict, pi, pj):
    lno = None
    for no, line in line_dict.items():
        if pi in line and pj in line:
            lno = no
    return lno

def main():
    file = open('bgstations_pinyin.txt', 'rb')
    line_num = int(file.readline().decode('utf-8'))
    line_dict = {}
    name_dict = {}
    ind2name = []
    city_num = 0
    for i in range(line_num):
        no, stop_num = file.readline().decode('utf-8').split()
        line_dict[no] = []
        for j in range(int(stop_num)):
            name, trans = file.readline().decode('utf-8').split()
            if not name in name_dict.keys():
                name_dict[name] = city_num
                ind2name.append(name)
                city_num += 1
            line_dict[no].append(name_dict[name])
        file.readline()
    file.close()
    vStart = input()
    vEnd = input()
    out = []
    matrix = [([0] * city_num) for i in range(city_num)]
    for v in line_dict.values():
        for i in range(len(v)-1):
            matrix[v[i]][v[i+1]] = 1
            matrix[v[i+1]][v[i]] = 1
    graph = Graph(matrix, 0)
    paths = graph.dijkstra(name_dict[vStart])
    p = name_dict[vEnd]
    path = [p]
    while paths[p][1] != 0:
        p = paths[p][0]
        path.append(p)
    path.reverse()
    path_num = 1
    current_line = None
    for i in range(len(path)-1):
        no = same_line(line_dict, path[i], path[i+1])
        if (not current_line) or (no != current_line):
            if current_line:
                out.append(str(current_line) + '(' + str(path_num) + ')')
            out.append(ind2name[path[i]])
            current_line = no
            path_num = 1
        else:
            path_num += 1
    out.append(str(current_line) + '(' + str(path_num) + ')')
    out.append(ind2name[path[-1]])
    print('-'.join(out))
main()
