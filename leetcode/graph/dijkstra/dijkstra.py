import heapq
from typing import Dict, List

from numpy import Inf

graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}


def dijkstra(src, g: Dict[int:List]):
    n = len(g)

    # set up to source node distance list
    # dist = [[math.inf] * n for _ in range(m)]
    distToSrc = [Inf for _ in range(n)]
    distToSrc[src] = 0
    # set up priority queue
    pq = [(0, src)]
    while pq:
        dist, u = heapq.heappop(pq)
        if distToSrc[u] < dist:
            continue
        for v, w in g[u]:
            if w + distToSrc[u] < distToSrc[v]:
                distToSrc[v] = w + distToSrc[u]
                heapq.heappush(pq, (distToSrc[v], v))
    return distToSrc
