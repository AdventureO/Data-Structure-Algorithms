class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            node = self.root
            while node is not None:
                if item < node.data:
                    if node.left is None:
                        node.left = Node(item)
                        return
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(item)
                        return
                    else:
                        node = node.right

    def search(self, node, item):
        while node != None and node.data != item:
           if node.data < item:
               node = node.left
           else:
               node = node.right
        return item

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)

    def pre_order(self, node):
        if node:
            print(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data)

    def get_min(self, node):
        if node.left is None:
            return node.data
        else:
            return self.get_min(node.left)

    def get_max(self, node):
        if self.root is None:
            return "Tree is empty."
        else:
            if node.right is None:
                return node.data
            else:
                return self.get_max(node.right)

    def successor(self, node):
        if node.right != None:
            return self.get_min(node.right)
        parent = node.parent
        while parent != None and node == parent.right:
            node = parent
            parent = node.parent
        return parent

    def binary_tree_present(self): #Breadth-First Traversal
          self.root.level = 0
          queue = [self.root]
          out = []
          current_level = self.root.level
          while len(queue) > 0:
             current_node = queue.pop(0)
             if current_node.level > current_level:
                current_level += 1
                out.append("\n")
             out.append(str(current_node.data) + " ")
             if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
             if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
          print("".join(out))


tree = BinarySearchTree()
arr = [100, 20, 500, 30, 10, 40]

for x in arr:
    tree.insert(x)

print(tree.successor(tree.get_root()))
tree.binary_tree_present()
print("In-order Traversal: ")
tree.in_order(tree.get_root())
print("Pre-order Traversal: ")
tree.pre_order(tree.get_root())
print("Post-order Traversal: ")
tree.post_order(tree.get_root())


