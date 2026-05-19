class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root_value):
        self.root = BSTNode(root_value)

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)

        else:
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self, node, visit_list):
        if node is None:
            return

        self.in_order_traversal(node.left, visit_list)
        visit_list.append(node.value)
        self.in_order_traversal(node.right, visit_list)

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)

        return node


my_bst = BinarySearchTree(50)
my_bst.insert(25)
my_bst.insert(12)
my_bst.insert(30)
my_bst.insert(70)
my_bst.insert(65)
my_bst.insert(63)
my_bst.insert(67)
my_bst.insert(85)
my_bst.insert(80)


visit_order = []
my_bst.in_order_traversal(my_bst.root, visit_order)

print("in-order\t", visit_order)
print("12\t", my_bst.search(12))
print("64\t", my_bst.search(64))


my_bst.delete(70)
