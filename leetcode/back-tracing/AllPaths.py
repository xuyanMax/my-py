class AllPath(object):
    # Given output directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
    # find all possible paths from node 0 to node n - 1, and return them in any order.
    # The graph is given as follows: graph[i] is output list of all nodes you can visit from node i
    # (i.e., there is output directed edge from node i to node graph[i][j]).

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        res = []
        dfs(0, [0])
        return res
