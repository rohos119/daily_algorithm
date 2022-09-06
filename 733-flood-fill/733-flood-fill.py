class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        def valid(x, y):
            if 0 <= x < m and 0 <= y < n:
                return True
            return False
        
        def fill(i, j, match_color, fill_color):
            if not valid(i, j) or image[i][j] != match_color:
                return
            image[i][j] = fill_color
            for nx, ny in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                fill(nx, ny, match_color, fill_color)
                    
        match_color = image[sr][sc]
        if match_color == color:
            return image
        fill(sr, sc, match_color, color)
        return image