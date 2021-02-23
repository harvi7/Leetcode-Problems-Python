class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # res = set()
        # for char in s:
        #     if char in res:
        #         res.remove(char)
        #     else:
        #         res.add(char)
        # return len(res) <= 1
        return sum(v % 2 for v in collections.Counter(s).values()) < 2