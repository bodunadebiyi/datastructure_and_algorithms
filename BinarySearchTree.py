class Node:
    left = None
    right = None

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return '{}'.format(self.val)

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        self.append_node(self.root, node)

    def find(self, val):
        return self.bfs(self.root, val)

    def bfs(self, root, val):
        if root.val == val:
            return root

        if root.val > val:
            if root.left == None:
                return -1
            return self.bfs(root.left, val)
        else:
            if root.right == None:
                return -1
            return self.bfs(root.right, val)

    def append_node(self, root, node):    
        if root.val > node.val:
            if root.left == None:
                root.left = node
                return

            self.append_node(root.left, node)
        else:
            if root.right == None:
                root.right = node
                return 

            self.append_node(root.right, node)
    
    def traverse_tree(self, balance=False):
        output = []
        self.run_preorder_traversal(output, self.root, balance)
        return output

    def run_preorder_traversal(self, results, node, balance=False):
        results.append(node.val)

        if node.left:
            self.run_preorder_traversal(results, node.left, balance)
        else:
            if balance:
                results.append(-1)

        if node.right:
            self.run_preorder_traversal(results, node.right, balance)
        else:
            if balance:
                results.append(-1)

    def serialize(self):
        result = self.traverse_tree(True)
        return ', '.join([str(x) for x in result])

    @staticmethod
    def deserialize(serialized_tree):
        serialized_arr = [int(x) for x in serialized_tree.split(',')]
        root = None
        current_root = None

        for val in serialized_arr:
            if val == -1:
                continue
        
            if root == None:
                root = Node(val)
                current_root = root
            elif current_root.val > val:
                current_root.left = Node(val)
                current_root = current_root.left
            else:
                current_root.right = Node(val)
                current_root = current_root.right
        
        return root




node_a = Node(20)
bst = BinarySearchTree(node_a)
bst.insert(Node(8))
bst.insert(Node(10))
bst.insert(Node(5))

# print(bst.find(54))
print(bst.traverse_tree())
serialized = bst.serialize()
print(serialized)

deserialized = BinarySearchTree.deserialize(serialized)
bst_two = BinarySearchTree(deserialized)
print(bst_two.traverse_tree())