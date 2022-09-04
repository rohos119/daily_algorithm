#start 2304
# 문제정의 : circle 범위로 터지는 폭탄 묵음에서 한개를 터트렸을때 최대한 많이 터트릴 수 있는 폭탄개수를 구하라
# input : 1 [x,y,range] 100 / 1 x,y,range 1e5
# output : maxsize bomb

from collections import deque
class Solution: 
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # logic
        # 원의 범위 안에 있다는 것을 판단을 x2+y2 <= r2 으로 정하면 가능하다.
        # 즉, 두 원점 사이의 거리가 r 안에 있으면 가능
        # 그렇다면 que 안에 어떻게 넣어야할까..?
        
    ### 두 원점사이 거리 계산으로 구현 코드 -> 18.12%
    
    # def dist(self, x, y):
    #    sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))
    # def maximumDetonation(self, bombs: List[List[int]]) -> int:
    #         res = 1
    #         for i in range(len(bombs)):
    #             current_res = 1
    #             visited = set()
    #             visited.add(i)
    #             q = collections.deque([i])
    #             while q:
    #                 node = q.popleft()
    #                 for c in range(len(bombs)):
    #                     if c not in visited and self.dist(bombs[node], bombs[c]) <= bombs[node][2]:
    #                         q.append(c)
    #                         visited.add(c)
    #                         current_res += 1

    #             res = max(res, current_res)

    #         return res
        
        
        # 코드를 간결하게 줄였으나 속도가 나오지 않는다 왜? x,y의 range가 1e5이기 때문에...
        # 해서 거리를 구하는것을 하는것 보다 인덱스로 접근하는게 훨씬 빠르다.
    
    ### index를 활용한 BFS -> 32.32% 아직 속도가 너무느리다
    #         bomb_dic = {}
    #         for idx,bomb in enumerate(bombs) :
    #             visitied = set()
    #             visitied.add(idx)
    #             bomb_dic[idx] = []
    #             x,y,r = bomb
    #             for i,b in enumerate(bombs) :
    #                 x_t,y_t,r_t = b
    #                 if i not in visitied and (x_t-x)**2 + (y_t-y)**2 <= r**2 :
    #                     visitied.add(i)
    #                     bomb_dic[idx] += [i]

    #         answer = 0
    #         for a in bomb_dic :
    #             visited = [False] * len(bombs)
    #             q = deque([a])
    #             count = 0
    #             while q :
    #                 i = q.popleft()
    #                 if visited[i] == False :
    #                     count+=1
    #                     visited[i] = True
    #                     for t in bomb_dic[i] :
    #                         if visited[t] == False :
    #                             q.append(t)
    #             answer = max(answer,count)
    #         return answer
    
        # DFS 접근법
        # index로 graph 그리는 것까지는 동일
        bomb_dic = {}
        for idx,bomb in enumerate(bombs) :
            visitied = set()
            visitied.add(idx)
            bomb_dic[idx] = []
            x,y,r = bomb
            for i,b in enumerate(bombs) :
                x_t,y_t,r_t = b
                if i not in visitied and (x_t-x)**2 + (y_t-y)**2 <= r**2 :
                    visitied.add(i)
                    bomb_dic[idx] += [i]

        def dfs(root,visitied) :
            visitied.add(root)
            
            for target in bomb_dic[root] :
                if target not in visitied:
                    dfs(target,visitied)
        
        answer = 1
        for i in range(len(bombs)) :
            visitied = set()
            dfs(i,visitied)
            answer = max(answer,len(visitied))
        return answer
                