class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.groups = [-1] * N
        self.adj = [[] for _ in range(N)]

        for p in dislikes:
            self.adj[p[0] - 1].append(p[1] - 1)
            self.adj[p[1] - 1].append(p[0] - 1)
            
        for i in range(N):
            if self.groups[i] == -1 and not self.dfs(i, 0):
                return False
        return True
    
    def dfs(self, v, grp):
        if self.groups[v] == -1: self.groups[v] = grp
        else: return self.groups[v] == grp
        
        for n in self.adj[v]:
            if not self.dfs(n, 1 - grp):
                return False
        return True
            