class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -float('inf')
        self.recMaxSum(root)
        return self.maxSum
    
    def recMaxSum(self, current):
        if not current:
            return 0
        left = max(self.recMaxSum(current.left), 0)
        right = max(self.recMaxSum(current.right), 0)

        sum = current.val + left + right
        self.maxSum = max(sum, self.maxSum)
        return max(left, right) + current.val
        