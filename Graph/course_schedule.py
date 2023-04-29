# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         vis = [0] * numCourses
#         digraph = collections.defaultdict(set)
#         for dst, src in prerequisites:
#             digraph[src].add(dst)

#         def dfs(x):
#             vis[x] = -1
#             for y in digraph[x]:
#                 if vis[y] < 0 or (vis[y] == 0 and not dfs(y)):
#                     return False
#             vis[x] = 1
#             return True

#         for i in range(numCourses):
#             if vis[i] == 0 and not dfs(i): return False
#         return True

class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque
        graph = defaultdict(GNode)

        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        while nodepCourses:
            course = nodepCourses.pop()

            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
   
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        return True if removedEdges == totalDeps else False