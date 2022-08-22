'''These are the common types of tree traversals. These tree traversals are ofter used for binary trees'''

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
