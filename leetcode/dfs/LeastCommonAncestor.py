import TreeNode


class LeastCommonAncestor:
    def solution(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root is None:
            return None
        if root == p or root == q:
            return root
        # 后序遍历
        left = self.solution(root.left, p, q)
        right = self.solution(root.right, p, q)

        if left and right:
            return root
        if left and right is None:
            return left
        if right and left is None:
            return right
        else:
            return None
