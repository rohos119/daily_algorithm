#start 2304
# 문제정의 : circle 범위로 터지는 폭탄 묵음에서 한개를 터트렸을때 최대한 많이 터트릴 수 있는 폭탄개수를 구하라
# input : 1 [x,y,range] 100 / 1 x,y,range 1e5
# output : maxsize bomb

from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # logic
        # 원의 범위 안에 있다는 것을 판단을 x2+y2 <= r2 으로 정하면 가능하다.
        # 그렇다면 que 안에 어떻게 넣어야할까..?
        
        N = len(bombs)
        
        # step-1. build graph
        graph = collections.defaultdict(list) # list not set
        for i in range(N):
            xi, yi, ri = bombs[i]
            for j in range(N):
                if i == j:
                    continue
                xj, yj, rj = bombs[j]
                if (xj - xi) ** 2 + (yj - yi) ** 2 <= ri ** 2:
                    graph[i].append(j)
                    
        # step-2. bfs recursive
        # def bfs(start, visited):
        #     visited.add(start)
        #     for j in graph[start]:
        #         if j not in visited:
        #             bfs(j, visited)
        
        # step-2 bfs iterative
        def bfs(start, visited=None):
            if visited is None:
                visited = set()
            q = collections.deque([start])
            cnt = 0
            while q:
                i = q.popleft()
                if i not in visited:
                    cnt += 1
                    visited.add(i)
                    for j in graph[i]:
                        if j not in visited:
                            q.append(j)
            return cnt
            
        
        # 3. get res
        res = 0
        for i in range(N):
            visited = set()
            bfs(i, visited)
            res = max(res, len(visited))
        return res