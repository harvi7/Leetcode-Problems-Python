class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0: return 0
        cols, rows, res = len(matrix[0]), len(matrix), 0
        heights = [0] * cols
        for row in matrix:
            for c in range(cols):
                if row[c] == '1': heights[c] += 1
                else: heights[c] = 0
            res = max(res, self.largestRectangleArea(heights))
        return res
    
    def largestRectangleArea(self, heights):
        if not heights or len(heights) == 0:return 0
        hist_len = len(heights)
        stack = []
        maxArea = 0
        i = 0
        while i <= hist_len:
            h = 0 if i == hist_len else heights[i]
            if not stack or h >= heights[stack[-1]]: 
                stack.append(i)
            else:
                currMax = stack.pop()
                maxArea = max(maxArea, heights[currMax] * (i if not stack else (i - 1 - stack[-1])))
                i -= 1
            i += 1

        return maxArea