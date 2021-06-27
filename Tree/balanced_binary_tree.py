class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        self.check = True
        
        def helper(root):
            l, r = 0, 0
            if root.left: l += helper(root.left)
            if root.right: r += helper(root.right)
            if abs(l - r) > 1: self.check = False
            return max(l, r) + 1
        
        helper(root)
        return self.check