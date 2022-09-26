class UF(object):
    def __init__(self, n):
        # 记录连通分量个数
        self.__count__ = n
        # 存储若干个树
        self.__parent__ = [0] * n
        # 存储树的子树个数
        self.__size__ = [0] * n
        # 编号从0开始
        for i in range(n):
            self.__parent__[i] = i
            self.__size__[i] = 1

    def union(self, p: int, q: int):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root: return
        if self.__size__[p_root] < self.__size__[q_root]:
            self.__size__[q_root] += self.__size__[p_root]
            self.__parent__[p_root] = q_root
        else:
            self.__size__[p_root] += self.__size__[q_root]
            self.__parent__[q_root] = p_root
        self.__count__ -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, n):
        while self.__parent__[n] != n:
            self.__parent__[n] = self.__parent__[self.__parent__[n]]
            n = self.__parent__[n]
        return n

    def count(self):
        return self.__count__
