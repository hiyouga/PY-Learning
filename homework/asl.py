HASH_BASE = 100
def hash(k: int):
    global HASH_BASE
    return k % HASH_BASE

class Node:
    def __init__(self, data, nxt = None):
        self.data = data
        self.nxt = nxt

class HashList:
    def __init__(self):
        self.list = [None] * HASH_BASE
    def add_data(self, n):
        if self.list[hash(n)] is None:
            self.list[hash(n)] = Node(n)
            return
        node = self.list[hash(n)]
        if node.data == n:
            return
        while node.nxt:
            node = node.nxt
            if node.data == n:
                return
        node.nxt = Node(n)
    def asl(self):
        count = 0
        cost = 0
        for node in self.list:
            if node:
                count += 1
                temp = 1
                cost += temp
                while node.nxt:
                    node = node.nxt
                    count += 1
                    temp += 1
                    cost += temp
        return cost/count

def main():
    t = int(input())
    nums = list(map(int, input().split()))
    if t != len(nums):
        return
    table = HashList()
    for n in nums:
        table.add_data(n)
    print("%.2f" % table.asl())
    
main()