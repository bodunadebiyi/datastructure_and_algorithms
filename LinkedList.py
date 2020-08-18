class Node(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)

class LinkedList(object):
  def __init__(self, *args):
    self.length = 0
    self.head = None
    self.tail = None
    self.append_nodes(*args)


  def __iter__(self):
    self.iterator = self.head
    return self

 
  def __next__(self):
    if not self.iterator:
      raise StopIteration

    x = self.iterator
    self.iterator = self.iterator.next
    return x


  def increment_length(self):
    self.length = self.length + 1


  def decrement_length(self):
    self.length = self.length - 1


  def append_nodes(self, *nodes):
    for node in nodes:
      self.append(node)


  def append(self, node):
    self.increment_length()

    if not self.head:
      self.head = node
      return

    if not self.tail:
      self.tail = node
      self.head.next = self.tail
      return

    self.tail.next = node
    self.tail = node


  def prepend_nodes(self, *nodes):
    for node in nodes:
      self.prepend(node)


  def prepend(self, node):
    self.increment_length()

    if not self.head:
      self.head = node
      return

    tmp = self.head
    self.head = node
    self.head.next = tmp


  def get_node_at(self, index):
    if index >= self.length:
      raise Exception('position does not exist')

    counter = 0

    for node in self:
      if counter == index:
        return node
      counter = counter + 1


  def insert_node_at(self, node, position):
    if position == 0:
      self.prepend(node)
      return

    self.increment_length()
    before_node = self.get_node_at(position - 1)
    next_node = before_node.next
    before_node.next = node
    node.next = next_node

  
  def pop(self):
    if (self.length == 0):
      raise Exception('List is empty')

    semi_last_node = self.get_node_at(self.length - 2)
    semi_last_node.next = None
    popped_node = self.tail
    self.tail = semi_last_node
    self.decrement_length()  
    popped_node.next = None  

    return popped_node

  
  def shift(self):
    if (self.length == 0):
      raise Exception('List is empty')

    shifted_node = self.head
    self.head = self.head.next
    list.length = list.length - 1
    self.decrement_length()
    shifted_node.next = None

    return shifted_node

  def print(self):
    output = ''
    
    for node in self:
      output += str(node)
      if node.next:
        output += ' ----> '

    print(output)


  def delete_node_at(self, index):
    prev_node = self.get_node_at(index-1)
    node_to_delete = self.get_node_at(index)

    prev_node.next = node_to_delete.next
    node_to_delete.next = None
    self.decrement_length()


list = LinkedList(Node(1), Node(2) ,Node(3), Node(4))
list.print()

list.insert_node_at(Node(5), 1)
list.print()

list.prepend_nodes(Node(10), Node(11))
list.print()

list.delete_node_at(2)
list.print()

list.pop()
list.print()

list.shift()
list.print()

