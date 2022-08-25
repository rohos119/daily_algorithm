# start 2301
# 문제정의 : 소스 코드에 작성된 균형잡힌 괄호를 뽑아서 올바른 순서대로 배치하자
# input : 2 p 1000, '(,)'의 개수는 항상 같다
# return : 올바른 괄호로 바꾼 문자열 / 만약 이미 올바른 문자열이면 그대로 return
from collections import *
import re

def checkcorrect(s) :
    temp = deque(list(s))
    u = []
    while temp :
        t = temp.popleft()
        if t =='(' :
            u.append('(')
        else :
            if u :
                u.pop()
            else :
                break
                
    return False if u else True

def changeword(s) :
    temp = deque(list(s))
    u,v = '',''
    check = 0
    while temp :
        t = temp.popleft()
        u += t
        check = check-1 if t =='(' else check+1
        if check==0 :
            if checkcorrect(u) :
                answer += u
            else :
                changeword(''.join(temp))
            print(answer, u , v, temp) 
        

def solution(p):
    answer = ''
    # 입력이 빈 문자열인 경우, 빈 문자열 반환
    if p == '' :
        return p
    
    temp = deque(list(p))
    print(temp)
           
        
    return answer
