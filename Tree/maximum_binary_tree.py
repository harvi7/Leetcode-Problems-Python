class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums))
    
    def construct(self, nums, l, r):
        if l == r:
            return None
        max_i = self.maxIndex(nums, l, r);
        root = TreeNode(nums[max_i])
        root.left = self.construct(nums, l, max_i)
        root.right = self.construct(nums, max_i + 1, r)
        return root
    
    def maxIndex(self, nums, l, r):
        max_i = l
        for i in range(l, r):
            if nums[max_i] < nums[i]:
                max_i = i
        return max_i