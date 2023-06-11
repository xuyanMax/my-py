# u, v, weight
import collections
import heapq
from numpy import Inf

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]


def networkDelayTime(self, times, N, K):
    # 定义：distToEnd[i] 的值就是节点到达节点i的最短路径权重

    queue, adj = [(0, K)], collections.defaultdict(list)
    dist = [Inf for _ in len(times)]
    for u, v, w in times:
        adj[u].append((v, w))
    while queue:
        t, node = heapq.heappop(queue)
        if dist[node] < t:
            continue
        dist[node] = t
        for v, w in adj[node]:
            if dist[v] > dist[node] + t:
                dist[v] = dist[node] + t
                heapq.heappush(queue, (t + w, v))
    max_val = max(dist)
    return max_val if max_val != Inf else -1
