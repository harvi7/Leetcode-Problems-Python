class Solution:
    def countArrangement(self, N: int) -> int:
        self.count = 0
        def calculate(N, pos, visited):
            if pos > N:
                self.count += 1
            for i in range(1, N + 1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    calculate(N, pos + 1, visited)
                    visited[i] = False
      
        visited = [False] * (N + 1)
        calculate(N, 1, visited)
        return self.count