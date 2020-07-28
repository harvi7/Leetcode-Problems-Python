class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        aux = [0] * len(nums)
        aux[0] = nums[0]
        for k in range(1, len(nums)): 
            aux[k] = min(nums[k], aux[k - 1])
        
        stack = []
        stack.append(nums[-1])
        
        for j in range(len(nums) - 2, -1, -1):
            if nums[j] > aux[j]:
                while stack and stack[-1] <= aux[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
                
        return False