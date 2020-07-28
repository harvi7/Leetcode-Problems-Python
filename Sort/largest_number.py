# https://leetcode.com/problems/largest-number/discuss/729300/Python3-custom-comparator
 
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if x + y > y + x: return 1
            elif x + y == y + x: return 0
            else: return -1
                
        nums = [str(x) for x in nums]
        return "".join(sorted(nums, key = cmp_to_key(cmp), reverse = True)).lstrip("0") or "0"