class Solution:
    def __init__(self):
        self.M = 1000000007
    def checkRecord(self, n: int) -> int:
        a0l0 = 1
        a0l1 = 0
        a0l2 = 0
        a1l0 = 0
        a1l1 = 0
        a1l2 = 0
        for i in range(n + 1):
            a0l0_ = (a0l0 + a0l1 + a0l2) % self.M
            a0l2 = a0l1
            a0l1 = a0l0
            a0l0 = a0l0_
            a1l0_ = (a0l0 + a1l0 + a1l1 + a1l2) % self.M
            a1l2 = a1l1
            a1l1 = a1l0
            a1l0 = a1l0_
        return a1l0