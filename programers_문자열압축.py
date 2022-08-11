# start 1100
# 문제정의 : 가장짧은 문자열로 단축시켜라
# input : 1 s 1,000/ 소문자로만 되어있음
# output : 문자열 길이
from collections import Counter
def solution(s):
    answer = len(s)
    # logic 
    # 최대 input의 절반길이 까지는 검사 한다
    # for 문을 돌려서, 짜르고 counter함수를 활용하여 숫자를센다
    # counter 함수에서 나온 len(counter.keys())*n + len(counter.values()) 만약 counter.value > 0
    temp = []
    count = []
    t_answer = ''
    for n in range(1,(len(s)//2)+1):
        for i in range(0,len(s),n) :
            temp += [s[i:i+n]] if n > 1 else s[i:i+n]
        c = 1
        while temp :
            t = temp.pop()
            if t not in count :
                if count :
                    t_answer += str(c)+count.pop() if c > 1 else count.pop()
                    count.append(t)
                    c = 1
                else :
                    count.append(t)
            else :
                c+= 1
        t_answer += str(c)+count.pop() if c > 1 else count.pop()
        if answer > len(t_answer) :
            answer = len(t_answer)
        t_answer = ''
        
    return answer
