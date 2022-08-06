class Binary_tree():
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def inorder_traversal(tree): #O(n) O(h) from the recursive stack
    if tree:
        inorder_traversal(tree.left)
        print(tree.data)
        inorder_traversal(tree.right)

    return

def preorder_traversal(tree): #O(n) O(h) from the recursive stack
    if tree:
        print(tree.data)
        preorder_traversal(tree.left)
        preorder_traversal(tree.right)

    return

def postorder_traversal(tree): #O(n) O(h) from the recursive stack
    if tree:
        postorder_traversal(tree.left)
        postorder_traversal(tree.right)
        print(tree.data)
    return