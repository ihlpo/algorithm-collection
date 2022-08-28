import math

class Tree_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_minimal_bst(array):  
    def create_minimal_bst_helper(array, start, end):
        if end < start:
            return None
        mid = math.floor((start + end) / 2)
        node = Tree_node(array[mid])
        node.left = create_minimal_bst_helper(array, start, mid - 1)
        node.right = create_minimal_bst_helper(array, mid + 1, end)
        return node


    return create_minimal_bst_helper(array, 0, len(array) - 1)

def is_balanced(tree):
    """A balanced tree when the height of of its subtree is not greater than 1.
    O(n) time complextity as the algorithm will need to check the entire tree.
    O(H) where h is the height of the tree for the call stack. The alogrithm recurses through the tree
    and while passing the depth and returning the depth of the deepest node when it hits null.
    since there are 2 children for each subtree you will need to return the maximum depth.
    Then check if the difference is larger than 1"""
    
    def checker(tree, depth):
        if not tree:
            return depth
        return max(checker(tree.left, depth + 1), checker(tree.right, depth + 1))

    return abs(checker(tree.left, 1) - checker(tree.right, 1)) <= 1


x = create_minimal_bst([1,3,5,7,10,11,15,20,24,30,36,40,50,60,76])

y = Tree_node(10, Tree_node(5), Tree_node(30))
y.right.right = Tree_node(40)
y.right.right.right = Tree_node(35)
y.right.right.right.right = Tree_node(60)
print(is_balanced(x))
