import collections


class TopoOrder(object):
    hasCycle = False

    def buildGraph(self, numCourses, edges):
        graph = collections.defaultdict(list)
        # 有向图
        for fr, to in edges:
            graph[fr].append(to)
        return graph

    def findOrder(self, numCourses, edges):
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
