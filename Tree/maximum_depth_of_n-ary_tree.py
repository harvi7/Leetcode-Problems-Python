class Solution:  
    def maxDepth(self, root: 'Node') -> int:
        # BFS Solution
        # queue, depth = [], 0
        # if root: queue.append((root, 1))
        # depth = 0
        # for (node, level) in queue:
        #     depth = level
        #     queue += [(child, level+1) for child in node.children]
        # return depth
        if root is None: return 0
        return self.get_max_depth(root, 1, 1)
    
    # DFS Solution
    def get_max_depth(self, node, depth, max_depth):
        if node is None: return max_depth
        max_depth = max(depth, max_depth)
        for child in node.children:
            max_depth = self.get_max_depth(child, depth + 1, max_depth)
        return max_depth