from template import List_node
from template import print_linked_list
from template import generate_linked_list

def kth_last_node(k, list):
  '''O(n) time and O(1) time. First traverse the linked list to find the length.
  onces you have the length you can find the kth last element with length-k'''
  count = 0
  counter = list
  while counter:
    count += 1
    counter = counter.next
  
  count = count - k
  current = list
  count2 = 1
  while list and count2 <= count:
    current = current.next
    count2 += 1

  return current
  
def kth_to_last_recursive(k, list):
  def recur(list):
    if not list:
      return
    if count == k:
      return
    recur(list.next)
    print(list.data)
    count += 1
  recur(list)

def kth_last_node_iter(k, list):
  '''O(n) time and O(1) space. If you know k, you can have 2 pointers you can have a one pointer to first run k steps,
  then the 2 points can step together. when the faster pointer hits the end, the slower pointer will be at the kth last
  element.'''
  slow = fast = list

  for i in range(k):
    fast = fast.next
  
  while fast:
    fast = fast.next
    slow = slow.next

  return slow


x = generate_linked_list([1,2,3,4,4,6,7,8])
print_linked_list(kth_last_node_iter(3,x))
