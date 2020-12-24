class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, root, low, high):
        if not root: return True
        if root.val <= low or root.val >= high: return False
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)