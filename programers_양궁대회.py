# start 2244
# 목표정의 : 우승자는 n발을 다 쏜 후 n발을 쏜다, 만약 같은 점수를 우승자와 비우승자가 같게 맞췄을 경우 비우승자가 점수 가져감
#           아무리 많이 맞춰도 해당 점수밖에 못가져감, 라이언이 가장 큰 점수차이로 이길 수 있는 경우를 return
# input : 1 n 10 , info -> 10,9,8,7 ....0
# output : 라이언의 점수 info [10,9,8,7...0] / 없을땐 [-1]

    
from itertools import combinations_with_replacement

def solution(n, info):
    # logic
    # 어피치가 맞힌 화살 개수에 따라, 라이언의 화살을 맞출곳이 결정된다
    # 그럼 어떻게 결정 할 것인가?
    # 일단 라이언이 맞출수 있는 모든 가지수를 구한다 
    # 그리고 비교해서 결과를 출력 
    answer = [-1]
    maxGap = -1e9
    candidates = list(combinations_with_replacement(range(0, 11), n))
 
    for candidate in candidates:
        info2 = [0] * 11
        apeach, lion = 0, 0

        for score in candidate:
            info2[10 - score] += 1

        for score, (a, l) in enumerate(zip(info, info2)):
            if a == l == 0:
                continue
            elif a >= l:
                apeach += (10 - score)
            else:
                lion += (10 - score)

        if lion > apeach:
            gap = lion - apeach
            if gap > maxGap:
                maxGap = gap
                answer = info2

    return answer
