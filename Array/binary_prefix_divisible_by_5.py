class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = A[0]
        check = True if num % 5 == 0 else False
        res = [check]
        
        for i in  range(1, len(A)):
            if A[i] == 1:
                num = num * 2 + 1
            else:
                num = num * 2
            if num % 5 == 0:
                res.append(True)
            else:
                res.append(False)
            num %= 5
        return res