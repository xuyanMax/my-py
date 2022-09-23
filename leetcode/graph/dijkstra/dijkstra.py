import heapq

from numpy import Inf

graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}


def dijkstra(src, graph):
    n = len(graph)

    # set up to source node distance list
    #dist = [[math.inf] * n for _ in range(m)]
    distToSrc = [Inf for _ in range(n)]
    distToSrc[src] = 0
    # set up priority queue
    pq = [(0, src)]
    while pq:
        dist, u = heapq.heappop()
        if distToSrc[u] < dist:
            continue
        for v, w in graph[u]:
            if w + distToSrc[u] < distToSrc[v]:
                distToSrc[v] = w + distToSrc[u]
                heapq.heappush(pq, (distToSrc[v], v))
    return distToSrc
