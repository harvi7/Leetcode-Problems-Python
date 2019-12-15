class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        max_list = []
        # BFS
        # row = [root]
        # while any(row):
        #     max_list.append(max(node.val for node in row))
        #     row = [child for node in row for child in (node.left, node.right) if child]
    
        if not root:
            return max_list
        self.dfs(root, max_list, 1)
    
        return max_list
    
    def dfs(self, node, max_list, depth):
        if not node:
            return
        if depth > len(max_list): 
            max_list.append(node.val)
        else: 
            max_list[depth-1] = max(node.val, max_list[depth-1])

        if node.left: self.dfs(node.left, max_list, depth+1)
        if node.right: self.dfs(node.right, max_list, depth+1)