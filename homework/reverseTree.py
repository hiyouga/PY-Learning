import math

class BTNode:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root is None
    def build(self, vals):
        self.root = BTNode(vals.pop(0))
        queue = [self.root]
        ans = [self.root.data]
        while len(queue):
            wqueue = []
            out = []
            while len(queue):
                node = queue.pop(0)
                if len(vals):
                    val = vals.pop(0)
                    out.append(val)
                    if val != "None":
                        node.left = BTNode(val)
                        wqueue.append(node.left)
                if len(vals):
                    val = vals.pop(0)
                    out.append(val)
                    if val != "None":
                        node.right = BTNode(val)
                        wqueue.append(node.right)
            queue = wqueue
            out.reverse()
            ans += out
        return ans
    
    def preorder(self):
        stack = []
        out = []
        ptr = self.root
        while ptr != None or len(stack) != 0:
            while ptr != None:
                out.append(ptr.data)
                stack.append(ptr)
                ptr = ptr.left
            if len(stack) != 0:
                ptr = stack.pop()
                ptr = ptr.right
        print(" ".join(out))
    
    def inorder(self):
        stack = []
        out = []
        ptr = self.root
        while ptr or len(stack):
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack.pop()
                out.append(ptr.data)
                ptr = ptr.right
        print(" ".join(out))

def main():
    s = input().split()
    while len(s) < 2**math.ceil(math.log(len(s)+1, 2)) - 1:
        s.append("None")
    tree = BTree()
    tree.build(tree.build(s))
    tree.preorder()
    tree.inorder()

main()