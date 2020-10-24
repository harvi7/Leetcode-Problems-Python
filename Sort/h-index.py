class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h, cit = 0, sorted(citations, reverse=True)
        for i, v in enumerate(cit):
            if v > i:
                h = i + 1
        return h