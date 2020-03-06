class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = 0
        for num in nums:
            totalSum += num

        if k <= 0 or k > len(nums) or totalSum % k != 0: 
            return False
        
        return self.canPartition(0, nums,[False] * len(nums), k, 0, totalSum / k)
    
    def canPartition(self, start, nums, used, k, currentSum, targetSum):
        if k == 1: 
            return True
        if currentSum == targetSum:
            return self.canPartition(0, nums, used, k - 1, 0, targetSum)
        for i in range(start, len(nums)):
            if used[i] == False and currentSum + nums[i] <= targetSum:
                used[i] = True
                if self.canPartition(i + 1, nums, used, k, currentSum + nums[i], targetSum) :
                    return True
                used[i] = False
        
        return False