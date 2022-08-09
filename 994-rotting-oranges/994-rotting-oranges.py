# 1254
# 문제정의 : m*n 에서 1분마다 썩은 오렌지의 4방향의 오랜지가 썩는다
#           오렌지가 다썩는데 걸리는 최소시간을 구하라
# input :  1 m n 10 / m row n col
# output : minimum number/ impossible -1
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time,fresh=0,0
        ROWS,COLS=len(grid),len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row<0 or col<0 or row==ROWS or col==COLS or
                       grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1