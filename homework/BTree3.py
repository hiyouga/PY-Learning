class BTNode:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None
        self.sym = "Yes"
    def is_empty(self):
        return self.root is None
    def build(self, vals):
        self.root = BTNode(vals.pop(0))
        queue = [self.root]
        while len(queue):
            wqueue = []
            data = []
            while len(queue):
                node = queue.pop(0)
                if len(vals):
                    val = vals.pop(0)
                    data.append(val)
                    if val != "None":
                        node.left = BTNode(val)
                        wqueue.append(node.left)
                if len(vals):
                    val = vals.pop(0)
                    data.append(val)
                    if val != "None":
                        node.right = BTNode(val)
                        wqueue.append(node.right)
            for i in range(len(data) // 2):
                if data[i] != data[-1-i]:
                    self.sym = "No"
            queue = wqueue
    def postorder(self):
        stack = []
        out = [self.sym]
        ptr = self.root
        while ptr or len(stack):
            while ptr:
                stack.append(ptr)
                ptr = ptr.left if ptr.left is not None else ptr.right
            ptr = stack.pop()
            out.append(ptr.data)
            if len(stack) and stack[-1].left == ptr:
                ptr = stack[-1].right
            else:
                ptr = None
        print(" ".join(out))
        
def main():
    s = input().split()
    tree = BTree()
    tree.build(s)
    tree.postorder()
    
main()