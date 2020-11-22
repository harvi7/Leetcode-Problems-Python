class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: 
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: 
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans