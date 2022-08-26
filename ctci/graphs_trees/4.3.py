from collections import deque

class Tree_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

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

def create_linked_lists(node):
    linked_lists = {}
    queue = deque([])
    
    queue.append()

    while queue:
        for i in len(queue):
            temp = queue.popleft()
            if temp.left:
                queue.append(temp.left)




x = create_minimal_bst([1,3,5,7,10,11,15,20,24,30,36])
print(create_linked_lists(x))
