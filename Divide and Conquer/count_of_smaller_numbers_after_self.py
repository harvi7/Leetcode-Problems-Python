class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        items = [[v, i] for i, v in enumerate(nums)]  # record value and index
        result = [0] * n

        def merge_sort(items, lo, hi):
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            merge_sort(items, lo, mid)
            merge_sort(items, mid, hi)
            merge(items, lo, hi, mid)

        def merge(items, lo, hi, mid):
            i = lo 
            j = mid  
            sorted_items = []
            while i < mid and j < hi:
                if items[i][0] <= items[j][0]:
                    result[items[i][1]] += j - mid
                    sorted_items.append(items[i])
                    i += 1
                else:
                    sorted_items.append(items[j])
                    j += 1
                    
            while i < mid:
                result[items[i][1]] += j - mid
                sorted_items.append(items[i])
                i += 1
            while j < hi:
                sorted_items.append(items[j])
                j += 1
 
            for i in range(lo, hi):
                items[i] = sorted_items[i - lo]

        merge_sort(items, 0, n)

        return result
    