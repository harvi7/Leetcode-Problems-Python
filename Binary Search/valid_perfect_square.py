class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        high, low = 100000, 1
        
        while low <= high:
            mid = low + (high - low) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                high = mid - 1
            else:
                low = mid + 1
        return False