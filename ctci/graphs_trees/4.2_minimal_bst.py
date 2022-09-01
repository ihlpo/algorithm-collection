import math
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_minimal_bst(array):
    '''A key intuitiion for this algorithm is from recognising a BST is composed of multiple subtrees. Since the array
    sorted, we can safely have the middle value in the array to be the root node, have the left child to be values to the
    left of the middle value, and have the right child to be values to the right of the middle value. We can use recursion
    to break down the problem and recursively add subtrees using partitioned arrays. you want the node to be the
    mid value of the tree'''    
    def create_minimal_bst_helper(array, start, end):
        if end < start:
            return None
        mid = math.floor((start + end) / 2)
        node = Node(array[mid])
        node.left = create_minimal_bst_helper(array, start, mid - 1)
        node.right = create_minimal_bst_helper(array, mid + 1, end)
        return node

    return create_minimal_bst_helper(array, 0, len(array) - 1)