class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x        
        return self.helper(x, n)
    
    def helper (self, x, n):
        if n == 0: return 1
        elif n % 2 == 0:
            y = self.helper(x, n / 2)
            return y * y
        else:
            return x * self.helper(x, n - 1)