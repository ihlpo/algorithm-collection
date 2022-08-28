def successor(node):
    """O(h) time where h is the depth of the node. O(1) constant space"""
    def find_left_most_child(node):
        if not tree:
            return
        while node.left:
            node = node.left
        return node
    
    if node.right:
        return find_left_most_child(node.right)
    else:
        temp = node
        parent_node = node.parent
         #This condition checks that a parent exist and whether temp is on the right parent
         # We need temp to be on the left of the parent_node. We keep moving up until its on the left
         # Then we return the parent
        while parent_node and parent_node.left is not temp:
            temp = parent_node
            parent_node = parent_node.parent
        return parent_node if parent_node else None
