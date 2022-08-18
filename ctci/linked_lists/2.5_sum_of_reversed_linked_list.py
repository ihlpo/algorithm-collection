from template import List_node
from template import print_linked_list
from template import generate_linked_list

def sum_lists(list1, list2):
    '''O(n) time as we tranverse both linked list. O(n) space for the longer node from list1 or list2'''
    result_list = head = List_node()
    carry = 0
    current1 = list1
    current2 = list2
    
    while current1 and current2:
        result = current1.data + current2.data
        if carry == 0:
            if result > 9:
                carry =  1
                result = result - 10
                head.next = List_node(result)

            else:
                head.next = List_node(result)
        else:
            if result > 9:
                result = result - 10
                head.next = List_node(result + 1)
                carry = 1

            else:
                head.next = List_node(result + 1)
                carry = 0
        head = head.next
        current1 = current1.next
        current2 = current2.next
    
    while current1:
        result = current1.data + carry
        if carry == 0:
            if result > 9:
                carry =  1
                result = result - 10
                head.next = List_node(result)

            else:
                head.next = List_node(result)
        else:
            if result > 9:
                result = result - 10
                head.next = List_node(result)
                carry = 1

            else:
                head.next = List_node(result)
                carry = 0
        head = head.next
        current1 = current1.next
    while current2:
        result = current2.data + carry
        if carry == 0:
            if result > 9:
                carry =  1
                result = result - 10
                head.next = List_node(result)

            else:
                head.next = List_node(result)
        else:
            if result > 9:
                result = result - 10
                head.next = List_node(result)
                carry = 1

            else:
                head.next = List_node(result)
                carry = 0
        head = head.next
        current2 = current2.next

    if carry:
        head.next = List_node(1)

    return result_list.next

def sum_lists_recursive(x,y):
    result_list = head = List_node()
    global_carry = 0

    def recurse(list1, list2, head, carry):
        if list1 and list2:
            result = list1.data + list2.data + carry
            if result > 9:
                result = result - 10
                head.next = List_node(result)
            else:
                head.next = List_node(result)
                recurse(list1.next, list2.next, head.next, 0)
        return carry

    def count_nodes(head):
        if not head:
            return 0
        return count_nodes(head.next) + 1
    
    def fill_list(less, difference):
        
        while less and less.next:
            less = less.next
        while difference:
            less.next = List_node(0)
            less = less.next
            difference -= 1
    
    if count_nodes(x) == count_nodes(y):
        recurse(x,y,result_list, 0)
    else:
        if count_nodes(x) < count_nodes(y):
            fill_list(x, count_nodes(y) - count_nodes(x))
        else:
            fill_list(y, count_nodes(x) - count_nodes(y))
            print(recurse(x,y,result_list, 1))
    return result_list.next


x = generate_linked_list([1,3,4,5])
y = generate_linked_list([1,2,3,3])

print_linked_list(sum_lists_recursive(x,y))
        
