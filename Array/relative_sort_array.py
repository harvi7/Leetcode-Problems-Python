# https://leetcode.com/problems/relative-sort-array/discuss/343445/Python3.-Actually-easy-to-understand.-Beats-75-on-speed-and-100-on-memory

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        dic = {}
        for elem in arr1:
            dic[elem] = arr1.count(elem)
        output = []
        for elem in arr2:
            output += [elem] * dic[elem]
        extra_output = []
        for elem in set(arr1) - set(arr2):
            extra_output += [elem] * dic[elem]
        return output + sorted(extra_output)