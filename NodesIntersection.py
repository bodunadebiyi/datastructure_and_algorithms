import re

class Node:
  next = None

  def __init__(self, val):
    self.val = val

'''
A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10
'''

list_a = Node(3)
list_a.next = Node(7)
list_a.next.next = Node(8)
list_a.next.next.next = Node(1)

list_b = Node(99)
list_b.next = Node(1)
list_b.next.next = Node(8)
list_b.next.next.next = Node(10)

list_a_hash = {}

current_node = list_a
while current_node:
  list_a_hash[current_node.val] = True
  current_node = current_node.next

result = None
current_node = list_b
while current_node:
  if current_node.val in list_a_hash:
    result = current_node.val
    break
  
  current_node = current_node.next


print(list_a_hash)

a = re.split(r'[\t\n]', '\twe are \there')
print(a)