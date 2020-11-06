class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, sums = 0, 0
        arrSums = dict({0 : 1})
        for i in range(len(nums)):
            sums += nums[i]
            result += arrSums.get(sums-k,0)
            arrSums[sums] = arrSums.get(sums,0) + 1
        
        return result