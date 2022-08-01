from linked_list_template import List_node
from linked_list_template import print_linked_list
from linked_list_template import generate_linked_list

def reverse_sublist(list, start, finish):
    head = sublist_head = List_node(0, list)

    for _ in range(1, start):
        sublist_head = sublist_head.next
    
    sublist_counter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_counter.next
        sublist_counter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return head.next

arr = [11, 3, 5, 7, 2]

x = generate_linked_list(arr)
print_linked_list(reverse_sublist(x, 2, 6))