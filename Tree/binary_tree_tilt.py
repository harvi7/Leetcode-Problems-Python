class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root: return 0
        self.tilt = 0
        self.traverse(root)
        return self.tilt
    
    def traverse(self, root):
        if not root: return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val