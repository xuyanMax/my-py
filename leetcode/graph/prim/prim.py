import collections
import heapq
from typing import List


class prim(object):
    def __init__(self, connections: List[List[int]]):
        self.graph = self.buildGraph(connections)
        self.pq = []
        self.inMST = [False] * len(connections)
        self.inMST[0] = True
        self.weightSum = 0
        # 随便一个点开始切分，不妨选0 - 注意索引是从0开始
        self.cut(0)
        while self.pq:
            weight, to = heapq.heappop(self.pq)
            if self.inMST[to]:
                continue
            self.weightSum += weight
            self.inMST[to] = True
            self.cut(to)

    def cut(self, u):
        for _, v, w in self.graph[u]:
            if self.inMST[v]:
                continue
            # 加入横切边/临边
            heapq.heappush(self.pq, (w, v))

    @staticmethod
    def buildGraph(self, connections: List[List[int]]):
        graph = collections.defaultdict(list)
        for u, v, w in connections:
            graph[u].append((w, v))
            graph[v].append((w, u))
        return graph

    def weightSum(self):
        return self.weightSum

    # check if mst has included all graph nodes
    def allConnected(self):
        for i in self.inMST:
            if not i:
                return False
        return True
