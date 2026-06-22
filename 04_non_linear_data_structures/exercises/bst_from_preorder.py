from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def bstFromPreorder(preorder):
    idx = 0
    n = len(preorder)

    def helper(lower=float("-inf"), upper=float("inf")):
        nonlocal idx

        if idx == n:
            return None

        val = preorder[idx]

        if val < lower or val > upper:
            return None

        idx += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        return root

    return helper()


root = bstFromPreorder([8, 5, 1, 7, 10, 12])
print("")


def tree_to_list_level_order(root):

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


print(tree_to_list_level_order(root))
