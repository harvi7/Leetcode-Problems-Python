class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        
        def helper(i, j, color):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != color:
                return;
            image[i][j] = newColor;
            helper(i - 1, j, color)
            helper(i + 1, j, color)
            helper(i, j + 1, color)
            helper(i, j - 1, color)
              
        if image[sr][sc] == newColor: return image
        helper(sr, sc, image[sr][sc])
        return image
    
    