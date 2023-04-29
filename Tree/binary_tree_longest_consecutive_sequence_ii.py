class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxval = 0
        self.longestPath(root)
        return self.maxval
    
    def longestPath(self, root):
        if not root:
            return [0, 0]
        inr, dcr = 1, 1
        if root.left:
            l = self.longestPath(root.left)
            if root.val == root.left.val + 1:
                dcr = l[1] + 1
            elif root.val == root.left.val - 1:
                inr = l[0] + 1
    
        if root.right:
            r = self.longestPath(root.right)
            if root.val == root.right.val + 1:
                dcr = max(dcr, r[1] + 1)
            elif root.val == root.right.val - 1:
                inr = max(inr, r[0] + 1)
        
        self.maxval = max(self.maxval, dcr + inr - 1)
        return [inr, dcr]
