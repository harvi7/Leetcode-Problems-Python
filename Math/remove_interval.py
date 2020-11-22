class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        for interval in intervals:
            if interval[0] > toBeRemoved[1] or interval[1] < toBeRemoved[0]:
                result.append([interval[0], interval[1]])
            else:
                if interval[0] < toBeRemoved[0]:
                    result.append([interval[0], toBeRemoved[0]])

                if interval[1] > toBeRemoved[1]:
                    result.append([toBeRemoved[1], interval[1]])

        return result