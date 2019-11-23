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
        while len(queue) != 0:
            node = queue.pop(0)
            if len(vals) != 0:
                val = vals.pop(0)
                if val != "None":
                    node.left = BTNode(val)
                    queue.append(node.left)
            if len(vals) != 0:
                val = vals.pop(0)
                if val != "None":
                    node.right = BTNode(val)
                    queue.append(node.right)
    def preorder(self):
        stack = []
        out = []
        ptr = self.root
        while ptr or len(stack):
            while ptr:
                out.append(ptr.data)
                stack.append(ptr)
                ptr = ptr.left
            if len(stack):
                ptr = stack.pop()
                ptr = ptr.right
        print(" ".join(out))
    
def main():
    s = input().split()
    tree = BTree()
    tree.build(s)
    tree.preorder()
    
main()