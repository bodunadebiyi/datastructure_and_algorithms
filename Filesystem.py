import re

class Node:
  def __init__(self, val, children=[]):
    self.val = val
    self.children = children
  
  def __str__(self):
    return str(self.val)

filesystem = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

filesystem_arr = filesystem.split("\n\t")
print(filesystem_arr)

def get_parent_node(children):
  for i in range(len(children) - 1, -1, -1):
    if '.' not in children[i].val:
      return children[i]

def construct_tree(input_data, root=None):
  if isinstance(input_data, str):
    if re.search(r'\t', input_data):
      construct_tree(
        re.sub(r'\t', '', input_data, count=1),
        get_parent_node(root.children)
      )
    else:
      root.children = root.children + [Node(input_data)]
    return

  for item in input_data:
    if root == None:
      root = Node(item)
    else:
      construct_tree(item, root)

  return root
    
def print_tree(root_node):
  if len(root_node.children):
    for node in root_node.children:
      print_tree(node)

def get_all_files(node, prepend='', result=[]):
  if '.' in node.val:
    result.append(prepend + node.val)
    return

  if node.children:
    for new_node in node.children:
      get_all_files(new_node, '{}{}/'.format(prepend, node.val), result)

  

root = construct_tree(filesystem_arr, None)
result = []
get_all_files(root, '', result)

answer = ''

for filename in result:
  if len(answer) < len(filename):
    answer = filename

print(result, answer)
