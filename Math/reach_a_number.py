class Solution:
    def reachNumber(self, target: int) -> int:
        currSum, k, target = 0, 0, abs(target)
        while currSum < target or (currSum != target and (currSum - target) % 2 != 0):
            currSum, k = currSum + k, k + 1
        return k - 1 if k > 0 else 0