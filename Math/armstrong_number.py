class Solution:
    def isArmstrong(self, N: int) -> bool:
        return sum(int(i) ** (len(str(N))) for i in str(N)) == N