class Node:
    left = None
    right = None

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def dfs(self, val=None):
        stack = [self.root]
        visited = [self.root]
        cwn = self.root

        while len(stack) > 0:
            if val and cwn.val == val:
                return cwn

            if cwn.left and cwn.left not in visited:
                stack.append(cwn.left)
                visited.append(cwn.left)
                cwn = cwn.left
            elif cwn.right and cwn.right not in visited:
                stack.append(cwn.right)
                visited.append(cwn.right)
                cwn = cwn.right
            else:
                stack.pop()
                if len(stack) > 0:
                    cwn = stack[-1]

        if val:
            return None

        return visited

    def insert(self, insert_to, val):
        node_to_attach = self.dfs(insert_to)

        if node_to_attach == None:
            raise Exception('Node to attach not found')

        if node_to_attach.left == None:
            node_to_attach.left = Node(val)
            return
        
        if node_to_attach.right == None:
            node_to_attach.right = Node(val)
            return
        
        raise Exception('Node doesnt have available branch')
    
    def is_leaf(self, node):
        return not node.left and not node.right

    def is_bst(self, node):
        if self.is_leaf(node):
            return True
        
        if node.left and node.right:
            if node.left.val < node.val and node.right.val > node.val:
                return True
        else :
            if node.left and node.left.val < node.val:
                return True

            if node.right and node.right.val > node.val:
                return True
        
        return False
        

    def max_sum(self):
        all_nodes = self.dfs()
        max_sum_sub_tree = None
        node_tree = []

        for node in all_nodes:
            if self.is_bst(node):
                total_sum = node.val + (node.left and node.left.val or 0) + (node.right and node.right.val or 0)
                if max_sum_sub_tree == None or max_sum_sub_tree < total_sum:
                    max_sum_sub_tree = total_sum
                    node_tree = [node.val, node.left and node.left.val, node.right and node.right.val]

        return max_sum_sub_tree, node_tree



node_a = Node(10)

tree = BinaryTree(node_a)
tree.insert(10, 77)
tree.insert(10, 5)
tree.insert(5, 14)
# tree.insert(5, 88)
# tree.insert(88, 8)
# tree.insert(77, 50)
# tree.insert(77, 120)

print(tree.max_sum())
'''
            10
        77       5
             14
'''


