class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        if k == size:
            return "0"
        
        stack = []
        counter = 0
        while counter < size:
            while k > 0 and stack and stack[-1] > num[counter]:
                stack.pop()
                k -= 1
            
            stack.append(num[counter])
            counter += 1
         
        while k > 0:
            stack.pop()
            k -= 1
        return "".join(stack).lstrip('0') or "0"