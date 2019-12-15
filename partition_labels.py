class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S or len(S) == 0: return null
       
        res = []      
        lastIndices = [0] * 26
        for i in range(len(S)):
            lastIndices[ord(S[i]) - ord('a')] = i
            
        start, end = 0, 0
        for i in range(len(S)):
            end = max(end, lastIndices[ord(S[i]) - ord('a')])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res