class Binary_tree():
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def inorder_traversal(tree):
    # in order traversal without using recursion by using stack to mimic the call stack
    stack = []
    result = []

    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            result.append(tree.data)
            tree = tree.right
    return result
