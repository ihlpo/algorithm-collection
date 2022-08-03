def remove_kth_node(list, k): #O(n) O(1)
    length = 0
    dummy_node = List_node(0,list)
    counter = list

    while counter: #gets the length
        length += 1
        counter = counter.next

    prev = None
    current = list
    for i in range(length - k):
        prev = current 
        current = current.next   
    
    prev.next = current.next

    return list

def remove_kth_node2(list, k): #O(n) Time O(1) Space
    dummy_node = List_node(0, list)
    first = second = list
    prev = dummy_node
    for i in range(k):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
        prev = prev.next
    
    prev.next = prev.next.next

    return dummy_node.next

def remove_kth_node3(list, k): #O(n) Time O(1) Space
    dummy_node = List_node(0, list)
    first = second = dummy_node
    for i in range(k + 1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next

    return dummy_node.next