# start 1512 end 1532
# 문제정의 : 4개지표로 성격 구분, 질문에 대답에 따라 성격유형은 판단할 수 있다. 이때 성격유형을 구하라
# input : 1 survey 1000 / 1 choice 1000 , 1 choice[i] 7
# output : (r,t)(c,f)(j,m)(a,n)/ 점수가 같을경우 사전 순으로 빠른것을 return
def solution(survey, choices):
    answer = ''
    sumdic = {'R' :0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    # logic
    # survey에 들어오는 원소들이 순서가 뒤죽 박죽이고, 첫번째인지 두번째인지 선택에 따라
    # 더하는 값이 다르기때문에 잘 확인을 한다
    for i in range(len(survey)) :
        if choices[i] > 4 :
            sumdic[survey[i][1]] += choices[i]-4
        else :
            sumdic[survey[i][0]] += 4-choices[i]
    
    for k,v in [('R','T'),('C','F'),('J','M'),('A','N')] :
        if sumdic[k] > sumdic[v] :
            answer += k 
        elif sumdic[k] < sumdic[v] :
            answer += v
        else :
            answer += min(k,v)
    
    return answer
