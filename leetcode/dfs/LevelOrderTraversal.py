import collections


class LevelOrderTraversal(object):
    def LevelOrderBottom(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res

    def levelOrderBottom2(self, root):
        deque, ret = collections.deque(), []
        if root:
            deque.append(root)
        while deque:
            level, size = [], len(deque)
            for _ in range(size):
                node = deque.popleft()
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            ret.append(level)
        return ret[::-1]
print("hell")