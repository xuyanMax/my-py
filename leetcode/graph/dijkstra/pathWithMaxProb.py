import collections
import heapq
import math
from typing import List

edges = [[0, 1], [1, 2], [0, 2]]

print(edges[0])


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int):
    """
    :type n: int
    :type edges: List[List[int]]
    :type succProb: List[float]
    :type start: int
    :type end: int
    :rtype: float
    """
    prob = [-math.inf for _ in range(n)]
    # build adjacent list
    edge_map = collections.defaultdict(list)
    for i in range(len(edges)):
        u, v = edges[i][0], edges[i][1]
        print(u, v, succProb[i])
        # 无向图=双向图
        edge_map[u].append((succProb[i], v))
        edge_map[v].append((succProb[i], u))

    prob[start] = 1
    print(edge_map)
    # (prob, node)
    pq = [(-1, start)]
    while pq:
        p, u = heapq.heappop(pq)
        if prob[u] > -p:
            continue
        if u == end:
            return -p
        for p_v, v in edge_map[u]:
            if p_v * prob[u] > prob[v]:
                prob[v] = p_v * prob[u]
                heapq.heappush(pq, (-prob[v], v))

    return 0


print(maxProbability(3, edges, succProb=[0.5, 0.5, 0.3], start=0, end=2))
print(maxProbability(5,
                     [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
                     [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
                     3,
                     4))
