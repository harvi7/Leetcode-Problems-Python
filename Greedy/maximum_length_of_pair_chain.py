class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[1])
        last, count = float('-inf'), 0
        for pair in pairs:
            if pair[0] > last:
                last = pair[1]
                count += 1
        return count