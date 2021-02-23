class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth) + 1