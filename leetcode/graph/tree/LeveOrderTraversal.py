from typing import List

import TreeNode


class LevelOrderTraversal:

    # 非递归
    @staticmethod
    def level(root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            res.append([node.val for node in queue])

            childNodes = []
            for node in queue:
                if node.left:
                    childNodes.append(node.left)
                if node.right:
                    childNodes.append(node.right)
            queue = childNodes
        return res

    # 递归
    def levelDfs(self, node: TreeNode, depth, res):
        if len(res) < depth:
            res.append([])
        res[depth - 1].append(node.val)
        if node.left:
            self.levelDfs(node.left, depth + 1, res)
        if node.right:
            self.levelDfs(node.right, depth + 1, res)

    def levelOrderDfs(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        res = []
        self.levelDfs(root, 1, res)
        return res
