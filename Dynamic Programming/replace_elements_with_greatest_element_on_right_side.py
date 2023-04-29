class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSoFar = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i];
            arr[i] = maxSoFar
            maxSoFar = max(maxSoFar, temp)
        return arr