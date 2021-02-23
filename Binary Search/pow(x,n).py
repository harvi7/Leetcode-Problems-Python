class Solution:
    def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             n = -n
#             x = 1 / x        
#         return self.helper(x, n)
    
#     def helper (self, x, n):
#         if n == 0: return 1
#         elif n % 2 == 0:
#             y = self.helper(x, n / 2)
#             return y * y
#         else:
#             return x * self.helper(x, n - 1)

#       Iterative
        if n == 0 or x == 1.0:
            return 1.0
        if x == 0:
            if n < 0:
                return float('inf')
            else:
                return 0.0
        if n < 0:
            x, n = 1/x, -n
            
        ans, num, power = 1.0, x, n
        while power != 1:
            if power % 2 == 0:
                num = num * num
                power /= 2
            else:
                ans *= num
                power -= 1
        
        return ans * num