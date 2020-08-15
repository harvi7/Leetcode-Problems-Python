class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missed = 0
        for i in range(len(arr)):
            if i == 0:
                missed += arr[0] - 1
                if missed >= k:
                    return k
            else:
                missed += arr[i] - arr[i - 1] -1
                if missed >= k:
                    missed -= arr[i] - arr[i - 1] -1
                    result = arr[i - 1]
                    while missed < k:
                        missed += 1
                        result += 1
                    return result
        result = arr[-1]
        while missed < k:
            missed += 1
            result += 1
        return result