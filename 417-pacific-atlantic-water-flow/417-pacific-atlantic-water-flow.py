class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ans = []
        
        for c in range(len(heights[0])):
            self.dfs(0, c, heights, pac)
            self.dfs(len(heights) - 1, c, heights, atl)
        
        
        for r in range(len(heights)):
            self.dfs(r, 0, heights, pac)
            self.dfs(r, len(heights[0]) - 1, heights, atl)
        
            
        for i in range(len(heights)):
            
            for j in range(len(heights[0])):
                
                if (i, j) in pac and (i, j) in atl:
                    ans.append([i, j])
        return ans
        
    def dfs(self, i, j, heights, pac):
        
        pac.add((i, j))
        
        direc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        for di in direc:
            
            r = i + di[0]
            c = j + di[1]
            
            if r >= 0 and c >= 0 and r <= len(heights) -1 and c <= len(heights[0]) - 1:
                
                if heights[r][c] >= heights[i][j] and (r, c) not in pac:
                    self.dfs(r, c, heights, pac)