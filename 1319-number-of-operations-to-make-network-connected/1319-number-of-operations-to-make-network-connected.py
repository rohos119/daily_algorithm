#2041

# 문제정의 : 주어진 n 개가 모두 연결되도록 만드는 최소 수
# input : 1 n 10*5 , 1 connections 10*5
# output : minium count/ -1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 연결이 되지 않는다면 -1을 반환, 연결 가능성이 있으면 탐색
        # 연결가능성을 어떻게 판단하는가?
        # connection.legth < n-1 을때는 무조건 -1
        if len(connections) < n-1 :
            return -1
        
        # 연결해야 할 pc의 갯수 = minium count
        # 연결되어 있지 않는 pc는 어떻게 찾을까? 
        # connections에 정보를 활용해서 그래프로 표현하자
        # 그래프로 표현했을때
        
        n_cables = len(connections)
        cnt_groups = 0
        n_pc = set(range(n))
        
        conn = defaultdict(list)
        for c in connections:
            a, b = c
            conn[a].append(b)
            conn[b].append(a)
        
        while n_pc:
            start_pc = n_pc.pop()
            que = deque([start_pc])
            cnt_groups += 1
            while que:
                cur = que.popleft()
                for nxt in conn[cur]:
                    if nxt in n_pc:
                        que.append(nxt)
                        n_pc.remove(nxt)
                                
        return cnt_groups - 1 