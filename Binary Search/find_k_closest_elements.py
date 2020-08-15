class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x <= arr[0]:
            return arr[0 : k]
        elif arr[n - 1] <= x:
            return arr[n -k : n]
        else: 
            left, right = 0, len(arr) - k
            while left < right:
                mid = (left + right) // 2
                if x - arr[mid] > arr[mid + k] - x:
                    left = mid + 1
                else:
                    right = mid
            return arr[left : left + k]