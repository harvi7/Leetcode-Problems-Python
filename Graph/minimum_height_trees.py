# https://leetcode.com/problems/minimum-height-trees/discuss/479559/Python3-O(n)-with-explanation

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:        
        if n == 1:
            return [0]       
        graph = {}
        
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u) 
        
        leaves = [x for x in range(n) if len(graph[x]) == 1]
        
        return self.prone(graph, leaves);
    
    def prone(self, graph, leaves):
        new_leaves = []
        if len(graph) <= 2:
            return graph.keys()

        for leaf in leaves:
            neighbor = graph.get(leaf)[0]
            graph.get(neighbor).remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
            graph.pop(leaf)
        
        return self.prone(graph, new_leaves);