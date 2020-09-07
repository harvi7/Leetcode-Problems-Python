class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N, prev, future, ans = len(seats), -1, 0, 0

        for i in range(N):
            if seats[i] == 1:
                prev = i
            else:
                while future < N and seats[future] == 0 or future < i:
                    future += 1

                left = N if prev == -1 else i - prev
                right = N if future == N else future - i
                ans = max(ans, min(left, right))

        return ans