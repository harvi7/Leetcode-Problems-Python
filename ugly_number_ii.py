class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        index2, index3, index5 = 0, 0, 0
        for i in range(n):
            min_num = min(nums[index2] * 2, nums[index3] * 3, nums[index5] * 5)
            if min_num == nums[index2] * 2: index2 += 1
            if min_num == nums[index3] * 3: index3 += 1
            if min_num == nums[index5] * 5: index5 += 1
            nums.append(min_num)
        return nums[n - 1]