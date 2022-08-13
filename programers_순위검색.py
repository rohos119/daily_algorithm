# 1332
# 문제정의 : 4가지 정보, 코딩테스트 결과가 담긴 하나의 문자열에서, 조건에 해당하는 사람이 몇명인지 확인
# input : 1 info 5*10e4 / query 언어, 직군, 경력, 소울푸드, X -는 고려안함
#          1 query 10e5
# infodetail -> cpp,java,python/ backend frontend / junior,senior/ chicken, pizza
from collections import deque
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    # logic -> 한가지 쿼리를 실행할때마다,, info를 다 탐색한다면 -> o(m*n) o(n^2)
    # 그렇다면 info를 가공해서 query가 접근할때 o(1)을 만들어야한다
    # - 일때는 어떻게 하지 ? 고민해봐야함
    # 그럼 그냥 key로 표현가능한 모든 조합을 만들고 -> 그 조합 dic 안에 다 넣는다
    # 일단 key -> query [100,200,250,]
    info_dict = {}
    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류
        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]
    
    for k in info_dict:
        info_dict[k].sort()
    
    for i,q in enumerate(query) :
        querys = deque([])
        temp = q.split(' and ')
        temp = temp[:-1] + temp[-1].split(' ')
        qu,val = '', temp[-1]
        for t in temp[:-1] :
            if t!='-' :
                qu+=t
                
        if qu in info_dict.keys():  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu]
            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(val))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
        
        
    return answer
