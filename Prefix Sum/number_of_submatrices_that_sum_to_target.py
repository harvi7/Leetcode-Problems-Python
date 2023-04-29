class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for row in range(m):
            for col in range(1, n):
                matrix[row][col] += matrix[row][col - 1]
        
        count = 0
        
        for c1 in range(n):
            for c2 in range(c1, n):
                hmap = defaultdict(int)
                hmap[0] = 1
                curr_sum = 0
                
                for row in range(m):
                    curr_sum += matrix[row][c2] - (matrix[row][c1 - 1] if c1 > 0 else 0)
                    count += hmap[curr_sum - target]
                    hmap[curr_sum] += 1

        return count