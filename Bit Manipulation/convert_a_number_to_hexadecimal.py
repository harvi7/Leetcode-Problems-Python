class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: 
            return '0'
        if num < 0:
            num = num + 2**32
        mp = '0123456789abcdef'  
        result = ''
        while num > 0:
            result = mp[num & 15] + result
            num = num >> 4
        return result