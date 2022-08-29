import math
from collections import deque

class Tree_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

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

def create_linked_lists_bfs(node):
    """O(n) time complexity for the total number of nodes if nodes are skewed. O(n) space
    as we are create new linked listed from existing nodes"""
    linked_lists = {}
    queue = deque([])
    
    queue.append(node)
    depth = 0
    while queue:
        head = tail = Node()
        for i in range(len(queue)):
            temp = queue.popleft()
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            
            tail.next_node = Node(temp.value)
            tail = tail.next_node
        
        linked_lists[depth] = head.next_node
        
        depth += 1
    
    return linked_lists

def create_linked_list_traversal(node):
    """O(n) time complexity by traversing all the nodes. There is a recursive stack call of O(log n) but O(n) dominates
    O(n) space complexity for extra nodes created in linked list. A modified preorder traversal was used.
    Make sure to pass in the node depth for each recursive call"""
    linked_list = {}
    def traversal(linked_list, node, depth):
        if not node:
            return
        if depth not in linked_list:
            linked_list[depth] = Node(node.value)
        else:
            pointer = linked_list[depth]
            while pointer.next_node:
                pointer = pointer.next_node
            pointer.next_node = Node(node.value)

        traversal(linked_list, node.left, depth + 1)
        traversal(linked_list, node.right, depth + 1)

    traversal(linked_list, node, 0)
    return linked_list


# x = create_minimal_bst([1,3,5,7,10,11,15,20,24,30,36,40,50,60,76])

# y = create_linked_list_traversal(x)

# for k, node in y.items():
#     print(f"depth {k}")
#     while node:
#         print(node.value)
#         node = node.next_node
