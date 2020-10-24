class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for i in graph[node]:
                    dfs(i)
                    
        if len(connections) < n - 1:
            return -1
        graph = defaultdict(list)
        for u , v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        components = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components - 1