class Solution:
    def isValid(self, s: str) -> bool:
        stack, arr = [], list(s)
        for i in range(len(s)):
            ch = arr[i];
            if ch == 'a':
                stack.append("a")
            elif ch == 'b' and stack and stack[-1] == "a":
                stack.pop();
                stack.append("ab");
            elif ch == 'c' and stack and stack[-1] == "ab":
                stack.pop()
            else:
                return False
        return False if stack else True