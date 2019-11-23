class BTNode:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None
        self.a = 0
        self.b = 0
    def is_empty(self):
        return self.root is None
    def build(self, vals, qst):
        self.a, self.b = qst
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
                    
    def postorder(self):
        stack = []
        ptr = self.root
        while ptr or len(stack):
            while ptr:
                stack.append(ptr)
                ptr = ptr.left if ptr.left is not None else ptr.right
            ptr = stack.pop()
            if self.preorder(ptr):
                return ptr.data
            if len(stack) and stack[-1].left == ptr:
                ptr = stack[-1].right
            else:
                ptr = None
    
    def preorder(self, ptr):
        stack = []
        qst = [self.a, self.b]
        while ptr != None or len(stack) != 0:
            while ptr != None:
                if ptr.data in qst:
                    qst.pop(qst.index(ptr.data))
                stack.append(ptr)
                ptr = ptr.left
            if len(stack) != 0:
                ptr = stack.pop()
                ptr = ptr.right
        if len(qst) == 0:
            return True
        else:
            return False

def main():
    s = input().split()
    a = input()
    b = input()
    tree = BTree()
    tree.build(s, [a, b])
    print(tree.postorder())
    
main()


'''
34 2 4 0 None None None None 53 45 23 52 6
6
23
'''