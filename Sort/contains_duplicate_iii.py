# https://leetcode.com/problems/contains-duplicate-iii/discuss/658158/python-well-explained-sliding-window-%2B-bucket-sort
# The main idea is splitting elements in nums into different buckets in terms of the value of t (for each element, divide by (t+1) for integer division).
# If the result is True, which means one of the following 3 cases hold:

# Two elements in the same bucket
# One in the previous bucket
# One in the next bucket
# If the case 2 or 3 holds, you need to check if their difference <= t.
# And there can be at most k buckets at any time. If i (counter in code) >= k, delete the (i-k)-th one.

# That's my understanding of the code. Hope it can help you.
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t>=0:
            bs,w = {}, t+1
            for i, v in enumerate(nums):
                b = v // w
                if b in bs:
                    return True
                else:
                    bs[b] = v
                    if (b-1 in bs and v-bs[b-1] <= t) or (b+1 in bs and bs[b+1]-v <= t):
                        return True
                    if i >= k:
                        del bs[nums[i-k] // w]
        return False 