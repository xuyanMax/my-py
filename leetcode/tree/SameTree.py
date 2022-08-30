class SameTree(object):
    #  p: TreeNode, q: TreeNode) -> bool
    def isSameTree(self, p, q):
        # if not p or not q:
        #     return p == q
        # if p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return False
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
