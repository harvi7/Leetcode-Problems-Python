class Solution:
    def removeDuplicates(self, S: str) -> str:
        sb = []
        for ch in S:
            if sb and ch == sb[-1]: 
                sb.pop()
            else: 
                sb.append(ch)
        return ''.join(sb)