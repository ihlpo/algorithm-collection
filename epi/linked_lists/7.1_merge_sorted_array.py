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
        
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return head.next