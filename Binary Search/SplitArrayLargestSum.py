class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split (nums, validMaxSum):
            sumTot, count = 0, 1
            for num in nums:
                if sumTot + num > validMaxSum:
                    sumTot = num
                    count += 1
                else:
                    sumTot += num
            return count
        
        maxNum, sumTotal = max(nums), sum(nums)
        lo, hi = maxNum, sumTotal
        while lo < hi:
            mid = lo + (hi - lo) // 2
            numOfSubarrays = split(nums, mid)
            if numOfSubarrays > m:
                lo = mid + 1;
            else:
                hi = mid
        return lo
