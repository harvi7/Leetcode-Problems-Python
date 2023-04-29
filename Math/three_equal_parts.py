class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        IMPOSSIBLE = [-1, -1]
        
        oneCount = sum(arr)
        if oneCount % 3: 
            return IMPOSSIBLE
        
        target_ones = oneCount // 3
        if target_ones == 0:
            return [0, len(arr) - 1]

        breaks = []
        currCount = 0
        for i, bit in enumerate(arr):
            if bit == 1:
                currCount += bit
                if currCount in {1, target_ones + 1, 2 * target_ones + 1}:
                    breaks.append(i)
                if currCount in {target_ones, 2 * target_ones, 3 * target_ones}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks
        
        if not(arr[i1 : j1 + 1] == arr[i2 : j2 + 1] == arr[i3 : j3 + 1]):
            return [-1, -1]

        trailing_zeros_left = i2 - j1 - 1
        trailing_zeros_mid = i3 - j2 - 1
        trailing_zeros = len(arr) - j3 - 1

        if trailing_zeros > min(trailing_zeros_left, trailing_zeros_mid): 
            return IMPOSSIBLE
        
        j1 += trailing_zeros
        j2 += trailing_zeros
        return [j1, j2 + 1]