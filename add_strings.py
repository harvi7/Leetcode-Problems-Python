class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            tot_sum = carry
            if i >= 0: 
                tot_sum += int(num1[i])
                i -= 1
            if j >= 0: 
                tot_sum += int(num2[j])
                j -= 1
            result += str(tot_sum % 10)
            carry = tot_sum // 10
        if carry != 0: result += str(carry)
        return result[::-1]