class BTNode:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None
        self.is_comp = True
        self.num = 0
    def is_empty(self):
        return self.root is None
    def build(self, preorder, inorder):
        self.num = len(preorder)
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
    def judge(self):
        queue = [self.root]
        i = 0
        while len(queue):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            elif 2 * i + 1 < self.num:
                self.is_comp = False
            if node.right:
                queue.append(node.right)
            elif 2 * i + 2 < self.num:
                self.is_comp = False
            i += 1

def main():
    preorder = input().split()
    inorder = input().split()
    tree = BTree()
    tree.build(preorder, inorder)
    tree.judge()
    if tree.is_comp is True:
        print("True")
    else:
        print("False")
main()