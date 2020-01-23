class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(words) != len(pattern): 
            return False
        
        map = {}
        for i in range(len(pattern)):
            currChar = pattern[i]
            if currChar in map:
                if map[currChar] != words[i]:
                    return False            
            else:
                if words[i] in map.values():
                    return False
                map[currChar] = words[i]
        return True 