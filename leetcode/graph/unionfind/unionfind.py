class UF(object):
    def __init__(self, n):
        # 记录连通分量个数
        self.count = n
        # 存储若干个树
        self.parent = [0] * n
        # 存储树的子树个数
        self.size = [0] * n
        # 编号从0开始
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def union(self, p: int, q: int):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root: return
        if self.size[p_root] < self.size[q_root]:
            self.size[q_root] += self.size[p_root]
            self.parent[p_root] = q_root
        else:
            self.size[p_root] += self.size[q_root]
            self.parent[q_root] = p_root
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def count(self):
        return self.count
