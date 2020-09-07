class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []

        for i in range(len(words)):
            charDict, curr, isValid = {}, words[i], False
            if len(curr) != len(pattern):
                continue
            for j in range(len(curr)):
                if pattern[j] in charDict and charDict[pattern[j]] != curr[j]:
                    isValid = False
                    break
                elif not pattern[j] in charDict and curr[j] in charDict.values():
                	isValid = False
                	break
                else :
                	charDict[pattern[j]] =  curr[j]
                	isValid = True
            if isValid:
            	result.append(curr)
        return result