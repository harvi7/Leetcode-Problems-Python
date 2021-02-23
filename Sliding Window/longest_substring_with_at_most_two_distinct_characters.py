class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3: return n
        
        left, right, maxLen = 0, 0, 2
        hashmap = defaultdict()
        
        while right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) == 3:
                smallestIndex = min(hashmap.values())
                del hashmap[s[smallestIndex]]
                # move left pointer of the slidewindow
                left = smallestIndex + 1

            maxLen = max(maxLen, right - left)

        return maxLen