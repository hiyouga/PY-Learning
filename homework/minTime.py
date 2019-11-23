import re

class SQueue:
	def __init__(self, init_len=8):
		self.__elem = [0] * init_len
		self.__len = init_len
		self.__head = 0
		self.__num = 0
	def __extend(self):
		old_len = self.__len
		self.__len *= 2
		new_elems = [0] * self.__len
		for i in range(old_len):
			new_elems[i] = self.__elem[(self.__head + i) % old_len]
		self.__elem, self.__head = new_elems, 0
	def is_empty(self):
		return self.__num == 0
	def peek(self):
		if self.__num == 0:
			raise Exception('Queue is empty when doing peek()!')
		return self.__elem[self.__head]
	def enqueue(self, e):
		if self.__num == self.__len:
			self.__extend()
		self.__elem[(self.__head + self.__num) % self.__len] = e
		self.__num += 1
	def dequeue(self):
		if self.__num == 0:
			raise Exception('Queue is empty when doing dequeue()!')
		e = self.__elem[self.__head]
		self.__head = (self.__head + 1) % self.__len
		self.__num -= 1
		return e

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
    def minTime(self, v0):
        ans = 0
        visited = [0] * self._vnum
        visited[v0] = 1
        seq = [v0]
        sq = SQueue()
        sq.enqueue((0, self.out_edges(v0)))
        while not sq.is_empty():
            i, edges = sq.dequeue()
            for j in range(len(edges)):
                v, e = edges[j]
                if not visited[v]:
                    seq.append(v)
                    visited[v] = 1
                    sq.enqueue((i+1, self.out_edges(v)))
                    ans = max([ans, i+1])
        return ans
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
    vStart = namedic[param[1]]
    graph = Graph(matrix, 0)
    print(graph.minTime(vStart))
    
main()