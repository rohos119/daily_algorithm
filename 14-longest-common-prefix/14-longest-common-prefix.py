# start : 2353
# 문제정의 : list에 있는 단어에서 가장 긴 공통된 접두사를 찾아라
# input : 1 str 200, 1 str[i].length 200
# output : common prefix else ""

from collections import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # logic
        # list의 끝까지 돌린다 1. for each 2. while 3. for index
        # 종료조건 : list 끝에 있을때
        
        q = deque(strs[0])
        answer =''
        idx = 1
        while idx < len(strs) :
            s_idx = 0
            temp = deque()
            while q :
                t = q.popleft() 
                if s_idx >= len(strs[idx]) :
                    break
                if t == strs[idx][s_idx]:
                    temp.append(strs[idx][s_idx])
                    s_idx += 1
                else :
                    break
            q = temp
            idx+=1
        
        while q :
            answer += q.popleft()
        return answer
        