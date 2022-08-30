class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

a = Node(10, None, Node(20, Node(15), Node(24, Node(22))))
b = Node(20, Node(15), Node(24))

def is_subtree(tree1, tree2):
    def preorder_append(node, array):
        if not node:
            array.append(0)
            return array
        array.append(node.value)
        preorder_append(node.left, array)
        preorder_append(node.right, array)
        return array


    list1 = preorder_append(tree1, [])
    list2 = preorder_append(tree2, [])

    sublist = False
    length1 = len(list1)
    length2 = len(list2)
    count1 = 0
    count2 = 0
    while count1 < length1:
        if list1[count1] == list2[count2]:
            sublist = True
            if count2 == length2:
                return True
        else:
            sublist = False
            count2 = -1
        count1 += 1
        count2 += 1
    return sublist


print(is_subtree(a, b))