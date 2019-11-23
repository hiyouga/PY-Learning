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
    def build(self, preorder, inorder):
        self.root = self.recover(preorder, inorder)
    def recover(self, preorder, inorder):
        root = BTNode(preorder[0])
        if len(preorder) == 0 and len(inorder) == 0:
            return root
        idx = inorder.index(preorder[0])
        if idx > 0:
            root.left = self.recover(preorder[1:idx+1], inorder[0:idx])
        if len(inorder) - idx - 1 > 0:
            root.right = self.recover(preorder[idx+1:], inorder[idx+1:])
        return root
    def postorder(self):
        stack = []
        out = []
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
    preorder = input().split()
    inorder = input().split()
    tree = BTree()
    tree.build(preorder, inorder)
    tree.postorder()
main()