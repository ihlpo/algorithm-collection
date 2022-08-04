from linked_list_template import List_node
from linked_list_template import print_linked_list
from linked_list_template import generate_linked_list

def even_odd_merge(list1, list2): #O(n) O(n) Brute force
    even_head = even_list = List_node()
    odd_head = odd_list = List_node()

    while list1 or list2:
        if list1:
            if list1.data % 2 == 0:
                even_list.next = list1
                list1 = list1.next
                even_list = even_list.next
            else: 
                odd_list.next = list1
                list1 = list1.next
                odd_list = odd_list.next
        if list2:
            if list2.data % 2 == 0:
                even_list.next = list2 
                list2 = list2.next
                even_list = even_list.next
            else:
                odd_list.next = list2
                list2 = list2.next
                odd_list = odd_list.next
    
    prev = even_list
    current = prev.next

    while current:
        prev = current
        current = current.next
    
    prev.next = odd_head.next

    return even_head.next


arr1 = [2,4,6,7]
arr2 = [11,36,12]

x = generate_linked_list(arr1)
y = generate_linked_list(arr2)

print_linked_list(even_odd_merge(x,y))