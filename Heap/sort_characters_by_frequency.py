class Solution:
    def frequencySort(self, s: str) -> str:
        char_map = {}
        for c in s: 
            char_map[c] =  char_map.get(c, 0) + 1
        
        sorted_map = sorted(char_map, key = char_map.get, reverse = True)
        
        result = ""
        for count in sorted_map:
            result += count * (char_map[count])
        return result