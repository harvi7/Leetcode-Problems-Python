class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = list(map(int, str(n)))
        i = len(a) - 2
        while i >= 0 and a[i + 1] <= a[i]:
            i -= 1
        
        if i < 0:
            return -1
        
        j = len(a) - 1
        while j >= 0 and a[j] <= a[i]:
            j -= 1
        
        a[i], a[j] = a[j], a[i]
        a[:] = a[: i + 1] + a[-1 : i : -1]
        a = [str(integer) for integer in a]
        res = int("".join(a))
        return  res if (res > n and res <= (2**31 - 1)) else -1