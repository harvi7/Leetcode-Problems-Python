class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack, star_stack, str_len = [], [], len(s)
        
        for i in range(str_len):
            if s[i] == '(': open_stack.append(i)
            elif s[i] == '*': star_stack.append(i)
            else:
                if open_stack: open_stack.pop()
                elif star_stack: star_stack.pop()
                else: return False
        
        while open_stack:
            if not star_stack: return False
            elif open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else: return False
        return True