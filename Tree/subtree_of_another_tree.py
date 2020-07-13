class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isSame(s, t):
            return True
        if s.left and self.isSubtree(s.left, t):
            return True
        if s.right and self.isSubtree(s.right, t):
            return True
        return False
    
    def isSame(self, s, t):
        if s == t:
            return True
        if not s or not t: 
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)