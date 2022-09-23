from graph.dfs.TreeNode import TreeNode


class BinaryTreeUtils(object):

    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0
        if root.left:
            maxLeft = self.maxDepth(root.left)
        if root.right:
            maxRight = self.maxDepth(root.right)
        return max(maxLeft, maxRight) + 1

    def minDepth(self, root: TreeNode):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)

        if root.left is not None and root.right is None:
            return left_min + 1
        if root.right is not None and root.left is None:
            return right_min + 1
        if root.right is not None and root.left is not None:
            return min(left_min, right_min) + 1

    # 前序遍历
    def allPaths(self, root: TreeNode):
        if root is None:
            return
        res = []
        self.getPaths(root, "", res)

    def getPaths(self, root: TreeNode, path, res):
        if root is None:
            return
        path += str(root.val)
        if root.left is None and root.right is None:
            res.append(path)

        self.getPaths(root.left, path + "->", res)
        self.getPaths(root.right, path + "->", res)

    # def leftLeafNodes(self, root: TreeNode):

