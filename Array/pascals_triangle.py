class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = res[row_num - 1][j - 1] + res[row_num - 1][j]

            res.append(row)

        return re