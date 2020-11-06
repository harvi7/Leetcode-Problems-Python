class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s) 
        if k == 0 or n == 0:
            return 0
        
        left, right = 0, 0
        hashmap = OrderedDict()

        max_len = 1
        
        while right < n:
            character = s[right]
            if character in hashmap:
                del hashmap[character]
            hashmap[character] = right
            right += 1

            if len(hashmap) == k + 1:
                _, del_idx = hashmap.popitem(last = False)
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len