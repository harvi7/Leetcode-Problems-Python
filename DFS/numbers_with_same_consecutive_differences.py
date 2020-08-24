class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        result = []
        if N == 1:
            result.append(0)
        
        def dfs(num, N):
            if N == 0:
                result.append(num)
                return
            last_digit = num % 10
            if last_digit >= K:
                dfs(num * 10 + last_digit - K, N - 1)
            if K > 0 and last_digit + K < 10:
                dfs(num * 10 + last_digit + K, N - 1)
        for d in range(1, 10):
            dfs(d, N - 1)
        
        return result