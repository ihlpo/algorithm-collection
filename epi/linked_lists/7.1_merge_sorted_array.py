from linked_list_template import List_node
from linked_list_template import print_linked_list

def merge_sorted_lists(list1, list2):
    head = tail = List_node()
    

    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next
        
    # tail.next = list1 or list2
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return head.next

x = List_node(2)
x.next = List_node(5)
x.next.next = List_node(7)

y = List_node(3)
y.next = List_node(11)

print_linked_list(merge_sorted_lists(x, y))
