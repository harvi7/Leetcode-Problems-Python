class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        uf = UF(n)
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge
        return None
    
class UF:
    def __init__(self, size):
        self.sub = [i for i in range(size)]
        
    def find(self, x):
        if x != self.sub[x]:
            self.sub[x] = self.find(self.sub[x])
        return self.sub[x]
    
    def union (self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        
        self.sub[xr] = self.find(yr)
        return True