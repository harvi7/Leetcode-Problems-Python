class Solution:     
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0
        self.maxDepth(root)
        return self.max_diameter
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            self.max_diameter = max(self.max_diameter, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
    