class Solution:
    totalPaths = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, start, s):
            if not root:
                return
            s -= root.val 
            if s == 0:
                self.totalPaths += 1
            dfs(root.left,False, s)
            dfs(root.right,False, s)
            if start: 
                dfs(root.left,True,sum)
                dfs(root.right,True,sum)
        
        dfs(root, True, sum)
        return self.totalPaths