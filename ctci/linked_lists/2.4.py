from template import List_node
from template import print_linked_list
from template import generate_linked_list

def partition(part, list):
    '''O(n) with 2 passes. O(n) space'''
    new_list = head = List_node()
    current = list
    while current: #First iteration
        if current.data < part:
            head.next = List_node(current.data)
            head = head.next
    current = current.next
  
    current = list  
    while current:
        if current.data >= part:
            head.next = List_node(current.data)
            head = head.next
    current = current.next
  
    return new_list.next
  
def partition2(x, list):
    '''O(n) time with 1 pass. O(n) space'''
    head = less_list = List_node()
    head2 = greater_list = List_node()

    current = list
    while current:
        if current.data < x:
            less_list.next = List_node(current.data)
            less_list = less_list.next
        else:
            greater_list.next = List_node(current.data)
            greater_list = greater_list.next
        current = current.next

        less_list.next = head2.next

    return head.next

x = generate_linked_list([3,5,8,5,10,2,1])
print_linked_list(partition2(5,x))
