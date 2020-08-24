class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        currSum, sumMap = 0, {}
        sumMap[0] = -1
        for i in range(0, len(nums)):
            currSum += nums[i]
            if k != 0:
                currSum = currSum % k
            if currSum in sumMap:
                if i - sumMap[currSum] > 1:
                    return True
            else:
                sumMap[currSum] = i
        return False