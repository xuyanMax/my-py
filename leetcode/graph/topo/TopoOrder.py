import collections


class TopoOrder(object):
    hasCycle = False

    def buildGraph(self, numCourses, edges):
        graph = collections.defaultdict(list)
        # 有向图
        for fr, to in edges:
            graph[fr].append(to)
        return graph

    def findOrder_dfs(self, numCourses, edges):
        graph = self.buildGraph(numCourses, edges)
        visited = [False] * numCourses
        onPath = [False] * numCourses
        postorder = []
        # 遍历图中每一个节点，通过visited标记已访问，通过onPath标记每一轮遍历中走过的节点
        for n in numCourses:
            self.traverse(n, graph, postorder, visited, onPath)

        # 存在环，不可拓扑排序
        if TopoOrder.hasCycle:
            return []
        # 逆序排序后，为拓扑排序结果
        return postorder[::-1]

    def traverse(self, u, graph, postorder, visited, onPath):
        if onPath[u]:
            # 发现环
            TopoOrder.hasCycle = True
        if onPath[u] or visited[u]:
            return
        # 前序遍历标记
        visited[u] = True
        onPath[u] = True
        for v in graph[u]:
            self.traverse(v, graph, postorder, visited, onPath)

        # 后序遍历位置，添加该节点
        onPath[u] = False
        postorder.append(u)

    def findOrder_bfs(self, numCourses, prerequisites):
        graph = self.buildGraph(numCourses, prerequisites)
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            in_degree[v] += 1
        queue = []
        for i in len(in_degree):
            if in_degree[i] == 0:
                queue.append(i)
        count = 0
        order = []
        while queue:
            curr = queue.pop()
            count += 1
            order.append(curr)
            for to in graph[curr]:
                in_degree[to] -= 1
                if in_degree[to] == 0:
                    queue.append(to)
        return order if count == numCourses else []
