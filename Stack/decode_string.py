class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, count = [], "", 0
        
        for c in s:
            if c == '[':
                stack.append(res)
                stack.append(count)
                res = ''
                count = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                res = prevString + num * res
            elif c.isdigit():
                count = count * 10 + int(c)
            else:
                res += c
        return res