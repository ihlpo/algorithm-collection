from linked_list_template import List_node
from linked_list_template import print_linked_list
from linked_list_template import generate_linked_list

def reverse_sublist(list, start, finish):
    dummy_node = sublist_head = List_node(0, list)

    for _ in range(1, start):
        sublist_head = sublist_head.next
    
    sublist_counter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_counter.next
        sublist_counter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_node.next

def reverse_list(list):

    prev = None
    current = list

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    return prev

def reverse_sublist2(list, start, finish):
    dummy_node = List_node(0, list)
    left_prev = dummy_node
    current = list

    for i in range(start - 1):
        left_prev = current
        current = current.next
    
    prev = None
    for i in range(finish - start + 1):
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    left_prev.next.next = current
    left_prev.next = prev

    return dummy_node.next

arr = [11, 3, 5, 7, 2]

x = generate_linked_list(arr)

print_linked_list(reverse_sublist2(x,1,5))