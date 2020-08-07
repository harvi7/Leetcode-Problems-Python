class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isValid(x1, x2, start, num):
            if start == len(num):
                return True
            x2 = x2 + x1
            x1 = x2 - x1
            temp_sum = str(x2)
            return num[start:].startswith(temp_sum) and isValid(x1, x2, start + len(temp_sum), num)
        
        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] == '0' and i > 1:
                return False
            x1 = int(num[:i])
            j = 1
            while (max(j, i) <= n - i - j):
                if num[i] == '0' and j > 1:
                    break
                x2 = int(num[i : i + j])
                if isValid(x1, x2, j + i, num):
                    return True
                j += 1
        return False