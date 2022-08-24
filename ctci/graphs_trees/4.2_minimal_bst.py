import math
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_minimal_bst(array):
    
    def create_minimal_bst_helper(array, start, end):
        if end < start:
            return None
        mid = math.floor((start + end) / 2)
        node = Node(array[mid])
        node.left = create_minimal_bst_helper(array, start, mid - 1)
        node.right = create_minimal_bst_helper(array, mid + 1, end)
        return node


    return create_minimal_bst_helper(array, 0, len(array) - 1)

def inorder(node):
    if not node:
        return None
    
    inorder(node.left)
    print(node.value)
    inorder(node.right)
    

x = create_minimal_bst([1,2,4,6,10])
inorder(x)