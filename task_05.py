class Node(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent



class BinarySearchTree():
    def __init__(self, preorder_list, root=None):
        self._root = Node(preorder_list[0])
        self.i = 0
        self.counter = 0
        self.preorder_list = preorder_list
        self.insert(self._root)
        self.sort_by()


    def insert(self, node):
        self.counter += 1
        if self.preorder_list[self.counter]:
            new_n = Node(self.preorder_list[self.counter])
            node.left = new_n
            new_n.parent = node
            self.insert(node.left)
        self.counter += 1

        if self.preorder_list[self.counter]:
            new_n = Node(self.preorder_list[self.counter])
            node.right = new_n
            new_n.parent = node
            self.insert(node.right)

    def sort_by(self):
        x = [i for i in self.preorder_list if i!= 0]
        self.preorder_list = sorted(x)
        self.in_order(self._root)


    def in_order(self, node):
        if node:
            self.in_order(node.left)
            if self.i < len(self.preorder_list):
                node.data = self.preorder_list[self.i]
                self.i += 1
            self.in_order(node.right)

    def find_sum(self, s):
        path1 = []
        s1 = s
        self._find_sum(self._root, s, s1, path1)
        return path1

    def _find_sum(self, node, s, s1, path1):

        if node.left and node.data <= s:
            self._find_sum(node.left, s - node.data, s1, path1)

        if node.left:
            self._find_sum(node.left, s, s1, path1)

        if node.right and node.data <= s:
            self._find_sum(node.right, s - node.data, s1, path1)

        if node.right:
            self._find_sum(node.right, s, s1, path1)

        if node.data == s:
            x = 0
            path = []
            while x != s1 and node:
                x += node.data
                path.append(node)
                node = node.parent

            if x == s1:
                path.reverse()
                path1.append(path)

    def root(self):
        return self._root

    def parent(self, node):
        return node.parent

    def left(self, node):
        return node.left

    def right(self, node):
        return node.right

    def key(self, node):
        return node.data



    def binary_tree_present(self): #Breadth-First Traversal
        self._root.level = 0
        queue = [self._root]
        out = []
        current_level = self._root.level
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
                out.append("\n")
            out.append(str(current_node.data) + " - ")
            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
        print("".join(out))


preorder_list1 = [1, 4, 6, 10, 0, 0, 0, 7, 0, 8, 0, 0, 2, 5, 0, 0, 3, 9, 0, 0, 0]
tree = BinarySearchTree(preorder_list1)
tree.binary_tree_present()
print(tree.find_sum(9))



