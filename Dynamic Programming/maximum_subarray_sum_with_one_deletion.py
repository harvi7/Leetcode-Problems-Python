class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        del_elem, res, keep = arr[0], arr[0], arr[0]
        n = len(arr)
        for i in range(1, n):
            del_elem = max(keep, del_elem + arr[i])
            keep = max(keep + arr[i], arr[i])
            res = max(res, max(del_elem, keep))
        return res