class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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