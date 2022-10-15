import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    path_max = float("-inf")
    if not root:
        return

    def dfs(node):  # in-order
        nonlocal path_max
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        path_max = max(left + right + node.val, path_max)
        return node.val + max(left, right)

    dfs(root)
    return path_max
