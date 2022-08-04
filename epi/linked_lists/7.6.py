from linked_list_template import List_node
from linked_list_template import print_linked_list
from linked_list_template import generate_linked_list
# from linked_list_template import delete_node

arr = [11, 3, 5, 7, 2]

x = generate_linked_list(arr)

print_linked_list(x)

x.delete_node(5)

print_linked_list(x)

