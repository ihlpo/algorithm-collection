from template import List_node
from template import print_linked_list
from template import generate_linked_list

def remove_duplicates(list):
  new_list = tail = List_node()
  seen = {}
  current = list

  while current:
    if current.data not in seen:
      seen[current.data] = 0
    current = current.next

  for i in seen.keys():
    tail.next = List_node(i)
    tail = tail.next

  return new_list.next

def remove_duplicates2(list):
  prev = dummy = List_node(0, list)
  seen = {}
  current = prev.next

  while current:
    if current.data in seen:
      current = current.next
    else:
      seen[current.data] = 0
      prev.next = current
      current = current.next
      prev = prev.next
  
  prev.next = current
  return dummy.next

def remove_duplicates3(list):
  current = list
  
  while current and current.next:
    distinct = current
    while distinct and distinct.next:
      if distinct.next.data == current.data:
        distinct.next = distinct.next.next

      else:
        distinct = distinct.next

    current = current.next

  return list


x = generate_linked_list([1,4,3,3,3,3,2,4])
print_linked_list(remove_duplicates3(x))


