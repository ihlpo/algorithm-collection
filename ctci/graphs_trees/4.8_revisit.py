class Node:
    def __init__(self, value, parent= None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

h = Node(31)
g = Node(35,None,h)
f = Node(40,None,g)
e = Node(7,None)
d = Node(1,None)
c = Node(30, None, None, f)
b = Node(5, None, d, e)
a = Node(10, None, b, c)

h.parent = g
g.parent = f
f.parent = c
c.parent = a
d.parent = b
e.parent = b
b.parent = a

def common_ancestor(node1, node2):
    """This algorithm only works if the nodes have a parent property. The algorithm traversals up the tree
    by calling both nodes' parents and when both nodes are the same, we can return. We need to first make
    sure the comparisons are being done on the same depth. we will first need to traversal up to the parent
    for each node individually to count the depth. Once the depths have been calculated we can find the
    difference and traveral the deeper node up. when the depths are the same, we can start our equality
    check. O(d) time where d is the deepest node. O(1) space from
    using references."""

    if not node1 or not node2:
        return None

    node_depth1 = 0
    node_depth2 = 0
    counter1 = node1 #Since we are working with references, we cannot reuse main reference since we will lose its initial state
    counter2 = node2
    while counter1.parent:
        counter1 = counter1.parent
        node_depth1 += 1
    while counter2.parent:
        counter2 = counter2.parent
        node_depth2 += 1
    if node_depth1 > node_depth2:
        diff = node_depth1 - node_depth2
        for i in range(diff):
            node1 = node1.parent
    elif node_depth2 > node_depth1:
        diff = node_depth2 - node_depth1
        for i in range(diff):
            node2 = node2.parent
    
    while node1 and node2:
        if node1 is node2:
            return node1.value
        node1 = node1.parent
        node2 = node2.parent

