class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        n = 10
        result = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(digits[start: start + length])
                if num >= low and num <= high:
                    result.append(num)
        
        return result