class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sumTot = sum(A)
        if sumTot % 3 != 0: return False
        target, count, curSum = sumTot / 3, 0, 0
        for num in A:
            curSum += num
            if curSum == target:
                curSum = 0
                count += 1
        return count >= 3