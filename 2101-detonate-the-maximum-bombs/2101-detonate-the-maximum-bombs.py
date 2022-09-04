#start 2304
# 문제정의 : circle 범위로 터지는 폭탄 묵음에서 한개를 터트렸을때 최대한 많이 터트릴 수 있는 폭탄개수를 구하라
# input : 1 [x,y,range] 100 / 1 x,y,range 1e5
# output : maxsize bomb

from collections import deque
class Solution:
    def dist(self, x, y):
        return sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # logic
        # 원의 범위 안에 있다는 것을 판단을 x2+y2 <= r2 으로 정하면 가능하다.
        # 즉, 두 원점 사이의 거리가 r 안에 있으면 가능
        # 그렇다면 que 안에 어떻게 넣어야할까..?
        res = 1
        for i in range(len(bombs)):
            current_res = 1
            visited = set()
            visited.add(i)
            q = collections.deque([i])
            while q:
                node = q.popleft()
                for c in range(len(bombs)):
                    if c not in visited and self.dist(bombs[node], bombs[c]) <= bombs[node][2]:
                        q.append(c)
                        visited.add(c)
                        current_res += 1
                        
            res = max(res, current_res)
                
        return res