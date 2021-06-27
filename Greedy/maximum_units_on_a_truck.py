class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = 1)
        unitCount = 0
        for boxType in boxTypes:
            boxCount = min(boxType[0], truckSize)
            unitCount += boxCount * boxType[1]
            truckSize -= boxCount
            if truckSize == 0:
                break
        return unitCount