class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bannedWords = set(banned)
        validWordCounts = {}       
        
        for i in "!?',;.":
            paragraph = paragraph.replace(i,' ')
        
        words = paragraph.lower().split()
        
        maxCount = 0
        result = ""
        
        for word in words:
            if not word in bannedWords:
                if word in validWordCounts:
                    validWordCounts[word] += 1
                else:
                    validWordCounts[word] = 1
        
                if validWordCounts[word] > maxCount:
                    result = word
                    maxCount = validWordCounts[word]
        return result