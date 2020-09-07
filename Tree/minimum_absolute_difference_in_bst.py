class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(node):
            if node:
                inorder(node.left) 
                self.minDiff = min(self.minDiff, abs(self.prev - node.val))
                self.prev = node.val  
                inorder(node.right)

        self.prev = self.minDiff = float('inf')
        inorder(root)      
        return self.minDiff