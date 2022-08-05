# start 2046 goal 30m end  1105 total 20m
# 문제정의 : 프로도가 숫자를 영어로 바꾼 문자열을 주면 프로도는 숫자를 맞춘다
# input : 1 s 50 / s는 zero or 0 인 경우는 없다
# output : int형 숫자
from collections import deque
import re
def solution(s):
    answer = ''
    # logic
    # isdigit을 활용하여 숫자일경우는 그냥 list에 밀어 넣기
    # isdigit이 아닐경우 re로 검사 검사했을때 key value로 값 넣기
    
    dictionary = {'zero' : '0', 'one' : '1','two' :'2' ,'three' :'3','four':'4',
                 'five' : '5', 'six' : '6','seven' :'7' ,'eight' :'8','nine':'9'}
    word = deque(list(s))
    temp = ''
    while word :
        w = word.popleft()
        if w.isdigit() :
            answer += w
        else :
            temp += w
            if temp in dictionary.keys() :
                answer += temp.replace(temp,dictionary[temp])
                temp = ''
    return int(answer)
