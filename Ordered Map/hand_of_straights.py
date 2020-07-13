# https://leetcode.com/problems/hand-of-straights/discuss/135655/Python-O(nlgn)-simple-solution-with-intuition

from collections import Counter
from heapq import heappop, heapify

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        l, count = len(hand), Counter(hand)
        if l % W: return False
        if W == 1: return True
        heapify(hand)
        for i in range(l // W):
            start = heappop(hand)
            while count[start] == 0:
                start = heappop(hand)
            for i in range(W):
                if not count[start]: return False
                count[start] -= 1
                start += 1
        return True