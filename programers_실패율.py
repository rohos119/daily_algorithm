# start 1506 1532
# 문제정의 : 실패율(스테이지에서 클리어하지 못한 플레이어수 / 스테이지에 있는 플레이어수) 높은 스테이지 부터 내림차순으로 반환하라
# input : 1 N(스테이지 수) 500 / 1 stages(플레이어의 스테이) 2*1e5 / N+1은 N번째를 깬 플레이어
# output : 실패율이 높은 스테이지 부터 내림차순 정렬 -> list
# def solution(N, stages):
#     answer = []
    
#     # logic 그리디한 방법으로도 가능
#     # 전체에서 -1씩 감소시켜서 0이될 경우 스테이지라 생각 할 수 있다.
#     stay = len(stages)
#     pre_stay = 0
#     for i in range(1,N+1) :
#         for j in range(len(stages)) :
#             if stages[j]!=0 :
#                 stages[j] = stages[j]-1        
        
#         stay_cur = stages.count(0)-pre_stay
#         #print(stages,stay_cur,'/',stay)
#         answer.append([i,stay_cur/stay])
#         stay -= stay_cur
#         pre_stay += stay_cur
#         #print('answer',answer)
    
#     answer = sorted(answer, key =lambda x:-x[1])
#     return [a[0] for a in answer ]

from collections import Counter

def solution(N,stages) :
    
    # logic greedy 하게 dic 를 사용해볼까?
    check = Counter(stages)
    answer = {}
    sum_val = len(stages)
    for i in range(1,N+1) :
        if sum_val !=0 :
            answer[i]=check[i]/sum_val
            sum_val-=check[i]
        else :
            answer[i]=0

    return sorted(answer,key= lambda x:-answer[x])
