class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        
        sumTot, i = 0, 1
        while i * i <= num:
            if num % i == 0:
                sumTot += i;
                if i * i != num:
                    sumTot += num / i
            i += 1
                    
        return sumTot - num == num