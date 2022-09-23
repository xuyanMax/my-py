import heapq
import math

from numpy import Inf

# heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
# [[1,10,6,7,9,10,4,9]]
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

def minimumEffortPath(heights):
    """
    :type heights: List[List[int]]
    :rtype: int
    """
    # append (0, 0) with effort 0
    # (effort, x, y)
    pq = []
    # append (0, 0) with effort 0
    # (effort, x, y)
    heapq.heappush(pq, (0, 0, 0))
    # dist[i][j] effort from (i,j) to (0,0)
    dist = [[math.inf] * len(heights) for _ in range(len(heights[0]))]
    print(dist)
    dist[0][0] = 0
    dirs = [0, 1, 0, -1, 0]
    while pq:
        w, u, v = heapq.heappop(pq)
        print(w,u,v)
        if dist[u][v] < w:
            continue
        if u == len(heights) - 1 and v == len(heights[0]) - 1:
            print(dist)
            return dist[u][v]
        for i in range(len(dirs) - 1):
            next_u = u + dirs[i]
            next_v = v + dirs[i + 1]
            if next_u >= len(heights) or next_u < 0 or next_v >= len(heights[0]) or next_v < 0:
                continue
            effort = max(w, abs(heights[next_u][next_v] - heights[u][v]))
            if effort < dist[next_u][next_v]:
                dist[next_u][next_v] = effort
                heapq.heappush(pq, (effort, next_u, next_v))
    return 0


print(minimumEffortPath(heights))
