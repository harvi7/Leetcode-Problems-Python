class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0 and source == destination: return True
        if len(edges) == 0 and source != destination: return False
    
        g = self.buildGraph(n, edges)
        
        colors = [0] * n 
        
        return self.dfs(g, source, destination, colors)
        
    def dfs(self, g, s, d, colors):
        if not g[s] or len(g[s]) == 0: return s == d

        colors[s] = 1
        for next in g[s]:
            if colors[next] == 1: return False
            if colors[next] == 0 and not self.dfs(g, next, d, colors): return False

        colors[s] = 2
        return True
        
    def buildGraph(self, n, edges):
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            fro, to = edge[0], edge[1]
            graph[fro].append(to)
            
        return graph   
            