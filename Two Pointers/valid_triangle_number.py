class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # count = 0
        # nums.sort()
        # for i in range(len(nums) - 2):
        #     k, j = i + 2, i + 1
        #     for j in range(i + 1, len(nums) - 1):
        #         if nums[i] != 0: 
        #             while k < len(nums) and nums[i] + nums[j] > nums[k]:
        #                 k += 1
        #             count += k - j - 1
        #         else: break
        # return count
        nums.sort()
        ans = 0
        L = len(nums)
        # c < (a+b)
        for i in range(L - 1, 1, -1):
            c = nums[i]
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > c:
                    ans += end - start
                    end -= 1
                elif nums[start] + nums[end] <= c:
                    start += 1
        return ans