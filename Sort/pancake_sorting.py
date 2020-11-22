class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        def flip(idx):
            for i in range(0, idx // 2 + 1):
                arr[i], arr[idx - i] = arr[idx - i], arr[i]
                
        for i in range(len(arr) - 1, 0, -1):
            for j in range(1, i + 1):
                if arr[j] == i + 1:
                    flip(j)
                    result.append(j + 1)
                    break
            flip(i)
            result.append(i + 1)
        return result
