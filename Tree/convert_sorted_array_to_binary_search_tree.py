class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        return self.constructBSTRecursive(nums, 0, len(nums) - 1)
    
    def constructBSTRecursive(self, nums, left, right):
        if (left > right):
            return None
        mid = left + (right- left) // 2
        current = TreeNode(nums[mid])
        current.left = self.constructBSTRecursive(nums, left, mid - 1)
        current.right = self.constructBSTRecursive(nums, mid + 1, right)
        return current