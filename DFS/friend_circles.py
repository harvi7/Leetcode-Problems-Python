class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M, visited, j)
                    
        visited, count = [0] * len(M), 0
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(M, visited, i)
                count += 1
        return count