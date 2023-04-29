class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for i in range(0, len(s)):
        #     try:
        #         index = t.index(s[i])
        #     except ValueError: 
        #         return False
        #     t = t[index + 1:]
        # return True
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == LEFT_BOUND