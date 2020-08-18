class HashTable:
  hash = []

  class DataItem:
    def __init__(self, key, value):
      self.key = key
      self.value = value

    def __str__(self):
      return '{} --> {}'.format(self.key, self.value)

  def __init__(self, size):
    self.size = size
    for i in range(size):
      self.hash.append(None)

  def get_hash_index(self, key):
    return key % self.size

  def insert(self, item):
    hash_index = self.get_hash_index(item.key)
    nodes_touched = 0

    while nodes_touched <= self.size:
      nodes_touched = nodes_touched + 1
      if not self.hash[hash_index] or self.hash[hash_index].key == -1:
        self.hash[hash_index] = item
        return

      hash_index += 1
      hash_index %= self.size

    raise Exception("space filled")

  def search(self, key):
    hash_index = self.get_hash_index(key)
    nodes_touched = 0

    while nodes_touched <= self.size:
      nodes_touched += 1
      if not self.hash[hash_index] or self.hash[hash_index].key == -1:
        return None

      if self.hash[hash_index] and self.hash[hash_index].key == key:
        return self.hash[hash_index]
      
      hash_index += 1
      hash_index %= self.size

    return None

  def delete(self, key):
    node_to_delete = self.search(key)

    if not node_to_delete:
      return None
    tmp = HashTable.DataItem(node_to_delete.key, node_to_delete.value)

    node_to_delete.key = -1
    node_to_delete.value = None
    return tmp

  def __str__(self):
    stringified = ''
    index = 0

    for item in self.hash:
      if not item or item.key == -1:
        index = index + 1
        continue
      stringified += '{} ---> {} \n'.format(item.value, index)
      index = index + 1

    return stringified

