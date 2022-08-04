def delet_all_duplicate_nodes(head): #O(n) Time O(n) Space
    dummy_node = List_node(0, head)
    prev = dummy_node
    current = dummy_node.next
    seen = {}

    while current:
        if current.data in seen:
            prev.next = prev.next.next
        else:
            seen[current.data] = current.data

        prev = current
        current = current.next   

    return dummy_node.next

def delet_all_duplicate_nodes2(head): #O(n) Time O(1) Space
    '''
    Delete the successive node if it has the same value as the current node
    '''
    current = head

    while current:
        next_distinct = current.next
        while next_distinct and next_distinct.data == current.data:
            next_distinct = next_distinct.next
        current.next = next_distinct
        current = current.next

    return head