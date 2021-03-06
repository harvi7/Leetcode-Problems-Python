class Solution:
    def calculate(self, s: str) -> int:
        q = collections.deque()
        for c in s:
            if c != ' ':
                q.append(c)

        q.append(' ')
        
        num, prev, temp_sum = 0, 0, 0
        prevOp = '+'

        while q:
            c = q.popleft()
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                num = num * 10 + ord(c) - ord('0')
            else:
                if prevOp == '+':
                    temp_sum += prev
                    prev = num
                    
                if prevOp == '-':
                    temp_sum += prev
                    prev = -num
                
                if prevOp == '*':
                    prev *= num
                    
                if prevOp == '/':
                    prev //= num

                num = 0
                prevOp = c

        return temp_sum + prev