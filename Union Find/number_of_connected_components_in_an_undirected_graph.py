class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ids = [0] * n
        for i in range(n):
            ids[i] = i
        for edge in edges:
            self.union(edge[0], edge[1], ids)
        comp_set = set()
        for i in range(n):
            comp_set.add(self.find(i, ids))
        return len(comp_set)
    
    def union(self, edge1, edge2, ids):
        parent1 = self.find(edge1, ids)
        parent2 = self.find(edge2, ids)
        ids[parent1] = parent2
    
    
    def find(self, edge, ids):
        if ids[edge] != edge: 
            ids[edge] = self.find(ids[edge], ids)
        return ids[edge]