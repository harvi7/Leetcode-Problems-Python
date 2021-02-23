class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 2:
            return a
        
        A = []
        while a > 1:
            for d in range(9, 1, -1):
                if a % d == 0:
                    a /= d
                    A.append(d)
                    break
            else:
                return 0

        ans = int("".join(map(str, A[::-1])))
        return ans if ans < 2**31 else 0