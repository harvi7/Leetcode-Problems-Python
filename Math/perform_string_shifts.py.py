class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shifts = 0
        for direction, amount in shift:
            if direction == 1:
                amount = -amount
            left_shifts += amount
            
        left_shifts %= len(s)
        s = s[left_shifts:] + s[:left_shifts]
        return s