class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sums = 0
        arrSums = dict()
        arrSums[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            result += arrSums.get(sums-k,0)
            arrSums[sums] = arrSums.get(sums,0) + 1
        
        return(result)