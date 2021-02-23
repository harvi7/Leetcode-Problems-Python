class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                count += 1
                left +=1
                right -=1
            elif s > k:
                right -= 1
            else:
                left += 1
        return count
        # Hashmap approach
        # cnt, ans = Counter(nums), 0
        # for val in cnt:
        #     ans += min(cnt[val], cnt[k - val])
        # return ans//2