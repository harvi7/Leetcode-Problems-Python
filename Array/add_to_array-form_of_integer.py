# https://leetcode.com/problems/add-to-array-form-of-integer/discuss/234488/JavaC%2B%2BPython-Take-K-itself-as-a-Carry

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:    
        for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A