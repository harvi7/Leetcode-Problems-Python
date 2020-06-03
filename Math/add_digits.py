class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        
        temp_sum = 0
        while num > 0:
            onesPlace = num % 10
            temp_sum += onesPlace
            num //= 10
        return self.addDigits(temp_sum)