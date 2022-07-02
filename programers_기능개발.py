import math

# 문제 : 각 작업률을 100프로 완성시키기 위해 필요한 시간을 계산하고, 이전작업이 끝날때 같이 배포되는 수를 찾자

def solution(progresses, speeds):
    answer = []
    jinhang = []
    for p,s in zip(progresses,speeds) :
        if (100-p)%s != 0 : jinhang.append(int((100-p)/s)+1)
        else : jinhang.append(int((100-p)/s))
    
    count = 1
    check = 0
    pre = jinhang.pop(0)
    while jinhang :
        print(jinhang,pre,count, answer)
        if pre >= jinhang[0] :
            jinhang.pop(0)
            count += 1
        else :
            answer.append(count)
            pre = jinhang[0]
            count = 0
    answer.append(count)
    return answer
