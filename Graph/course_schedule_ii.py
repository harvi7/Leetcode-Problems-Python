# https://leetcode.com/problems/course-schedule-ii/discuss/59425/My-python-DFS-recursive-solution-(same-algorithm-for-207-and-210)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)] 
        visit = [0 for i in range(numCourses)]         
        res = []                                        
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        i = 0
        while i < numCourses:
            if len(graph[i]) == 0:
                res += i,               
                visit[i] = -1          
            i += 1

        def dfs(x, res):
            if visit[x] == -1:       
                return False
            if visit[x] == 1:    
                return True

            visit[x] = 1         
            for v in graph[x]:
                if dfs(v, res):
                    return True
            visit[x] = -1               
            res.append(x)             
            return False

        for i in range(numCourses):
            if dfs(i, res):
                return []           

        return res     