class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = {}

        def nSumCount(lists: List[List[int]]) -> int:
            addToHash(lists, 0, 0)
            return countComplements(lists, len(lists) // 2, 0)

        def addToHash(lists: List[List[int]], i: int, sum: int) -> None:
            if i == len(lists) // 2:
                m[sum] = m.get(sum, 0) + 1
            else:
                for a in lists[i]:
                    addToHash(lists, i + 1, sum + a)

        def countComplements(lists: List[List[int]], i: int, complement: int) -> int:
            if i == len(lists):
                return m.get(complement, 0)
            cnt = 0
            for a in lists[i]:
                cnt += countComplements(lists, i + 1, complement - a)
            return cnt

        return nSumCount([A, B, C, D])