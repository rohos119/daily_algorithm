# start 2333 goal 40m
# 문제정의 : 캐릭터 처음 위치 1,1에서 상대팀으로 가는 가장 빠른길을 찾아라
# input : n*m 배열 -> maps, 1 n 100 , 1 m 100, 상대팀으로 갈 수 없는 경우도 있음
# output : 상대팀으로 갈 수 있는 경우 최소거리 or 상대팀으로 갈수 없는 경우 -1
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    visitied = [[0]*len(maps[0]) for _ in range(len(maps))]
    direct =  [(1, 0), (-1, 0), (0, 1), (0, -1)]    
    def BFS(x,y) :
        que = deque([])
        que.append((x,y))
        while que :
            x,y = que.popleft()
            for dx,dy in direct :
                if x+dx < 0 or x+dx >= n or y+dy <0 or y+dy >= m : continue
                if maps[x+dx][y+dy]==0 : continue
                if maps[x+dx][y+dy]==1 :
                    maps[x+dx][y+dy] = maps[x][y] + 1
                    que.append((x+dx,y+dy))
            if x == n-1 and  y == m-1 :
                return maps[x][y]         
        return maps[n-1][m-1]    
    answer = BFS(0,0)
    
    return -1 if answer == 1 else answer 
