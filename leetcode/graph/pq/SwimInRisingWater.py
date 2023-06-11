import heapq


class SwimInRisingWater:
    def swimInWater(self, grid):
        N = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        time = 0

        while True:
            value, x, y = heapq.heappop(pq)
            print(time, value)
            time = max(time, value)

            if x == y == N - 1:
                return time
            dirs = [-1, 0, 1, 0, -1]
            for i in range(len(dirs) - 1):
                x1 = x + dirs[i]
                y1 = y + dirs[i + 1]
                if 0 <= x1 < N and 0 <= y1 < N and (x1, y1) not in visited:
                    visited.add((x1, y1))
                    heapq.heappush(pq, (grid[x1][y1], x1, y1))
