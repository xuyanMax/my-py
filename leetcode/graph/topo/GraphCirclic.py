import collections


# 有向图，图中是否存在环，如果存在环，那就说明存在循环依赖
class GraphCirclic(object):
    @staticmethod
    def buildGraph(numNodes: int, edges: list[list[int]]):
        graph = collections.defaultdict(list)
        # 有向图
        for u, v in edges:
            graph[u].append(v)
        return graph

    # 能对所有节点进行拓扑排序，则返回true，否则由于存在环而失败
    onPath = []
    hasCycle = False
    visited = []

    @staticmethod
    def canFinish(numNodes, edges):
        GraphCirclic.onPath = [False] * numNodes
        graph = GraphCirclic.buildGraph(numNodes, edges)
        GraphCirclic.visited = [False] * numNodes
        GraphCirclic.hasCycle = False

        print(graph)
        for i in range(numNodes):
            GraphCirclic.traverse(i, graph)
        # print(GraphCirclic.onPath)
        return not GraphCirclic.hasCycle

    @staticmethod
    def traverse(node: int, graph):
        if GraphCirclic.onPath[node]:
            GraphCirclic.hasCycle = True
        if GraphCirclic.onPath[node] or GraphCirclic.onPath[node]:
            return False

        GraphCirclic.onPath[node] = True
        GraphCirclic.visited[node] = True

        for to in graph[node]:
            GraphCirclic.traverse(to, graph)

        GraphCirclic.onPath[node] = False

 


edges = [[0, 3], [1, 3], [3, 6], [3, 7], [7, 9], [4, 5], [5, 9]]
print(GraphCirclic.canFinish(10, edges))
