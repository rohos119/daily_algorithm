# start 0104
# 문제정의 :1은 땅, 0은 물로 표시되어있는 셀에서, 땅에서 가장 먼 물을 찾아라
# input : 1 n 100,
# output : maximized distance -< int / 만약 땅,물 모두 없는 경우 return -1
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        # logic
        # DFS ? BFS ? -> 어떤게 좋을까.. 음....
        # BFS로 풀기 위해서, 한개의 셀을 움직일때마다, 다음 셀과 거리를 넘겨야하고
        # DFS로 풀게 되면모든 방향으로 land를 찾을때 발생하는 콜스텍이 너무 많다
        # BFS로 풀자
        #print(grid,'\n')

        
        ### 0에서 1을 찾아서 가장 최소값을 반환한다는 관점 -> 0이 더 많을 경우 불리
        ### 34/37 통과, 3개는 시간초과 발생, 통과 못한 testcase에 대해서 값은 맞음 그러나 시간초과임
        ### 0 찾는 버전 11596ms ..... ㄷㄷ

        #         if len(grid) == 1 :
        #             return -1

        #         # 탐색 방법
        #         # 먼저 0인 곳에서 4방향으로 찾는다
        #         direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        #         # 순회 방법
        #         # 일단 전체 grid를 다 돌고 돌다가 0을 만나면 시작
        #         row, col = len(grid), len(grid[0])
        #         # default answer 
        #         # 만약 전부 땅이거나 전부 물일 경우 answer 값은 최신화가 되지 않음
        #         answer = -1
        #         for r in range(row) :
        #             for c in range(col) :
        #                 if grid[r][c] == 0 :
        #                     visitied = set()
        #                     visitied.add((r,c))
        #                     q = collections.deque([[[r,c],0]])
        #                     temp = []
        #                     while q :
        #                         target,dist =q.popleft()
        #                         #print(target,dist ,q)
        #                         x_t,y_t = target[0],target[1]
        #                         for x,y in direct :
        #                             if x_t+x < 0 or x_t+x > row or y_t+y<0 or y_t+y > col :
        #                                 continue

        #                             if 0 <= x_t+x <= row-1 and 0<= y_t+y <= col-1 :
        #                                 if (x_t+x,y_t+y) not in visitied :
        #                                     if grid[x_t+x][y_t+y] == 1:
        #                                         # print('return point',f'[{x_t+x},{y_t+y}]',abs((x_t+x)-r)+abs((y_t+y)-c))
        #                                         dist = abs((x_t+x)-r)+abs((y_t+y)-c)
        #                                         temp.append(dist)
        #                                         q = deque([])
        #                                         break

        #                                     visitied.add((x_t+x,y_t+y))
        #                                     dist = abs((x_t+x)-r)+abs((y_t+y)-c)
        #                                     q.append([[x_t+x,y_t+y],dist])       
        #                     if temp :
        #                         answer = max(answer,min(temp))
        #         return answer
        
        
        ### 1인곳에서 0을 찾는 방법
        
        one_grid = []
        visitied = set()
        for i in range(len(grid)) :
            for j in range(len(grid)):
                if grid[i][j] :
                    one_grid.append([i,j])
                    visitied.add((i,j))
                    
        if len(one_grid) == 0 or len(one_grid) == len(grid)*len(grid) :
            return -1
        
        one_grid = deque(one_grid)
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        dist = 0
        while one_grid :
            for _ in range(len(one_grid)) :
                x,y = one_grid.popleft()
                for dx,dy in direct :
                    if 0<=x+dx<=len(grid)-1 and 0<=y+dy<=len(grid[0])-1 :
                        if (x+dx,y+dy) not in visitied and grid[x+dx][y+dy] == 0:
                            visitied.add((x+dx,y+dy))
                            one_grid.append([x+dx,y+dy])
                    
            dist+=1
        return dist-1 
                        
                        