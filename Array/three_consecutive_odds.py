class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                cnt = 0;
                continue
            cnt += 1
            if cnt == 3:
                return True
        return False