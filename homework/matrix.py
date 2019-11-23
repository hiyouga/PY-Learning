class Matrix:
    def __init__(self):
        self.content = [0] * 16
    def get_pos(self, x, y):
        return self.content[(x - 1) * 4 + y - 1]
    def set_pos(self, x, y, value):
        self.content[(x - 1) * 4 + y - 1] = value
    def initialize(self, matlist):
        for i in range(4):
            for j in range(4):
                self.set_pos(i+1, j+1, matlist[i][j])

    def output(self):
        for t1 in range(1,5):
            print('|', end='')
            for t2 in range(1,5):
                print("%5d" % self.get_pos(t1, t2), end='') 
            print('    |')

    def trans(self):  # 求转置矩阵
        trans = Matrix()
        for p1 in range(1, 5):
            for p2 in range(1, 5):
                trans.set_pos(p2, p1, self.get_pos(p1, p2))
        return trans 

    def plus(self, m2):
        res = Matrix()
        for i in range(1, 5):
            for j in range(1, 5):
                s = self.get_pos(i, j) + m2.get_pos(i, j)
                res.set_pos(i, j, s)
        return res

    def multiply(self, m2):
        res = Matrix()
        for i in range(1, 5):
            for j in range(1, 5):
                s = 0
                for k in range(1, 5):
                    s += self.get_pos(i, k) * m2.get_pos(k, j)
                res.set_pos(i, j, s)
        return res


if True:  # 以下为主程序 
    N = 4  # 方阵阶数 
    array1 = [] 
    array2 = [] 
    for i1 in range(0, N): 
        array1.append([]) 
        array1[i1] = input().split() 
        for i2 in range(0, N): 
            array1[i1][i2] = int(array1[i1][i2]) 

    for j1 in range(0, N): 
        array2.append([]) 
        array2[j1] = input().split() 
        for j2 in range(0, N): 
            array2[j1][j2] = int(array2[j1][j2])

    print(array1)
    x = Matrix() 
    print("x before initialization:") 
    x.output() 
    x.initialize(array1) 
    print("x after initialization:") 
    x.output() 
    y = Matrix() 
    y.initialize(array2) 
    print("y after initialization:") 
    y.output() 
    print() 

    del array1 
    del array2 

    xT = x.trans() 
    print("Transpose x is:") 
    xT.output() 
    print("Transpose y is:") 
    y.trans().output() 
    print("Transpose x+y is:") 
    z = x.plus(y).trans() 
    z.output() 
    print("x*y is:") 
    w = x.multiply(y) 
    w.output()
