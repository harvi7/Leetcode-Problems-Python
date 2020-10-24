class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        def DFS(node):
            if node.val == k: 
                self.kNode = node
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                DFS(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                DFS(node.right)
        DFS(root)        
        visited = set()
        q = collections.deque([self.kNode])
        while q:
            node = q.popleft()
            if node not in visited:
                if not node.left and not node.right:
                    return node.val
                visited.add(node)
                for neighbor in graph[node]:
                    q.append(neighbor)

