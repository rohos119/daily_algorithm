# start 1049
# 문제정의 : 코스를 완벽하게 끝내라, 코스정보는 prerequisties안에 있고 [next, frist] 이다
# input : 1 numCourse 2000 , 0 prerequisites num*num-1 , a != b
# output : course 순서 list / 없으면 empty array [0]
from collections import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # logic 
        # DFS로 풀자/ BFS 도 괜춘
        # 일단 b 기준으로 sort하자, sort가 되있나?
        
        # BFS풀이
        graph = {i:[] for i in range(numCourses)}
        edge = [0]*numCourses
        for p in prerequisites :
            graph[p[1]].append(p[0])
            edge[p[0]] += 1
        
        # def bfs(edge,graph):
        pre = deque([i for i in range(numCourses) if edge[i] == 0])
        answer = []
        while pre :
            p = pre.popleft()
            answer.append(p)
            for g in graph[p] :
                # edge만큼 감소를 한다
                edge[g] -= 1
                # edge의 수만큼 감소해야 통과한것이므로
                # edge가 0이 될때는 통과 -> que에 들어간다 -> 다음으로 넘어간다의 의미
                if edge[g] == 0 :
                    pre.append(g)       

        if len(answer) != numCourses :
            return []
        return answer
        
        
        # return bfs(edge,graph)
    
        # DFS풀이
        
        
        
        
        