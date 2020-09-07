# https://leetcode.com/problems/minimum-distance-between-bst-nodes/solution/

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(node):
            if node:
                inorder(node.left)
                self.minDiff = min(self.minDiff, node.val - self.prev)
                self.prev = node.val
                inorder(node.right)

        self.prev = float('-inf')
        self.minDiff = float('inf')
        inorder(root)
        return self.minDiff