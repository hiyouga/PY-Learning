class BTNode:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None
        self.found = False
    def is_empty(self):
        return self.root is None
    def build(self, vals):
        self.root = BTNode(int(vals.pop(0)))
        queue = [self.root]
        while len(queue) != 0:
            node = queue.pop(0)
            if len(vals) != 0:
                val = vals.pop(0)
                if val != "None":
                    node.left = BTNode(int(val))
                    queue.append(node.left)
            if len(vals) != 0:
                val = vals.pop(0)
                if val != "None":
                    node.right = BTNode(int(val))
                    queue.append(node.right)
    def find(self, num):
        self.dfs(self.root, 0, num)
        if self.found:
            print("True")
        else:
            print("False")
    def dfs(self, node, val, num):
        val += node.data
        if val == num:
            self.found = True
        if node.left:
            self.dfs(node.left, val, num)
        if node.right:
            self.dfs(node.right, val, num)
    
    
def main():
    n = int(input())
    s = input().split()
    tree = BTree()
    tree.build(s)
    tree.find(n)
    
main()