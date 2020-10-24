class Solution:

    def __init__(self, rects: List[List[int]]):
        self.totPoints = 0
        self.rects = rects
        self.rectCumCount = []
        for rect in rects:
            self.totPoints += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.rectCumCount.append(self.totPoints)

    def pick(self) -> List[int]:
        targ = random.randint(0, self.totPoints - 1)
        low, high = 0, len(self.rects) - 1
        while low < high:
            mid = low + (high - low) // 2
            if self.rectCumCount[mid] <= targ: low = mid + 1
            else: high = mid

        rect = self.rects[low]
        width = rect[2] - rect[0] + 1
        height = rect[3] - rect[1] + 1
        ptsInRect = width * height
        ptStart = self.rectCumCount[low] - ptsInRect
        offset = targ - ptStart;
        return [rect[0] + offset % width, rect[1] + offset // width]