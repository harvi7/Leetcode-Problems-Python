class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            row, col, length = 0, len(matrix[0]) - 1, len(matrix)
            while row < length and col >= 0:
                if matrix[row][col] == target:
                    return True
                if matrix[row][col] > target:
                    col -= 1
                else:
                    row += 1
            return False
        return False