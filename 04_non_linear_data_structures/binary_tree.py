class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, new_value):
        new_node = TreeNode(new_value)

        if current_node.left is None:
            current_node.left = new_node
        else:
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node

    def pre_order_traversal(self, start_node, visit_list):
        if start_node is None:
            return
        # pre-recursion
        visit_list.append(start_node.value)

        self.pre_order_traversal(start_node.left, visit_list)
        self.pre_order_traversal(start_node.right, visit_list)

    def in_order_traversal(self, start_node, visit_list):
        if start_node is None:
            return
        self.in_order_traversal(start_node.left, visit_list)
        visit_list.append(start_node.value)
        self.in_order_traversal(start_node.right, visit_list)

    def post_order_traversal(self, start_node, visit_list):
        if start_node is None:
            return
        self.post_order_traversal(start_node.left, visit_list)
        self.post_order_traversal(start_node.right, visit_list)
        # post-recursion
        visit_list.append(start_node.value)

    def breadth_first(self, start_node, visit_list):
        queue = []
        queue.append(start_node)
        while queue:
            node = queue.pop(0)
            visit_list.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


bt = BinaryTree("A")

bt.insert_left(bt.root, "B")
bt.insert_right(bt.root, "C")
nodeB = bt.root.left
nodeC = bt.root.right
bt.insert_left(nodeB, "D")
bt.insert_right(nodeB, "E")
bt.insert_left(nodeC, "F")
bt.insert_right(nodeC, "G")
nodeG = nodeC.right
bt.insert_left(nodeG, "H")


visit_order = []
visit_order2 = []
visit_order3 = []
bt.pre_order_traversal(bt.root, visit_order)
print("pre-order\t", visit_order)

bt.in_order_traversal(bt.root, visit_order2)
print("in-order\t", visit_order2)


bt.post_order_traversal(bt.root, visit_order3)
print("post-order\t", visit_order3)


visit_order4 = []
bt.breadth_first(bt.root, visit_order4)
print("breadth\t\t", visit_order4)
