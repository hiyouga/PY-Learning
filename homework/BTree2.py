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
        num = 1
        ans = [self.root.data]
        while len(queue):
            wqueue = []
            out = []
            while len(queue):
                node = queue.pop(0)
                if len(vals):
                    val = vals.pop(0)
                    if val != "None":
                        out.append(val)
                        node.left = BTNode(val)
                        wqueue.append(node.left)
                if len(vals):
                    val = vals.pop(0)
                    if val != "None":
                        out.append(val)
                        node.right = BTNode(val)
                        wqueue.append(node.right)
            queue = wqueue
            if num % 2 == 1:
                out.reverse()
            num += 1
            ans += out
        print(" ".join(ans))

def main():
    s = input().split()
    tree = BTree()
    tree.build(s)

main()
