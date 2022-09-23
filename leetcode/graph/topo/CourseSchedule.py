class CourseSchedule(object):
    def findOrder(self, numCourses, prerequisites):
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for p in prerequisites:
            indegree[p[0]].add(p[1])
            outdegree[p[1]].append(p[0])
        ret, start = [], [i for i in range(numCourses) if not indegree[i]]
        while start:  # start contains courses without prerequisites
            newStart = []
            for i in start:
                    ret.append(i)
                    for j in outdegree[i]:
                        indegree[j].remove(i)
                        if not indegree[j]:
                            newStart.append(j)
            start = newStart  # newStart contains new courses with no prerequisites
        return ret if len(ret) == numCourses else []  # can finish if ret contains all courses

    def findOrder2(self, numCourses: int, prerequisites):
        indegree = [0 for _ in range(numCourses)]
        relations = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            to = edge[0]
            fr = edge[1]
            indegree[to] += 1
            relations[fr].append(to)
        ret, start = [], [i for i in range(numCourses) if not indegree[i]]

        while start:
            newStart = []
            for i in start:
                ret.append(i)
                for j in relations[i]:
                    indegree[j] -= 1
                    if not indegree[j]:
                        newStart.append(j)
                start = newStart
        return ret if len(ret) == numCourses else []