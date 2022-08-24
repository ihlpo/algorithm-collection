class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

'''These are the common types of tree traversals. These tree traversals are ofter used for binary trees'''
def build_tree(tree_dict):
    root_exist = False
    for node, children in tree_dict.items():
        
        if not root_exist:
            root = Node(node, children[0], children[1])
            root_exist = True
        else:
            Node(node, children[0], children[1])
    return root

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.value)
    inrder(node.right)


def preorder(node):
    if not node:
        return
    print(node.value)
    preorder(node.left)
    preoder(node.right)


def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.rignt)
    print(node.value)
